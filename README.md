<h1 align="center">Python + Flask + Sqlite</h1> 

![logos](https://github.com/tsotneforester/python-flask-sqlite3-CRUD/assets/79293287/506d2c72-65dc-4e66-a266-a075b88f0214)


<h3 align="center">Setup Guide</h3> 

## About

[CS50](https://pll.harvard.edu/course/cs50-introduction-computer-science]) flourished new trinity of web development for me: Python + Flask + Sqlite. Despite cloud coding with CS50 libraries was piece of cake, setting up local working environment could have been more comfortable for final project.
My initial desire was to create simple setup guide, but as you might have already guessed, it turned out to be setup + simple app, just to showcase general POST and GET request handling with SQL query executing.


## Environment setup + usage
- **_Python_** - Install it directly from Microsoft [Store](https://apps.microsoft.com/detail/9PJPW5LDXLZ5?hl=en-US&gl=US). Check installation status

```sh
python --version
``` 

- **_Flask_** - `pip` is a package manager for Python packages, or modules. Flask is one of them. To install it, run command:

```sh
pip install Flask
``` 

check status:

```sh
pip show flask
``` 

- **_Sqlite_** - Another simple step, but not classical one though, not installing `.exe` file, nor with `pip`. Here is [link](https://www.youtube.com/results?search_query=sqlite+installation+windows+10) how to do it.

As everything is installed correctly, you can run app with:

```sh
python app.py
``` 

## Environment description
We all know how backend works: with `GET` and `POST` requests (and not only) front communicates to server, which responds with some actual data. `flask` lives within `Python`, it is casebook of routs request methods and data gathering/sending instructions, which is stored in SQL database (database.db). `flask` works like real server: it gets request from html `form`, executes proper SQL query, gets data from database and displays it in HTML via `jinja2`. `sqlite` is just one lightweight library which works according to SQL principles

you will find `log.sql` file in project. it helps to execute SQL queries and test them while implementing it in flask. you can simultaneously launch second terminal and execute queries written in `log.sql`.

```sh
cat log.sql | sqlite3 database.db
``` 


## Acknowledgments
 I've included a few of helpful resources!
 
 -  [Sqlite.org](https://www.sqlite.org/doclist.html)
 -  [Flask](https://flask.palletsprojects.com/en/3.0.x/#user-s-guide)
 -  [W3schools](https://www.w3schools.com/sql/default.asp)


