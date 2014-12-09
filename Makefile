pdf:
	pdflatex -shell-escape paper.tex
	bibtex paper.aux
	pdflatex -shell-escape paper.tex
	pdflatex -shell-escape paper.tex
clean:
	(rm -rf *.ps *.log *.dvi *.aux *.*% *.lof *.lop *.lot *.toc *.idx *.ilg *.ind *.bbl *blg)
