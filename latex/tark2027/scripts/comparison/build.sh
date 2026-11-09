#!/usr/bin/env bash
# Build figures_comparison.pdf (arXiv vs TARK figures side by side) into latex/tark2027/.
set -euo pipefail
cd "$(dirname "$0")"
# Knowledge diagram from body.tex, with the TARK inset, without the float/caption.
sed -n '/^\\begin{figure} %\[t\]$/,/label{fig:indistinguish}/p' ../../body.tex | sed -n '/tikzpicture/,/end{tikzpicture}/p' \
  | sed 's/fig5_logit_all/tark_fig6_logit_inset/' | sed '1s/^/\\[\n/' > diagram_nofloat.tex
echo '\]' >> diagram_nofloat.tex
tectonic -X compile figures_comparison.tex --outdir . >/dev/null
mv figures_comparison.pdf ../../figures_comparison.pdf
rm -f diagram_nofloat.tex
echo "wrote latex/tark2027/figures_comparison.pdf"
