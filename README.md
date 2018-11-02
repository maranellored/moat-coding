Moat Coding Challenge
=====================

Requirements
------------
To run the code and the tests in this project, you need [Python 2.7](https://www.python.org/download/releases/2.7/). 
The testing framework is [Nose](https://github.com/nose-devs/nose/).

To install nose, use [pip](https://pip.pypa.io/en/latest/installing.html). After installing pip, just run
```
$ pip install nose
```

FileParser
----------
The fileparser parses the given file that is provided on the comamnd line and counts the number of special characters - blank lines, braces, brackets, tabs, new line characters and prints them out. 

```
$ ./fileparser.py
Usage:
./fileparser.py <path/to/file>
$ ./fileparser.py /tmp/FileParser/fileparser.py
Number of open braces - 9
Number of closed braces - 9
Number of open brackets - 24
Number of closed brackets - 24
Number of blank lines - 12
Number of new lines - 68
Number of tabs - 0
```

Incr-e-dict
-----------
This project provides a single module that implements the incr_dict function. To run the tests for this module -

```
$ nosetests
....
----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK nosetests 
```

HashMap
-------
This project provides a single module with the hashmap class.
The hashmap is a simple hashmap that has been created using a list. It uses the block chaining method to resolve collisions. 
To run the tests for this module-

```
$ nosetests
..............
----------------------------------------------------------------------
Ran 14 tests in 0.009s

OK
```
