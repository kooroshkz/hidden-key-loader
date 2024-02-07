# Hidden Credentials Loader
A streamlined tool for managing sensitive information in open-source Python projects. It facilitates secure development by loading credentials dynamically, eliminating the need to hardcode confidential details such as passwords or API keys.

## How to setup
1- Clone the repository into your preferred directory.
2- Prevent dev_credentials.txt from being tracked by version controllers.

Example for git on teminal:
```
touch .gitignore && echo "dev_credentials.txt" >> .gitignore
```
3- Integrate the script to use variables from dev_credentials.txt in your code:
```
from credentials import *
```
Refer to YOUR_PROJECT_SAMPLE.py for usage examples.

## What to expect?
This tool allows seamless access to variables in dev_credentials.txt, enabling secure and localized management of credentials in your Python projects.