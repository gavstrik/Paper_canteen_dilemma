#!/usr/bin/env bash
# Build the TARK 2027 submission and report page-budget status.
# Usage: ./build.sh            (from latex/tark2027/)
# Exit non-zero if: compile fails, main text > LIMIT pages, live author comments,
# or undefined references/citations.
set -uo pipefail
cd "$(dirname "$0")"

LIMIT=10
OUT=build
mkdir -p "$OUT"

if ! tectonic -X compile main.tex --keep-intermediates --keep-logs --outdir "$OUT" >"$OUT/tectonic.out" 2>&1; then
  echo "COMPILE FAILED"; grep -E '^(error|!)' "$OUT/tectonic.out" | head -20; exit 1
fi

PDF="$OUT/main.pdf"
TOTAL=$(pdfinfo "$PDF" | awk '/^Pages:/{print $2}')
MAINEND=$(grep -oE '\\newlabel\{mainend\}\{\{[^}]*\}\{[0-9]+\}' "$OUT/main.aux" | grep -oE '[0-9]+\}$' | tr -d '}')

# Approximate fill of the last main-text page: text lines above the "References" heading
# (EPTCS fits 46 text lines per page; figures make this approximate).
FILL=$(pdftotext -layout -f "$MAINEND" -l "$MAINEND" "$PDF" - | awk '/^ *References *$/{exit} NF{n++} END{print n+0}')

status=0
echo "total pages:          $TOTAL"
echo "main text ends on p.  $MAINEND  (limit $LIMIT, refs/appendix excluded)"
echo "last main page lines: ~$FILL / 46"
if [ "$MAINEND" -gt "$LIMIT" ]; then echo "OVER BUDGET by $((MAINEND - LIMIT)) page(s)"; status=2; fi

LIVE=$(pdftotext "$PDF" - | grep -nE 'TOBO:|TSN:|RE:|@@@Add|XXXX' || true)
if [ -n "$LIVE" ]; then echo "LIVE AUTHOR COMMENTS IN PDF:"; echo "$LIVE" | cut -c1-160; status=3; fi

UNDEF=$(grep -E "(Reference|Citation) .* undefined" "$OUT/main.log" | sort -u || true)
if [ -n "$UNDEF" ]; then echo "UNDEFINED:"; echo "$UNDEF"; status=4; fi

OVERFULL=$(grep -c '^Overfull \\hbox' "$OUT/main.log" || true)
echo "overfull hboxes:      $OVERFULL"
exit $status
