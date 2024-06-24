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