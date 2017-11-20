https://circleci.com/gh/coastrider/bench-test.png?circle-token=:circle-token 
# Bench restTest π 

The following repo contains my solution to the Bench Labs Rest Test take-home using Python 3

Here is a high level overview of the project: 
  - Python 3 has a number of libraries and packages that can be used to interact with HTTP resources. I decided that the best choice is [Requests](http://docs.python-requests.org/en/master/user/quickstart/) for it's simplicity and built-in methods to handle JSON responses. 

  - Using requests, the app retrieves the site's JSON content programmatically and processes the response using two processor functions. 

  - All the Python scripts have been checked with [Pylint](https://www.pylint.org/) and I created a test suite using [Pytest](https://docs.pytest.org/en/latest/) which is is a no-boilerplate alternative to Python’s standard unittest module.

## Usage
#### How to run locally
```bash
pip3 install -r requirements.txt
python3 run.py
```
#### How to run with Docker
The following `docker build` command needs to be run from the same directory than the **Dockerfile** present in this repository.
```bash
docker build . -t bench-test-docker-image
docker run --rm --name bench-test bench-test-docker-image 
```
The Docker run command should output the Daily Balances and Total Balance then automatically remove itself due to the *--rm* option


#### Configuration 
In order to decouple configuration from code, the file **sites.conf** contains target host information. In case there are any changes to the API endpoint such as URL content or structure, this file will need to be modified.

The app will request paths numerically using a loop until a *404 - Not Found* HTTP response is returned

## Testing the app
#### Unit Testing
```bash
pytest -v test_suite.py
```
Which should output something like the following:
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

## Deploying to AWS
I wanted to deploy the app on AWS as it's relevant to the position I'm applying for. I initially tried Elastic Beanstalk using the single Docker container configuration but decided it wasn't the best option due to the ephemeral nature of the app. Eventually, I decided to use Teraform to provision a Lambda function with the application code. Lambda is the perfect fit for this app as we can just execute it in response to an event such as a manual trigger, cron schedule or HTTP GET and not require any server or container to run continuously. 

The following Terraform commands will provision the Lambda function as defined in the file **main.tf**

```bash
terraform init
terraform plan
terraform apply
```
Then just trigger the Lambda function using a manual test trigger event or any other valid event trigger. The app should run in a few ms run and the output should look like this: 


The drawback of this setup is that I had to package and refactor the entire application code, including dependencies in the **lambda_deploy.zip** file as currently Lambda doesn't allow to deploy using version control. If the app is updated, a new source code .zip bundle will need to be generated each time and provided to Terraform. 

## Other considerations
- The app could be further improved by making the package *benchtest/core.py* more modular, for example, create different modules for query site, balance_processor etc. That will allow a more decoupled architecture and the services to be used independently as the app grows. 
- URL parsing and handling could be further improved. Currently it's very tailored to the URL structure of the restTest API which doesn't follow JSON API guidelines as described [here](http://jsonapi.org/recommendations/). 
- Current deployment flow is very limited, and taking aside the CircleCI hook it lacks automation. Ideally, CircleCI should release the app to an staging environment in AWS to run further tests and then deploy to production.

