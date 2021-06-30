# CFG Semantic Versioning 2.0.0 Analyzer

This is a simple context-free grammar (CFG) project, that implements the CYK to verify semantic versioning 2.0.0 expressions.
Grammar is defined inside in semverCFG.txt. It can be replaced by any other, but it must be in Chomsky's Normal Form (CNF). 
Official documentation for semantic versioning can be found here: https://semver.org/

## Installation (prerequisite)

To run the program you must install the following module [pip](https://pypi.org/project/pptree/) to print binary trees.

```bash
pip install pptree
```

And for a nice CLI, install [print-color](https://pypi.org/project/print-color/) to color debug.

```bash
pip install print-color
```

## Usage
To run the project just type:

```bash
py stxAnalyzer.py
```

A CLI will guide you thorugh inputs requested.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## References
https://github.com/huguintoch/Arithmetic-CFG
