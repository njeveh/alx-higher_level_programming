# 0x0F. Python - Object-relational mapping

# Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

# Resources
## Read or watch:

 - Object-relational mappers
 - mysqlclient/MySQLdb documentation (please don’t pay attention to _mysql)
 - MySQLdb tutorial
 - SQLAlchemy tutorial
 - SQLAlchemy
 - mysqlclient/MySQLdb
 - Introduction to SQLAlchemy
 - Flask SQLAlchemy
 - 10 common stumbling blocks for SQLAlchemy newbies
 - Python SQLAlchemy Cheatsheet
 - SQLAlchemy ORM Tutorial for Python Developers (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
 - SQLAlchemy Tutorial

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
 - Why Python programming is awesome
 - How to connect to a MySQL database from a Python script
 - How to `SELECT` rows in a MySQL table from a Python script
 - How to `INSERT` rows in a MySQL table from a Python script
 - What ORM means
 - How to map a Python Class to a MySQL table

# Requirements
## General
 - Allowed editors: `vi`, `vim`, `emacs`
 - All your files will be interpreted/compiled on `Ubuntu 20.04 LTS` using `python3` (`version 3.8.5`)
 - Your files will be executed with `MySQLdb` `version 2.0.x`
 - Your files will be executed with `SQLAlchemy` `version 1.4.x`
 - All your files should end with a new line
 - The first line of all your files should be exactly `#!/usr/bin/python3`
 - A `README.md` file, at the root of the folder of the project, is mandatory
 - Your code should use the `pycodestyle` (`version 2.8.*`)
 - All your files must be executable
 - The length of your files will be tested using `wc`
 - All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
 - All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
 - All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
 - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
 - You are not allowed to use execute with `sqlalchemy`
 
 
## Table of contents
Files | Description
----- | -----------
[0-select_states.py](./0-select_states.py) | Python script that lists all states from the database hbtn_0e_0_usa
[1-filter_states.py](./1-filter_states.py) | Python script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
[2-my_filter_states.py](./2-my_filter_states.py) | Python script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument
[3-my_safe_filter_states.py](./3-my_safe_filter_states.py) | Python script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument safe from SQL injections
[4-cities_by_state.py](./4-cities_by_state.py) | Python script that lists all cities from the database hbtn_0e_4_usa
[5-filter_cities.py](./5-filter_cities.py) | Python script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
[model_state.py](./model_state.py) | python file that contains the class definition of a State and an instance Base = declarative_base()
[7-model_state_fetch_all.py](./7-model_state_fetch_all.py) | Python script that lists all State objects from the database hbtn_0e_6_usa
[8-model_state_fetch_first.py](./8-model_state_fetch_first.py) | Python script that prints the first State object from the database hbtn_0e_6_usa
[9-model_state_filter_a.py](./9-model_state_filter_a.py) | Python script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
[10-model_state_my_get.py](./10-model_state_my_get.py) | Python script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa
[11-model_state_insert.py](./11-model_state_insert.py) | Python script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
[12-model_state_update_id_2.py](./12-model_state_update_id_2.py) | Python script that changes the name of a State object from the database hbtn_0e_6_usa
[13-model_state_delete_a.py](./13-model_state_delete_a.py) | Python script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
[model_city.py](./model_city.py) | Python file that contains the class definition of a City
[14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py) | Python script that prints all City objects from the database hbtn_0e_14_usa
