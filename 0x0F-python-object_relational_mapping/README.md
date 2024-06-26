## 0x0F-python-object_relational_mapping
### 0-select_states.py
> A script that lists all states from a database hbtn_0e_0_usa:
>> - Takes 3 arguments: mysql username, mysql password and database name (no argument validation needed)
>> - Uses the module MySQLdb (import MySQLdb)
>> - Connects to a MySQL server running on localhost at port 3306
>> - Results are sorted in ascending order by states.id
### 1-filter_states.py
> A script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
>> - Takes 3 arguments: mysql username, mysql password and database name (no argument validation needed)
>> - Uses the module MySQLdb (import MySQLdb)
>> - Connects to a MySQL server running on localhost at port 3306
>> - Results are sorted in ascending order by states.ids
### 2-my_filter_states.py
> A script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
>> - takes 4 arguments: mysql username, mysql password, database name and state name searched.
>> - Uses the module MySQLdb (import MySQLdb)
>> - Connects to a MySQL server running on localhost at port 3306
>> - uses format to create the SQL query with the user input
>> - Results are sorted in ascending order by states.ids
### 3-my_safe_filter_states.py
> An SQL injection safe script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
>> - takes 4 arguments: mysql username, mysql password, database name and state name searched.
>> - Uses the module MySQLdb (import MySQLdb)
>> - Connects to a MySQL server running on localhost at port 3306
>> - uses format to create the SQL query with the user input
>> - Results are sorted in ascending order by states.ids
### 4-cities_by_state.py
> A script that lists all cities from the database hbtn_0e_4_usa
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module MySQLdb (import MySQLdb)
>> - Connects to a MySQL server running on localhost at port 3306
>> - uses format to create the SQL query with the user input
>> - Results are sorted in ascending order by cities.id
### 5-filter_cities.py
> A script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
>> - Takes 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
>> - Uses the module MySQLdb (import MySQLdb)
>> - Connects to a MySQL server running on localhost at port 3306
>> - uses format to create the SQL query with the user input
>> - Results are sorted in ascending order by cities.id
### model_state.py
> A python file that contains the class definition of a State and an instance Base = declarative_base():
>> - State class:
>>> - inherits from Base Tips
>>> - links to the MySQL table states
>>> - Has class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
>>> - Has class attribute name that represents a column of a string with maximum 128 characters and can’t be null
>> - Uses the module SQLAlchemy
>> - Connects to a MySQL server running on localhost at port 3306
### 7-model_state_fetch_all.py
> A script that lists all State objects from the database hbtn_0e_6_usa
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
>> - Results are sorted in ascending order by states.id
### 8-model_state_fetch_first.py
> A script that prints the first State object from the database hbtn_0e_6_usa.
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
>> - State displayed is the first in states.id
>> - If the table states is empty, Nothing is printed followed by a new line
### 9-model_state_filter_a.py
> A script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
>> - Results are sorted in ascending order by states.id
### 10-model_state_my_get.py
> A script that prints the State object with the name passed as argument from the database hbtn_0e_6_usa.
>> - Takes 4 arguments: mysql username, mysql password, database name and state name to search (SQL injection free)
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
>> - Assumes you have one record with the state name to search
>> - Results displays the states.id
>> - If no state has the name you searched for, Not found is displayed
### 11-model_state_insert.py
> A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
>> - Prints the new states.id after creation
### 12-model_state_update_id_2.py
> A script that changes the name of a State object from the database hbtn_0e_6_usa
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
>> - Changes the name of the State where id = 2 to New Mexico
### 13-model_state_delete_a.py
> A script that deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa.
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
### model_city.py
> A python file that contains the class definition of a City and an instance Base = declarative_base():
>> - City class:
>>> - links to the MySQL table cities
>>> - inherits from Base (imported from model_state)
>>> - Has class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
>>> - Has class attribute name that represents a column of a string with maximum 128 characters and can’t be null
>>> - Has class attribute state_id that represents a column of an integer, can’t be null and is a foreign key to states.id
>> - Uses the module SQLAlchemy
>> - Connects to a MySQL server running on localhost at port 3306
### 14-model_city_fetch_by_state.py
> A script that prints all City objects from the database hbtn_0e_14_usa.
>> - Takes 3 arguments: mysql username, mysql password and database name
>> - Uses the module SQLAlchemy
>> - Imports State and Base from model_state - from model_state import Base, State
>> - Connects to a MySQL server running on localhost at port 3306
>> - Results are sorted in ascending order by cities.id
### 100-relationship_states_cities.py
### relationship_state.py
### relationship_state.py