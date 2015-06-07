# Pandoc-xepersian

*pandoc-xepersian* is a [pandoc] filter that converts english text to xepersian compatible version

This is just a latex filter

[pandoc]= http://pandoc.org/

## Usage

In order to convert persin Markdown to xepersian and applying this filter you must copy pandoc-xepersian.py into current directory, following command should be used:

	pandoc --latex-engine=xelatex -R -i in.md -o out.tex --filter ./pandoc-xepersian.py

Please make sure that the filter file is executable.


## Known bugs

It seems that in Windows OS filter usage resutls in encoding problems and it seems to be windows cmd and powershell's bug.


## Getting Help

If you have any difficulties with pandoc-eqnos, please feel welcome to [file an issue] on github so that we can help.


