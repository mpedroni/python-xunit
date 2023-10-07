# python-xunit

A simple testing framework, inspired by the xUnit framework family, for Python. I'm following along with the Kent Beck's [Test-Driven Development: By Example](https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530) book.

The main goal of this project is to create a testing framework (with a Test-Driven Development approach) and use this framework to test the framework itself (yes, I know, pretty weird idea).

Currently, the framework is able to run tests and report the results. It also supports `setUp` and `tearDown` methods.

The framework tests can be found in the [xunit/test_xunit.py](xunit/test_xunit.py) file. To run the tests, just run the following command:

```bash
python xunit/test_xunit.py
```

There are also an example of how to use the framework in the [main.py](main.py) file. To run the example, just run the following command:

```bash
python main.py
```
