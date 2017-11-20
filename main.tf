provider "aws" {
  region = "us-west-2"
  profile = "default"
}

resource "aws_iam_role" "iam_for_lambda" {
  name = "iam_for_lambda"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_instance" "alberto-test-amazonlinux" {
  ami = "ami-32d8124a"
  instance_type = "t2.micro"
  tags {
    Name = "alberto-test-amazonlinux"
  }
}

resource "aws_lambda_function" "benchtest-lambda" {
  filename         = "lambda_deploy.zip"
  function_name    = "benchtest-lambda"
  role             = "${aws_iam_role.iam_for_lambda.arn}"
  handler          = "main.lambda_handler"
  source_code_hash = "${base64sha256(file("lambda_deploy.zip"))}"
  runtime          = "python3.6"
}
