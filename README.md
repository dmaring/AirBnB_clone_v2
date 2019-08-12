<p align="center">
  <img src="https://i.imgur.com/ogbfW3k.png">
</p>

# AirBnB_clone
* This repository contains a full-stack clone of AirBnB divided into 6 parts:

| Component 	| Description 	|
|:--------------------------:	|:------------------------------------------------------------:	|
| [Console](https://github.com/tuvo1106/AirBnB_clone) 	| Data model management via command interpreter 	|
| [Web static](https://github.com/tuvo1106/AirBnB_clone/tree/master/web_static) | HTML/CSS/Templates 	|
| [MySQL storage](https://github.com/tuvo1106/AirBnB_clone_v2) | Importing local file storage to database |
| Web framework - templating 	| Web server deployment in Python 	|
| RESTful API 	| JSON web interface to display all objects 	|
| Web dynamic 	| Loading of objects from client side using Jquery/RESTful API 	|
---
Example of final product:
<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png">
</p>

## Techstack

<p align="center">
  <img src="https://i.imgur.com/lgZnZrz.png">
</p>

## Usage
* All files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 and Python3 (version 3.4.3)
* All Python code use the PEP 8 style (version 1.7.*)

## Testing

* All unittests can be executed with:

```
python3 -m unittest discover tests
```

## Tasks

### [ 0. Fork me if you can! ](./)
* For this project you will fork this codebase:
  * update the repository name to AirBnB_clone_v2
  * update the README.md with your information but don’t delete the initial authors

### [ 1. Bug free! ]
* All your unittests must pass without any errors at anytime in this project, with each storage engine!. Same for PEP8!

```sh
guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
```

### [ 2. Console improvements ](./console.py)
* Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters:
  * Command syntax: create <Class name> <param 1> <param 2> <param 3>...
  * Param syntax: <key name>=<value>
  * Value syntax:
    * String: "<value>" => starts with a double quote
      * any double quote inside the value must be escaped with a backslash \
      * all underscores _ must be replace by spaces . Example: You want to set the string My little house to the attribute name, your command line must be name="My_little_house"
    * Float: <unit>.<decimal> => contains a dot .
    * Integer: <number> => default case
  * If any parameter doesn’t fit with these requirements or can’t be recognized correctly by your program, it must be skipped

```sh
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create
create State name="California"
create State name="Arizona"
all State

create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297
all Place
guillaume@ubuntu:~/AirBnB_v2$ cat test_params_create | ./console.py 
(hbnb) d80e0344-63eb-434a-b1e0-07783522124e
(hbnb) 092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7
(hbnb) [[State] (d80e0344-63eb-434a-b1e0-07783522124e) {'id': 'd80e0344-63eb-434a-b1e0-07783522124e', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), 'name': 'California'}, [State] (092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7) {'id': '092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7', 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842779), 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842792), 'name': 'Arizona'}]
(hbnb) (hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124
(hbnb) [[Place] (76b65327-9e94-4632-b688-aaa22ab8a124) {'number_bathrooms': 2, 'longitude': -122.431297, 'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, 'price_by_night': 300, 'name': 'My little house', 'id': '76b65327-9e94-4632-b688-aaa22ab8a124', 'max_guest': 10, 'number_rooms': 4, 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843774), 'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843747)}]
(hbnb)
```

### [ 3. MySQL setup development ](./setup_mysql_dev.sql)
* Write a script that prepares a MySQL server for the project:
  * A database hbnb_dev_db
  * A new user hbnb_dev (in localhost)
  * The password of hbnb_dev should be set to hbnb_dev_pwd
  * hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
  * hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
  * If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

```sh
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db
Enter password: 
hbnb_dev_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
Enter password:
```
```sql
Grants for hbnb_dev@localhost
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost'
```

### [ 4. MySQL setup test ](./setup_mysql_test.sql)
* Write a script that prepares a MySQL server for the project:
  * A database hbnb_test_db
  * A new user hbnb_test (in localhost)
  * The password of hbnb_test should be set to hbnb_test_pwd
  * hbnb_test should have all privileges on the database hbnb_test_db (and only this database)
  * hbnb_test should have SELECT privilege on the database performance_schema (and only this database)
  * If the database hbnb_test_db or the user hbnb_test already exists, your script should not fail

```sh
guillaume@ubuntu:~/AirBnB_v2$ cat setup_mysql_test.sql | mysql -hlocalhost -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
Enter password: 
hbnb_test_db
guillaume@ubuntu:~/AirBnB_v2$ echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p
Enter password:
```
```sql
Grants for hbnb_test@localhost
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost'
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost'
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost'
```

### [ 5. Delete object ](./models/engine/file_storage.py)
* Update FileStorage: (models/engine/file_storage.py)
  * Add a new public instance method: def delete(self, obj=None): to delete obj from \_\_objects if it’s inside
  * Update the prototype of def all(self) to def all(self, cls=None) - that returns the list of objects of one type of class. Example below with State - it’s an optional filtering
  
```sh
guillaume@ubuntu:~/AirBnB_v2$ cat main_delete.py
```
```python
#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.state import State

fs = FileStorage()

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Create a new State
new_state = State()
new_state.name = "California"
fs.new(new_state)
fs.save()
print("New State: {}".format(new_state))

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])

# Delete the new State
fs.delete(new_state)

# All States
all_states = fs.all(State)
print("All States: {}".format(len(all_states.keys())))
for state_key in all_states.keys():
    print(all_states[state_key])
```
```sh
guillaume@ubuntu:~/AirBnB_v2$ ./main_delete.py
All States: 0
New State: [State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
All States: 1
[State] (b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce) {'name': 'California', 'created_at': datetime.datetime(2017, 11, 10, 1, 13, 32, 561137), 'id': 'b0026fc6-116f-4d1a-a9cb-6bb9b299f1ce'}
All States: 0
```

### [ DBStorage - States and Cities ](./models/engine/file_storage.py)

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg">
</p>

## Authors
* [__Tu Vo__](https://github.com/tuvo1106)
* [__Kevin Yook__](https://github.com/yook00627)
