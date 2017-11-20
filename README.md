[![CircleCI](https://circleci.com/gh/coastrider/bench-test/tree/master.svg?style=svg)](https://circleci.com/gh/coastrider/bench-test/tree/master)
# Bench RestTest take-home test 

The following repo contains my solution to the Bench Rest Test take-home test using Python 3

Here is a high level overview of the project: 
  - Python 3 has a number of libraries and packages that can be used to interact with HTTP resources. I decided that the best choice is [Requests](http://docs.python-requests.org/en/master/user/quickstart/) for it's simplicity and built-in methods to handle JSON responses. 

  - Using requests, the app retrieves the site's JSON content programatically and processes the response using two processor functions. 

  - All my scripts have been checked with [Pylint](https://www.pylint.org/) and I created a test suite using [Pytest](https://docs.pytest.org/en/latest/) which is is a no-boilerplate alternative to Python’s standard unittest module.

## Usage
#### How to run
```bash
pip3 install -r requirements.txt
python3 run.py
```
#### Configuration 
In order to decouple configuration from code, the file **sites.conf** contains target host information. In case there are any changes to the API endpoint such as URL content or structure, this file will need to be modified.

The app will request paths numerically using a loop until a *404 - Not Found* HTTP response is returned

## Testing the app
#### Unit Testing
```bash
pytest -v test_suite.py
```
Which should outoput something like the following:
```
============================================================================== test session starts ===============================================================================
platform linux -- Python 3.6.2, pytest-3.2.5, py-1.5.2, pluggy-0.4.0 -- /usr/bin/python3.6
cachedir: .cache
collected 5 items

test_suite.py::test_http_200 PASSED
test_suite.py::test_http_404 PASSED
test_suite.py::test_http_exception PASSED
test_suite.py::test_balance_processor PASSED
test_suite.py::test_total_balance PASSED
```
#### Automated Testing
CircleCI is used for automated testing and triggers a build when a new commit is pushed to the master branch. Currently, it's only configured to run the test_suite.py Unit Tests:

https://circleci.com/gh/coastrider/bench-test

## Other considerations

