Introduction
============

This is the source repository for the paper:

Moore, J.K., Hnat, S.K, van den Bogert, A. "An elaborate data set on human gait
and the effect of mechanical perturbations", 2014.

The latest rendered version of the PDF can be viewed via the ShareLaTeX CI
system:

.. image:: https://www.sharelatex.com/github/repos/csu-hmc/perturbed-data-paper/builds/latest/badge.svg
   :target: https://www.sharelatex.com/github/repos/csu-hmc/perturbed-data-paper/builds/latest/output.pdf

Data
====

The data presented in the paper is available for download from Zenodo under the
Creative Commons CC0 license.

.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.13030.svg
   :target: http://dx.doi.org/10.5281/zenodo.13030

Software
========

The software used for the analysis is availabe in the ``src`` directory and as
as an open source Python package developed for this paper. The snapshot of the
GaitAnalysisToolKit is available via Zenodo:

.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.13159.svg
   :target: http://dx.doi.org/10.5281/zenodo.13159

License
=======

This repository is licensed under the `Creative Commons Attribution 4.0
International License`_.

.. image:: https://i.creativecommons.org/l/by/4.0/80x15.png
   :target: http://creativecommons.org/licenses/by/4.0

.. _Creative Commons Attribution 4.0 International License: http://creativecommons.org/licenses/by/4.0

Notes on editing the files
==========================

- Wrap text files to 79 characters.
- No tabs, use 2 spaces for indentation in LaTeX, 3 in RestructuredText, and 4
  in Python and Octave.
- Please edit in new Git branch and submit a Pull Request since we have
  multiple authors.
- The README is in RestructuredText format. See
  http://docutils.sourceforge.net/docs/user/rst/quickref.html for tips on the
  syntax.
- Figures belong in the ``figures`` directory, tables in the ``tables``
  directory and the source code used to generate them should be in the ``src``
  directory along with any instructions in ``README.rst``.The figures should be
  correctly sized plots in the PDF format. The generated figures and tables can
  be committed to the Git repo so that the ShareLatex CI builds. Be careful
  about uploading (lots) of giant binaries. Do not add data to the Git repo,
  use a data hosting repository.

Get the source
==============

Either clone the repository with Git::

   $ git clone https://github.com/csu-hmc/perturbed-data-paper.git

Or download and unpack the zip file::

   $ wget https://github.com/csu-hmc/perturbed-data-paper/archive/master.zip
   $ unzip master.zip

Change into the source directory::

   $ cd perturbed-data-paper

Basic LaTeX Build Instructions
==============================

To build the pdf from the latex source using the pregenerated figures and
tables in the repository, make sure you have an up-to-date latex suite
installed [1]_, download the source, and run ``make``.

.. [1] The minted package requires Python and the Pygments packaged. See the
   minted documentation for installation details or installation instructions
   for building from the raw data.

The default ``make`` target will build the document::

   $ make

View with your preferred PDF viewer::

   $ evince paper.pdf

Full build instructions
=======================

The full build instructions allow you to generate the figures and tables from
raw data and compile the LaTeX document.

Install dependencies
--------------------

In addition to the basic LaTeX dependency install the following Octave and
Python software.

Install Octave_ (>=3.8) from your system package manager or other binary
method, for example on Debian based Linux systems::

   $ sudo apt-get install octave

.. _Octave: http://www.octave.org

Install the `Anaconda Python Distribution`_, following the instructions on the
website, for example for 64 bit Linux::

   $ wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-2.1.0-Linux-x86_64.sh
   $ bash Anaconda-2.1.0-Linux-x86.sh

.. _Anaconda Python Distribution: http://continuum.io/downloads

Now create and activate a Conda environment with the main Python dependencies::

   $ conda create -n gait python=2.7 pip numpy=1.9.1 scipy=0.14.0 \
     matplotlib=1.4.2 pytables=3.1.1 pandas=0.15.1 pyyaml=3.11 seaborn=0.5.0 \
     pygments=2.0.1
   $ source activate gait

Finally, install the remaining dependencies with pip::

   (gait)$ pip install oct2py==2.4.0
   (gait)$ pip install DynamicistToolKit==0.3.5
   (gait)$ pip install GaitAnalysisToolKit==0.1.2

Get the data
------------

The data is available for download from Zenodo. It consists of two gzipped tar
balls of approximately 1.2GB each. Create a directory to house the data,
download, and unpack::

   (gait)$ mkdir raw-data
   (gait)$ cd raw-data
   (gait)$ wget https://zenodo.org/record/13030/files/perturbed-walking-data-01.tar.gz
   (gait)$ wget https://zenodo.org/record/13030/files/perturbed-walking-data-02.tar.gz
   (gait)$ tar -zxfv perturbed-walking-data-01.tar.gz
   (gait)$ tar -zxfv perturbed-walking-data-02.tar.gz
   (gait)$ rm perturbed-walking-data-01.tar.gz
   (gait)$ rm perturbed-walking-data-02.tar.gz
   (gait)$ cd ..

The above commands can also be run with the make target::

   (gait)$ make download

Configuration file
------------------

Copy the default configuration file to a file called ``config.yml``::

   (gait)$ cp default-config.yml config.yml

This can also be performed with a make target::

   (gait)$ make defaultconfig

Generate the tables and figures
-------------------------------

The plots can be generated by running the following scripts from the ``src``
directory::

   (gait)$ python src/unperturbed_perturbed_comparison.py

The tables can be generated with::

   (gait)$ python src/subject_tables.py

This can also be performed with a make target::

   (gait)$ make tables
   (gait)$ make figures

Build the pdf
-------------

::

   (gait)$ make pdf

The entire process from data download to pdf compilation can be run with a
single make target::

   (gait)$ make pdfraw
