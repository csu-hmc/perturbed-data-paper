pdf: paper.tex tables/subjects.tex figures/unperturbed-perturbed-boxplot-comparison.pdf figures/unperturbed-perturbed-comparison.pdf figures/frequency_analysis.pdf figures/input_vs_output.pdf
	pdflatex -shell-escape paper.tex
	bibtex paper.aux
	pdflatex -shell-escape paper.tex
	pdflatex -shell-escape paper.tex
pdfraw: download defaultconfig tables figures pdf
download:
	mkdir raw-data
	wget -O raw-data/perturbed-walking-data-01.tar.gz https://zenodo.org/record/13030/files/perturbed-walking-data-01.tar.gz
	wget -O raw-data/perturbed-walking-data-02.tar.gz https://zenodo.org/record/13030/files/perturbed-walking-data-02.tar.gz
	wget -O raw-data/perturbation-signals.tar.gz https://zenodo.org/record/16064/files/perturbation-signals.tar.gz
	tar -C raw-data -zxf raw-data/perturbed-walking-data-01.tar.gz
	tar -C raw-data -zxf raw-data/perturbed-walking-data-02.tar.gz
	tar -C raw-data -zxf raw-data/perturbation-signals.tar.gz
	rm raw-data/perturbed-walking-data-01.tar.gz
	rm raw-data/perturbed-walking-data-02.tar.gz
	rm raw-data/perturbation-signals.tar.gz
defaultconfig: default-config.yml
	cp default-config.yml config.yml
figures: config.yml raw-data/README.rst raw-data/T020/meta-020.yml raw-data/T020/mocap-020.txt raw-data/T020/record-020.txt
	python src/unperturbed_perturbed_comparison.py
	matlab -nodisplay -nosplash -nodesktop -r "run('src/input_output_plot.m');exit;"
	matlab -nodisplay -nosplash -nodesktop -r "run('src/frequency_analysis.m');exit;"
	matlab -nodisplay -nosplash -nodesktop -r "run('src/lateral_perturbation_plot.m');exit;"
tables: config.yml raw-data/README.rst
	python src/subject_table.py
clean:
	(rm -rf *.ps *.log *.dvi *.aux *.*% *.lof *.lop *.lot *.toc *.idx *.ilg *.ind *.bbl *.blg *.cpt)
cleandata:
	rm -rf raw-data processed-data
