# serverless-pymysql-rds-test

A simple script to test RDS connectivity from a lambda function using [Serverless](https://github.com/serverless/serverless).
This script will deploy the following elements into your AWS account:
* private VPC
* private subnets
* t2.micro RDS instance
* lambda function

## Prerequisites

* serverless framework
* serverless-python-requirements plugin
* python 2.7
* PyMySQL lybrary

## Installing dependencies

Check out a clone of this repo to a location of your choice, such as `git clone --depth=1 https://github.com/matteomorelli/serverless-pymysql-rds-test.git`

Go inside your working directory location and install serverless plugin:
```
$ npm install --save-dev serverless-python-requirements
```

cd to the directory where requirements.txt is located, activate your virtual environment and install python requirements, or simply install python requirements:
```
$ pip install -r requirements.txt
```

Deploy your serverless stack:
```
$ sls deploy
```

Once the deploy is complete, run `sls info` to get the endpoint:
```
$ sls info
Service Information
<snip>
endpoints:
  GET - https://abc6defghi.execute-api.us-east-1.amazonaws.com/dev <-- Endpoint
  GET - https://abc6defghi.execute-api.us-east-1.amazonaws.com/dev/query
```

Copy paste into your browser, and your good!

To remove the stack from you AWS account remember to type in the terminal:
```
$ sls remove
```

## Deployment

See installing instruction
If you want to test a slightly complex query you can import into RDS database the included sql file and execute the second serverless function:
```
$ sls info
Service Information
<snip>
endpoints:
  GET - https://abc6defghi.execute-api.us-east-1.amazonaws.com/dev
  GET - https://abc6defghi.execute-api.us-east-1.amazonaws.com/dev/query <-- Endpoint
```

## Authors

* **Matteo Morelli** - *Initial work* - [matteomorelli](https://github.com/matteomorelli)

## License

This project is licensed under the GNU Affero General Public License v3.0 or later - see the [LICENSE](LICENSE) file for details
