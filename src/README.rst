Get the Data
============

Install Dependencies
====================

::

   $ apt-get install octave
   $ conda create -n perturbed-data-paper numpy=1.8.2 scipy=0.14.0 matplotlib=1.4.0 pytables=3.1.1 pandas=0.12.0 pyyaml=3.11
   $ source activate perturbed-data-paper
   (perturbed-data-paper)$ pip install DynamicistToolKit==0.3.5 oct2py==2.4.0 seaborn==0.4.0
   (perturbed-data-paper)$ pip install -e ~/src/GaitAnalysisToolKit

Run the Scripts
===============

::

   (perturbed-data-paper)$ cd src/
