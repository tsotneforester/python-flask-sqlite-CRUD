<h1 align="center">Python + Flask + Sqlite</h1> 
<h2 align="center">Setup Guide</h2> 


![logos](https://github.com/tsotneforester/python-flask-sqlite3-CRUD/assets/79293287/3d874e5a-52d0-4ed9-b5a8-6880e29f625a)



## About

CS50 flourished new trinity of web development for me: Python + Flask + Sqlite. Despite cloud coding with cs50 libraries was piece of cake, setting up local working evnironment could have been more comfortable for final project.  
my initial desire was to create simple setup guide, but As you might have already guessed, it turned out to be setup + simple app, just to showcase genaral POST and GET requst handling with sqlite query executing


## Environment setup + usage
- **_Python_** - install it directly form microsoft store. after instalation, you can check the status with

```sh
python --version
``` 

- **_Flask_** - PIP is a package manager for Python packages, or modules if you like. flask is one of them. to instal it, run command

```sh
pip install Flask
``` 

check the status with

```sh
pip show flask
``` 

- **_Sqlite_** - another simple step, but not classical one though, not installing `.exe` file, nor with `pip`. here is [link](https://www.youtube.com/results?search_query=sqlite+installation+windows+10)

as everything is installed correctly, you can run app with simple command

```sh
python app.py
``` 

## Environment description
we all know how backend works: with GET and POST requests (and not only) front communicates to server, which responds with some actual data. `flask` lives within `Python`, it is casebook of routs request methods and data gathering/sending instructions, which is stored in sqlite database (database.db). flask works like real server: it gets request from html `form`, executes proper sql query, gets data from database and displays it in HTML via `jinja2`

you will find `log.sql` file in project. it helps to execute sql queries and test them while implementing it in flask. you can simultaneously launch second terminal and execute queries written in `log.sql`.

```sh
cat log.sql | sqlite3 database.db
``` 


## Acknowledgments
 I've included a few of helpful resources!
 
 -  [Sqlite.org](https://www.sqlite.org/doclist.html)
 -  [Flask](https://flask.palletsprojects.com/en/3.0.x/#user-s-guide)
 -  [w3scholls](https://www.w3schools.com/sql/default.asp)




<!-- |||||||||||||| Heading |||||||||||||    -->
<!-- # About The Project -->
<!--<h1 align="center"> About The Project </h1> -->

<!-- |||||||||||||| Emphesize --|||||||||||||| -->
<!-- **bold** / **bold** / <strong>bold</strong> -->
<!-- _italic_ / _italic_ / <i>italic</i> -->
<!-- **_italic + Bold_** -->

<!----------------------------------- HR-------------------------------->

<!-- *** / <hr> / --- -->

<!----------------------------------- List-------------------------------->
<!-- - item -->
<!-- - item -->

<!-- 1. item 1 -->
<!-- 2. item 2 -->

<!----------------------------------- Link -------------------------------->
<!-- [hi](link) -->
<!-- <https://www.markdownguide.org> -->
<!-- <fake@example.com> -->

<!----------------------- image and badge-------------------------------->
<!-- <p align="center"><img src=""></p> -->
<!-- ![txt](src "title") -->
<!-- [![txt](src "title")](link) -->
<!-- ![txt](https://img.shields.io/badge/Nvidia-RTX%204090-D212E1?style=for-the-badge&logo=nvidia&logoColor=white&labelColor=76B900 "image") -->
<!-- ![html](https://img.shields.io/badge/-HTML-6abecd "image") -->

<!----------------------- Blockquote -------------------------------->
<!-- > blockquote -->

<!----------------------- code -------------------------------->
<!-- > `code` -->

<!----------------------- Terminal -------------------------------->
<!-- ```sh
const hello= "hello";
``` -->

<!----------------------- Table-------------------------------->
<!-- | name | surname | age |
| :--- | :-----: | --: |
| 4    |    5    |   6 | -->
<!----------------------- Back To Top -------------------------------->
<!-- <a name="readme-top"></a>
<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!----------------------- Links -------------------------------->
<!-- https://readme-typing-svg.demolab.com/demo/ -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md -->
<!-- https://github.com/tandpfun/skill-icons?ref=reactjsexample.com -->
<!-- https://shields.io/ -->
<!-- https://readme-typing-svg.demolab.com/demo/ -->
<!-- https://reheader.glitch.me/home -->
<!-- https://github-profile-summary-cards.vercel.app/demo.html -->
<!-- https://www.terminalgif.com/ -->
<!-- https://home.aveek.io/GitHub-Profile-Badges/ -->
<!-- https://github.com/MikeCodesDotNET/ColoredBadges -->

<!----------------------- Preview -------------------------------->
<!-- https://markdownlivepreview.com/ -->
