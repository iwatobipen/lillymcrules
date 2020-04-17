# lillymcrules

## this is helper script for LillyMedChem-Rules

## Requirements

- https://github.com/IanAWatson/Lilly-Medchem-Rules
- click

## Install

- edit FILTERPATH to the path where lillymedchem rules are installed
- Then type the script
```
$ pip install -e .
# or
$ pip install .
```
- Now you can use lillyfilter command

## Basic usage

- input file must have SMILES strings.
- The first line is SMILEs and the second line is molecular ID.

```
$ lillyfilter <yourfile.smi> [-o <outputfile.smi>,]
```

- default outputfilename is ok.smi
- And after processing the inputfile, the code aggricate all resuts inculdes passed and failed molecules to a csvfile.
