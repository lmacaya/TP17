#! /bin/sh

pdflatex --shell-escape $1
open ${1%.tex}.pdf
