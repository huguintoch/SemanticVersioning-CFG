# CFG Arithmetic Expression Analyzer

This is a simple contect-free grammar (CFG) project, that implements the CYK to verify arithmetic expressions.
Grammar is defined inside in arithmeticCFG.txt. It can be replaced by any other, but it must be in Chomsky's Normal Form (CNF). 
For current implementation, supported operators are: N (where N is any natural number), + , - , * , / , ( , )

## Installation (prerequisite)

To run the program you must install the following module [pip](https://pypi.org/project/pptree/) to print binary trees.

```bash
pip install pptree
```

## Usage
To run the project just run:

```bash
py CYK.py
```

A CLI will guide you thorugh inputs requested.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## References
CYK: https://github.com/mmheydari97/automata-cyk