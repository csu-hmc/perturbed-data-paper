Introduction
============

This is the source repository for the paper:

   Moore, J.K., Hnat, S.K, van den Bogert, A. "An elaborate data set on human
   gait and the effect of mechanical perturbations", 2015.

This repository contains or links to all of the information needed to reproduce
the results in the paper.

The latest rendered version of the PDF can be viewed via the ShareLaTeX_ CI
system:

.. image:: https://www.sharelatex.com/github/repos/csu-hmc/perturbed-data-paper/builds/latest/badge.svg
   :target: https://www.sharelatex.com/github/repos/csu-hmc/perturbed-data-paper/builds/latest/output.pdf

.. _ShareLaTeX: http://sharelatex.com

The peer reviewed article can be obtained from PeerJ:

https://peerj.com/articles/918

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

Article
-------

::

   @article{10.7717/peerj.918,
    title = {An elaborate data set on human gait and the effect of mechanical perturbations},
    author = {Moore, Jason K. and Hnat, Sandra K. and van den Bogert, Antonie J.},
    year = {2015},
    month = {4},
    keywords = {Gait, Data, Control, Perturbation},
    volume = {3},
    pages = {e918},
    journal = {PeerJ},
    issn = {2167-8359},
    url = {https://dx.doi.org/10.7717/peerj.918},
    doi = {10.7717/peerj.918}
   }


Preprint
--------

You may want to cite the particular version. See the PeerJ website for details.

::

   @article{10.7287/peerj.preprints.700,
     title = {An elaborate data set on human gait and the effect of mechanical perturbations},
     author = {Moore, Jason K and Hnat, Sandra K. and van den Bogert, Antonie J.},
     year = {2014},
     month = {12},
     keywords = {gait, data, control, perturbation},
     volume = {2},
     pages = {e700},
     journal = {PeerJ PrePrints},
     issn = {2167-9843},
     url = {http://dx.doi.org/10.7287/peerj.preprints.700},
     doi = {10.7287/peerj.preprints.700}}

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

   @misc{Hnat2015,
     author={Hnat, Sandra K. and Moore, Jason K. and van den Bogert, Antonie J.},
     title={{Commanded Treadmill Motions for Perturbation Experiments}},
     month=mar,
     year=2015,
     doi={10.5281/zenodo.16064},
     url={http://dx.doi.org/10.5281/zenodo.16064}}

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

Data
====

The data presented in the paper is available for download from Zenodo under the
Creative Commons CC0 license.

.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.13030.svg
   :target: http://dx.doi.org/10.5281/zenodo.13030


.. image:: https://zenodo.org/badge/doi/10.5281/zenodo.16064.svg
   :target: http://dx.doi.org/10.5281/zenodo.16064

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

Dependency Installation
=======================

There are a variety of dependencies that must be installed on your system to
run the scripts. It is best to follow the installation instructions provided by
each of the following software packages for your operating system.

- Various unix tools [#]_: cd, bash, gzip, make, mkdir, rm, tar, unzip, curl,
  wget
- The `Anaconda Python distribution`_ with Python 2.7 for ease of download and
  management of Python packages.
- Various Python packages: pip, numpy 1.9.1, scipy 0.14.0, matplotlib 1.4.2,
  pytables 3.1.1, pandas 0.15.1, pyyaml 3.11, seaborn 0.5.0, pygments 2.0.1,
  oct2py 2.4.2, DynamicistToolKit 0.3.5, GaitAnalysisToolKit 0.1.2
- Octave_ 3.6.4-3.8.2
- A LaTeX distribution which includes pdflatex. For example: MikTeX_ [Win],
  `TeX Live`_ [Linux], MacTeX_ [Mac].
- Various LaTeX Packages [#]_: minted_, lineno, graphicx, booktabs, cprotect,
  siunitx, inputenc, babel, ifthen, calc, microtype, times, mathptmx, ifpdf,
  amsmath, amsfonts, amssymb, xcolor, authblk, geometry, caption, natbib,
  fancyhdr, lastpage, titlesec, enumitem, bibtex
- Git_ (optional)
- MATLAB Version 7.9 (R2009b) and Simulink Toolbox Version 7.4, including the
  Signal Processing Blockset Version 6.10 and Communications Blockset Version
  4.3

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

Debian Based Linux Distros (e.g. Ubuntu)
----------------------------------------

Install the TeXLive LaTeX distribution and some subpackages::

   $ sudo apt-get install texlive texlive-humanities texlive-science

Install Octave::

   $ sudo apt-get install octave

Install Matlab by purchasing it from http://mathworks.com and following their
recommended installation procedure for your operating system. Make sure Matlab
is on the system PATH.

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

Finally, install the remaining dependencies with pip [#]_ which grabs the
correct versions from the `Python Package Index`_ (PyPi)::

   (gait)$ pip install oct2py==2.4.2
   (gait)$ pip install DynamicistToolKit==0.3.5
   (gait)$ pip install GaitAnalysisToolKit==0.1.2

.. [#] pip is also a lightweight package manager and is used here instead of
   Conda because the three packages listed do not yet have Conda binaries
   available.

.. _Python Package Index: https://pypi.python.org/pypi

Windows
-------

The following is a recommended dependency installation procedure for Windows.

Install msysgit from http://msysgit.github.io to provide a Unix compatible BASH
terminal. Use the default options and select "Use Git from Git Bash Only" and
"Checkout windows-style, commit unix-style line endings". This puts a command
"Git Bash" in the start menu that opens a shell which can be used for most
commands.

Install Anaconda from http://continuum.io/downloads to provide Python and many
standard Python packages. Select install for "Just Me" unless you want to
install it system wide with adminstrator priveleges. Be sure both "Add anaconda
to my PATH environment variable" and "Register Anaconda as my default
python2.7" are checked. At this point Python is now available both in Git Bash
and the Windows Command Prompt (``cmd.exe``).

Download the lastest SWC Installer from
https://github.com/swcarpentry/windows-installer/releases. Install it by double
clicking the ``exe`` file and then make sure to click "launch installer" in the
last dialog. You'll then see a command prompt briefly listing the things it
installs. GNU Make is now available in Git Bash.

Download the "Basic Miktek" from http://miktex.org/download. Install with the
default options and after the install run "Update" from the Start Menu to
update the packages. ``pdflatex`` and other LaTeX tools are now available in
Git Bash and the Windows command prompt. Either use the package manager to
install all of the necessary LaTeX packages or wait to be prompted for them
during the first document compilation.

Download Octave 3.8.2 from http://mxeoctave.osuv.de [#]_.
Install the ``exe`` file (this requires a Java VM runtime to be installed). Now
add Octave's ``bin`` directory to the Windows PATH so that the ``octave``
command can be run from Git Bash and the Windows command prompt. In the
computer system properties advanced tab, select "Environment Variables" and
prepend ``C:\Users\<your-user-name>\.swc\bin;C:\Octave\Octave-3.8.2\bin;`` to
the contents of ``PATH``. The SWC ``bin`` must come before the Octave ``bin``
because Octave contains a command called ``make`` that will override the
``.swc\bin\make`` executable, which is undesirable.

.. [#] The 3.6.4 MinGW binary from
   http://sourceforge.net/projects/octave/files/Octave%20Windows%20binaries
   will also work.

Install Matlab by purchasing it from http://mathworks.com and following their
recommended installation procedure for your operating system. Make sure Matlab
is on the system PATH.

The conda environment can be created from Git Bash or the Windows command
prompt with the same commands as above::

   $ conda create -n gait python=2.7 pip numpy=1.9.1 scipy=0.14.0 \
     matplotlib=1.4.2 pytables=3.1.1 pandas=0.15.1 pyyaml=3.11 seaborn=0.5.0 \
     pygments=2.0.1

But the environment activation and subsequent Python commands must be run from
the Windows command prompt [#]_::

   > activate gait
   [gait] > pip install oct2py==2.4.2
   [gait] > pip install DynamicistToolKit==0.3.5
   [gait] > pip install GaitAnalysisToolKit==0.1.2

.. [#] They can be run from Git Bash but the activate command does not work and
   the full path to the environment's Python would need to be specified to run
   the Python scripts, see https://github.com/conda/conda/issues/747 for more
   details.

Get the source
==============

First, navigate to a desired location on your file system in the terminal (Git
Bash on Windows) and either clone the repository with Git [#]_ and change into
the new directory::

   $ git clone https://github.com/csu-hmc/perturbed-data-paper.git
   $ cd perturbed-data-paper

or download with curl, unpack the zip file, and change into the new directory::

   $ curl -o perturbed-data-paper-master.zip https://github.com/csu-hmc/perturbed-data-paper/archive/master.zip
   $ unzip perturbed-data-paper-master.zip
   $ cd perturbed-data-paper-master

.. [#] Please use Git if you wish to contribute back to the repository. See
   CONTRIBUTING.rst for information on how to contribute.

Basic LaTeX Build Instructions
==============================

The only dependencies for the basic build are: LaTeX + required packages,
Python + pygments, and a PDF viewer. Make sure pygments is installed in the
root conda environment::

   $ conda install pygments

To build the pdf from the LaTeX source using the pre-generated figures and
tables in the repository run ``make`` from the root of the repository. The
default ``make`` target will build the document, i.e.::

   $ make

You can then view the document with your preferred PDF viewer. For example,
Evince can be used on Linux::

   $ evince paper.pdf

Full build instructions
=======================

The full build instructions allow you to both generate the figures and tables
from raw data and compile the LaTeX document.

Any command that runs Python will have to be run in the Windows command prompt
on Windows. Otherwise, run the commands in the Git Bash on Windows.

Get the data
------------

The data is available for download from Zenodo. It consists of two gzipped tar
balls of approximately 1.2GB each and one of 2.6MB. Create a directory to house
the data, download, and unpack::

   $ mkdir raw-data
   $ cd raw-data
   $ curl -o perturbed-walking-data-01.tar.gz https://zenodo.org/record/13030/files/perturbed-walking-data-01.tar.gz
   $ curl -o perturbed-walking-data-02.tar.gz https://zenodo.org/record/13030/files/perturbed-walking-data-02.tar.gz
   $ curl -o perturbation-signals.tar.gz https://zenodo.org/record/16064/files/perturbation-signals.tar.gz
   $ tar -zxvf perturbed-walking-data-01.tar.gz
   $ tar -zxvf perturbed-walking-data-02.tar.gz
   $ tar -zxvf perturbation-signals.tar.gz
   $ rm perturbed-walking-data-01.tar.gz
   $ rm perturbed-walking-data-02.tar.gz
   $ rm perturbation-signals.tar.gz
   $ cd ..

The above commands can also be run with the make target::

   $ make download

Configuration file
------------------

If custom paths are needed, copy the default configuration to a file called
``config.yml``::

   $ cp default-config.yml config.yml

and edit the new file to suit.

Generate the tables and figures
-------------------------------

The plots can be generated by running the following scripts from the ``src``
directory. The ``gait`` conda environment should be activated first.

Linux/Mac
~~~~~~~~~

The figures can be generated with::

   $ source activate gait
   (gait)$ python src/unperturbed_perturbed_comparison.py
   (gait)$ matlab -nodisplay -nosplash -nodesktop -r "run('src/input_output_plot.m');exit;"
   (gait)$ matlab -nodisplay -nosplash -nodesktop -r "run('src/frequency_analysis.m');exit;"
   (gait)$ matlab -nodisplay -nosplash -nodesktop -r "run('src/lateral_perturbation_plot.m');exit;"

The tables can be generated with::

   (gait)$ python src/subject_table.py

This can also be performed with a make target::

   (gait)$ make figures
   (gait)$ make tables

Windows (using ``cmd.exe``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The figures can be generated with in ``cmd.exe``::

   > activate gait
   [gait] > python src/unperturbed_perturbed_comparison.py
   [gait] > matlab -nodisplay -nosplash -nodesktop -r "run('src/input_output_plot.m');exit;"
   [gait] > matlab -nodisplay -nosplash -nodesktop -r "run('src/frequency_analysis.m');exit;"
   [gait] > matlab -nodisplay -nosplash -nodesktop -r "run('src/lateral_perturbation_plot.m');exit;"

The tables can be generated with::

   [gait] > python src/subject_table.py

The ``figures`` and ``tables`` make targets will fail in the Windows command
prompt because make is only available in Git Bash.

Build the pdf
-------------

After the figures and tables are generated, the PDF can be built as before::

   $ make pdf

Complete Build
--------------

The entire process described above, i.e. from data download to PDF compilation,
can also be run with a single make target (only Linux/Mac)::

   (gait)$ make pdfraw
