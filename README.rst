Introduction
============

This is the source repository for the paper:

   Moore, J.K., Hnat, S.K, van den Bogert, A. "An elaborate data set on human
   gait and the effect of mechanical perturbations", 2014.

This repository contains or links to all of the information needed to reproduce
the results in the paper.

The latest rendered version of the PDF can be viewed via the ShareLaTeX_ CI
system:

.. image:: https://www.sharelatex.com/github/repos/csu-hmc/perturbed-data-paper/builds/latest/badge.svg
   :target: https://www.sharelatex.com/github/repos/csu-hmc/perturbed-data-paper/builds/latest/output.pdf

.. _ShareLaTeX: http://sharelatex.com

The preprint can be obtained from the PeerJ preprint server:

http://peerj.com/preprints/700

License and Citation
====================

The contents of this repository is licensed under the `Creative Commons
Attribution 4.0 International License`_.

.. image:: https://i.creativecommons.org/l/by/4.0/80x15.png
   :target: http://creativecommons.org/licenses/by/4.0

.. _Creative Commons Attribution 4.0 International License: http://creativecommons.org/licenses/by/4.0

If you make use of our work we ask that you cite us. The following are some
BibTeX formatted references that may be useful.

Data
----

::

   @misc{Moore2014,
     title={An elaborate data set on human gait and the effect of mechanical perturbations},
     url={http://dx.doi.org/10.5281/zenodo.13030},
     DOI={10.5281/zenodo.13030},
     publisher={ZENODO},
     author={Moore, Jason K. and Hnat, Sandra K. and van den Bogert, Antonie},
     year={2014}}

Software
--------

::

   @misc{DTK2014,
     title={DynamicistToolKit: Version 0.3.5},
     url={http://dx.doi.org/10.5281/zenodo.13253},
     DOI={10.5281/zenodo.13253},
     publisher={ZENODO},
     author={Jason K. Moore and Christopher Dembia},
     year={2014}}

::

   @misc{GATK2014,
     title={GaitAnalysisToolKit: Version 0.1.2},
     url={http://dx.doi.org/10.5281/zenodo.13159},
     DOI={10.5281/zenodo.13159}, publisher={ZENODO},
     author={Jason K. Moore and Nwanna, Obinna and Hnat, Sandra K. and van den Bogert, Antonie},
     year={2014}}

Preprint
--------

Note that this citation will always be one version behind because the preprint
is published after this repository is pinned to a version. Visit the DOI for
the most up-to-date citation.

::

   @article{10.7287/peerj.preprints.700v2,
     title = {An elaborate data set on human gait and the effect of mechanical perturbations},
     author = {Moore, Jason K and Hnat, Sandra K. and van den Bogert, Antonie J.},
     year = {2014},
     month = {12},
     keywords = {gait, data, control, perturbation},
     volume = {2},
     pages = {e700v2},
     journal = {PeerJ PrePrints},
     issn = {2167-9843},
     url = {http://dx.doi.org/10.7287/peerj.preprints.700v2},
     doi = {10.7287/peerj.preprints.700v2}
   }

Data
====

The data presented in the paper is available for download from Zenodo under the
Creative Commons CC0 license.

.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.13030.svg
   :target: http://dx.doi.org/10.5281/zenodo.13030

Software
========

The scripts used for the analysis is available in the ``src`` directory of this
repository and depend primarily on two open source Python packages developed
for this paper. The snapshots of the DynamicistToolKit_ 0.3.5 and the
GaitAnalysisToolKit_ 0.1.2 are available via both Zenodo and PyPi:

.. _DynamicistToolKit: http://github.com/moorepants/DynamicistToolKit
.. _GaitAnalysisToolKit: http://github.com/csu-hmc/GaitAnalysisToolKit

Be sure to read the installation instructions for the two packages.

DynamicistToolKit
   .. image:: https://zenodo.org/badge/doi/10.5281/zenodo.13253.svg
      :target: http://dx.doi.org/10.5281/zenodo.13253

   .. image:: https://pypip.in/version/DynamicistToolKit/badge.svg
      :target: https://pypi.python.org/pypi/DynamicistToolKit/
      :alt: Latest Version
GaitAnalysisToolKit
   .. image:: https://zenodo.org/badge/doi/10.5281/zenodo.13159.svg
      :target: http://dx.doi.org/10.5281/zenodo.13159

   .. image:: https://pypip.in/version/GaitAnalysisToolKit/badge.svg
      :target: https://pypi.python.org/pypi/GaitAnalysisToolKit/
      :alt: Latest Version

Furthermore, there are a variety of dependencies that must be installed on your
system to run the scripts. It is best to follow the installation instructions
provided by each of the following software packages for your operating system.

- Various unix tools [#]_: cd, bash, gzip, make, mkdir, rm, tar, unzip, wget
- The `Anaconda Python distribution`_ with Python 2.7 for ease of download and
  management of Python packages.
- Various Python packages: pip, numpy 1.9.1, scipy 0.14.0, matplotlib 1.4.2,
  pytables 3.1.1, pandas 0.15.1, pyyaml 3.11, seaborn 0.5.0, pygments 2.0.1,
  oct2py 2.4.2, DynamicistToolKit 0.3.5, GaitAnalysisToolKit 0.1.2
- Octave_ 3.8.1
- A LaTeX distribution which includes pdflatex. For example: MikTeX_ [Win],
  `TeX Live`_ [Linux], MacTeX_ [Mac].
- Various LaTeX Packages [#]_: minted_, lineno, graphicx, booktabs, cprotect,
  siunitx, inputenc, babel, ifthen, calc, microtype, times, mathptmx, ifpdf,
  amsmath, amsfonts, amssymb, xcolor, authblk, geometry, caption, natbib,
  fancyhdr, lastpage, titlesec, enumitem, bibtex
- Git_ (optional)
- MATLAB Version 7.9 (R2009b) and Simulink Toolbox Version 7.4

.. [#] These are available by default in Linux distributions, provided by Xcode
   on the Mac, and can be obtained via Cygwin, MinGW, or individual install on
   Windows.
.. [#] Most packages will likely be installed with your LaTeX distribution,
   otherwise follow the installation instructions provided by the package. Note
   that minted has abnormal dependencies: Python and Pygments. On Debian based
   systems you will need to install ``texlive-humanities`` and
   ``texlive-science`` to get all of the necessary packages.

.. _Anaconda Python Distribution: http://continuum.io/downloads
.. _Octave: http://octave.org
.. _MikTeX: http://miktex.org
.. _TeX Live: https://www.tug.org/texlive
.. _MacTeX: https://tug.org/mactex
.. _minted: https://github.com/gpoore/minted
.. _Git: http://git-scm.com

Get the source
==============

First, navigate to a desired location on your file system and either clone the
repository with Git [#]_ and change into the new directory::

   $ git clone https://github.com/csu-hmc/perturbed-data-paper.git
   $ cd perturbed-data-paper

or download with wget, unpack the zip file, and change into the new directory::

   $ wget https://github.com/csu-hmc/perturbed-data-paper/archive/master.zip
   $ unzip perturbed-data-paper-master.zip
   $ cd perturbed-data-paper-master

.. [#] Please use Git if you wish to contribute back to the repository. See
   CONTRIBUTING.rst for information on how to contribute.

Basic LaTeX Build Instructions
==============================

To build the pdf from the LaTeX source using the pre-generated figures and
tables in the repository, make sure you have an up-to-date LaTeX distribution
installed and run ``make`` from within the repository. The default ``make``
target will build the document, i.e.::

   $ make

You can then view the document with your preferred PDF viewer. For example,
Evince can be used::

   $ evince paper.pdf

Full build instructions
=======================

The full build instructions allow you to both generate the figures and tables
from raw data and compile the LaTeX document.

These commands should work as is on Unix based systems (Linux, Mac, etc).
Windows users should install Cygwin, MinGW, or each Unix tool separately to
make use of those commands. If Cygwin or MinGW is used, the Unix tools will
have to be executed in their respective terminal applications. All other
commands will need to be executed in the Windows CMD prompt.

Install dependencies
--------------------

In addition to the LaTeX dependencies described above, install the following
Octave and Python software.

Install Octave from your system package manager or other binary method, for
example on Debian based Linux systems::

   $ sudo apt-get install octave

Install the Anaconda Python distribution, following the instructions on the
website, for example for 64 bit Linux::

   $ wget http://09c8d0b2229f813c1b93-c95ac804525aac4b6dba79b00b39d1d3.r79.cf1.rackcdn.com/Anaconda-2.1.0-Linux-x86_64.sh
   $ bash Anaconda-2.1.0-Linux-x86_64.sh

Now create and activate a Conda [#]_ environment with the main Python dependencies.::

   $ conda create -n gait python=2.7 pip numpy=1.9.1 scipy=0.14.0 \
     matplotlib=1.4.2 pytables=3.1.1 pandas=0.15.1 pyyaml=3.11 seaborn=0.5.0 \
     pygments=2.0.1
   $ source activate gait

.. [#] Conda is a lightweight package manager that is used to download the
   exact versions of software into an isolated user installed environment.

On Windows, the last command does not need to be prepended with ``source``::

   $ activate gait

Finally, install the remaining dependencies with pip [#]_ which grabs the
correct versions from the `Python Package Index`_ (PyPi)::

   (gait)$ pip install oct2py==2.4.2
   (gait)$ pip install DynamicistToolKit==0.3.5
   (gait)$ pip install GaitAnalysisToolKit==0.1.2

.. [#] pip is also a lightweight package manager and is used here instead of
   Conda because the three packages listed do not yet have Conda binaries
   available.

.. _Python Package Index: https://pypi.python.org/pypi

Get the data
------------

The data is available for download from Zenodo. It consists of two gzipped tar
balls of approximately 1.2GB each. Create a directory to house the data,
download, and unpack::

   (gait)$ mkdir raw-data
   (gait)$ cd raw-data
   (gait)$ wget https://zenodo.org/record/13030/files/perturbed-walking-data-01.tar.gz
   (gait)$ wget https://zenodo.org/record/13030/files/perturbed-walking-data-02.tar.gz
   (gait)$ tar -zxvf perturbed-walking-data-01.tar.gz
   (gait)$ tar -zxvf perturbed-walking-data-02.tar.gz
   (gait)$ rm perturbed-walking-data-01.tar.gz
   (gait)$ rm perturbed-walking-data-02.tar.gz
   (gait)$ cd ..

The above commands can also be run with the make target::

   (gait)$ make download

Configuration file
------------------

Copy the default configuration to a file called ``config.yml``::

   (gait)$ cp default-config.yml config.yml

This can also be performed with a make target::

   (gait)$ make defaultconfig

Generate the tables and figures
-------------------------------

The plots can be generated by running the following scripts from the ``src``
directory::

   (gait)$ python src/unperturbed_perturbed_comparison.py

The tables can be generated with::

   (gait)$ python src/subject_table.py

This can also be performed with a make target::

   (gait)$ make tables
   (gait)$ make figures

Build the pdf
-------------

::

   (gait)$ make pdf

Complete Build
--------------

The entire process described above, i.e from data download to pdf compilation,
can also be run with a single make target::

   (gait)$ make pdfraw
