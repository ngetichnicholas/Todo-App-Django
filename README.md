# To-Do  Django API
## Author
Nicholas Ngetich
*****
### Description
This is a Django backend for To do list web application .
*****
### Prerequisites
* Text editor eg Visual Studio Code
* You need to have git installed. You can install it with the following command in your terminal
`$ sudo apt install git-all`
*****
## Cloning the application
To access this project on your local files, you can clone it using these steps
1. Open your terminal
1. Use this command to clone:
```sh
$ git clone https://github.com/ngetichnicholas/Todo-App-Django.git
```
This will clone the repositoty into your local folder
*****
## Running the cloned App
The first thing to do is to change directory to project folder:
```sh
$ cd Todo-App-Django
```
Open the app with any code editor of your choice to setup environment variables:

To open with VS Code, just run command `$ code .`

### Environment Variables
Create `.env` file and add the following variables and update accordingly
```python
SECRET_KEY='Your-Secret-key'
DEBUG=True
DB_NAME='database-name'
DB_USER='system-user-name'
DB_PASSWORD='database-password'
DB_HOST='127.0.0.1'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

### Virtual Environment
Create a virtual environment to install dependencies and activate it:

```sh
$ python3 -m venv virtual
$ source virtual/bin/activate
```

Then install the dependencies:

```sh
(virtual)$ pip install -r requirements.txt
```
Note the `(virtual)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(virtual)$ python3 manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.
*****
## Dependencies
* Pillow
* psycopg2
* python-decouple
* whitenoise
* gunicorn
*****
## Technologies Used
* Python 3

*****
### License
This project is under:  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE)
*****
### Questions?
Twitter: **[@ngetichnichoh](https://twitter.com/ngetichnichoh)**  
Email: **[ngetichnicholas903@gmail.com](mailto:ngetichnicholas903@gmail.com)**
