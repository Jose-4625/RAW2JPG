# RAW2JPG

Simplistic Python wrapper for the *.CR2(RAW format) to *.JPG conversion functionality of the rawkit library.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Required dependencies

```
NumPy
os
time
Image from PIL
raw from rawkit
```

### Installing

Install dependencies
```
pip3 install pillow
pip3 install numpy
pip3 install rawkit
apt-get install libraw-dev
```

Place RAW2JPG.py in project directory

## Running the tests

Once RAW2JPG.py is in the project directory, call the "test" method to ensure install is complete.
```
import RAW2JPG

test = RAW2JPG.RAW2JPG() # create RAW2JPG object
test.test() # call the builtin test method

OUTPUT:
checking dependencies...
RAW2JPG is ready to be used!
```

### What is checked in the "test" method?

```
1. Existence of NumPy in the workspace.
2. Existence of Rawkit in the workspace.
3. Existence of PIL in the workspace.
4. Successful import of "raw" from Rawkit
5. Successful import of "Image" from PIL
```

## Usage example

Already have a filesystem created:
```
import RAW2JPG

test = RAW2JPG.RAW2JPG() # create RAW2JPG object
test.test() # call the builtin test method

OUTPUT:
checking dependencies...
RAW2JPG is ready to be used!
```
Have a filesystem created by the program

```
import RAW2JPG

test = RAW2JPG.RAW2JPG() # create RAW2JPG object
test.test() # call the builtin test method

OUTPUT:
checking dependencies...
RAW2JPG is ready to be used!
```
## Authors

* **Jose Torres** - *Maintainer*

## License

*None*

## Acknowledgments

* Rawkit
