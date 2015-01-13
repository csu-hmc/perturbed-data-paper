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
