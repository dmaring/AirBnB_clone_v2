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

### [ 0. Fork me if you can! ](https://github.com/yook00627/AirBnb_clone)
* For this project you will fork this codebase:
  * update the repository name to AirBnB_clone_v2
  * update the README.md with your information but don’t delete the initial authors

### [ 1. Bug free! ](./tests/)
* All your unittests must pass without any errors at anytime in this project, with each storage engine!. Same for PEP8!

```sh
guillaume@ubuntu:~/AirBnB_v2$ python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
guillaume@ubuntu:~/AirBnB_v2$ HBNB_ENV=test HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1
OK
```

### [ 2. Console improvements ](./console.py)
* Update the def do_create(self, arg): function of your command interpreter (console.py) to allow for object creation with given parameters:
  * Command syntax: create \<Class name> \<param 1> \<param 2> \<param 3>...
  * Param syntax: \<key name>=\<value>
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

### [ 6. DBStorage - States and Cities ](./models/engine/file_storage.py)

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg">
</p>

* In the following steps, you will make multiple changes:
  * the biggest one is the transition between FileStorage and DBStorage: In the industry, you will never find a system who can work with both in the same time - but you will find a lot of services who can manage multiple storage systems. (for example, logs service: in memory, in disk, in database, in ElasticSearch etc…) - The main concept behind is the abstraction: Make your code running without knowing how it’s stored.
  * add attributes for SQLAlchemy: they will be class attributes, like previously, with a “weird” value. Don’t worry, these values are for description and mapping to the database. If you change one of these values, or add/remove one attribute of the a model, you will have to delete the database and recreate it in SQL. (Yes it’s not optimal, but for development purposes, it’s ok. In production, we will add “migration mechanism” - for the moment, don’t spend time on it.)

* Update BaseModel: (models/base_model.py)
  * Create Base = declarative_base() before the class definition of BaseModel
  * Note! BaseModel does /not/ inherit from Base. All other classes will inherit from BaseModel to get common values (id, created_at, updated_at), where inheriting from Base will actually cause SQLAlchemy to attempt to map it to a table.
  * Add or replace in the class BaseModel:
    * class attribute id
      * represents a column containing a unique string (60 characters)
      * can’t be null
      * primary key
    * class attribute created_at
    * represents a column containing a datetime
      * can’t be null
      * default value is the current datetime (use datetime.utcnow())
    * class attribute updated_at
      * represents a column containing a datetime
      * can’t be null
      * default value is the current datetime (use datetime.utcnow())
  * Move the models.storage.new(self) from def \_\_init_\_(self, \*args, \*\*kwargs): to def save(self): and call it just before models.storage.save()
  * In def \_\_init\_\_(self, \*args, \*\*kwargs):, manage kwargs to create instance attribute from this dictionary. Ex: kwargs={ 'name': "California" } => self.name = "California" if it’s not already the case
  * Update the to_dict() method of the class BaseModel:
remove the key \_sa\_instance_state from the dictionary returned by this method only if this key exists
  * Add a new public instance method: def delete(self): to delete the current instance from the storage (models.storage) by calling the method delete

* Update City: (models/city.py)
  * City inherits from BaseModel and Base (respect the order)
  * Add or replace in the class City:
    * class attribute \_\_tablename\_\_ -
      * represents the table name, cities
    * class attribute name
      * represents a column containing a string (128 characters)
      * can’t be null
    * class attribute state_id
      * represents a column containing a string (60 characters)
      * can’t be null
      * is a foreign key to states.id

* Update State: (models/state.py)
  * State inherits from BaseModel and Base (respect the order)
  * Add or replace in the class State:
    * class attribute \_\_tablename\_\_
    * represents the table name, states
    * class attribute name
    * represents a column containing a string (128 characters)
    * can’t be null
    * for DBStorage: class attribute cities must represent a relationship with the class City. If the State object is deleted, all linked City objects must be automatically deleted. Also, the reference from a City object to his State should be named state
    * for FileStorage: getter attribute cities that returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City

* New engine DBStorage: (models/engine/db_storage.py)
  * Private class attributes:
    * \_\_engine: set to None
    * \_\_session: set to None
  * Public instance methods:
    * \_\_init\_\_(self):
      * create the engine (self.\_\_engine)
      * the engine must be linked to the MySQL database and user created before (hbnb_dev and hbnb_dev_db):
        * dialect: mysql
        * driver: mysqldb
      * all of the following values must be retrieved via environment variables:
        * MySQL user: HBNB_MYSQL_USER
        * MySQL password: HBNB_MYSQL_PWD
        * MySQL host: HBNB_MYSQL_HOST (here = localhost)
        * MySQL database: HBNB_MYSQL_DB
      * don’t forget the option pool_pre_ping=True when you call create_engine
      * drop all tables if the environment variable HBNB_ENV is equal to test
    * all(self, cls=None):
      * query on the current database session (self \_\_session) all objects depending of the class name (argument cls)
      * if cls=None, query all types of objects (User, State, City, Amenity, Place and Review)
      * this method must return a dictionary: (like FileStorage)
        * key = <class-name>.<object-id>
        * value = object
    * new(self, obj): add the object to the current database session (self.__session)
    * save(self): commit all changes of the current database session (self.__session)
    * delete(self, obj=None): delete from the current database session obj if not None
    * reload(self):
      * create all tables in the database (feature of SQLAlchemy) (WARNING: all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine))
      * create the current database session (self.__session) from the engine (self.__engine) by using a sessionmaker - the option expire_on_commit must be set to False ; and scoped_session - to make sure your Session is thread-safe
  
* Update \_\_init__.py: (models/\_\_init\_\_.py)
  * Add a conditional depending of the value of the environment variable HBNB_TYPE_STORAGE:
    * If equal to db:
      * Import DBStorage class in this file
      * Create an instance of DBStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
    * Else:
      * Import FileStorage class in this file
      * Create an instance of FileStorage and store it in the variable storage (the line storage.reload() should be executed after this instantiation)
  * This “switch” will allow you to change storage type directly by using an environment variable (example below)

State creation:
```sh
guillaume@ubuntu:~/AirBnB_v2$ echo 'create State name="California"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 95a5abab-aa65-4861-9bc6-1da4a36069aa
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all State' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[State] (95a5abab-aa65-4861-9bc6-1da4a36069aa) {'name': 'California', 'id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'updated_at': datetime.datetime(2017, 11, 10, 0, 49, 54), 'created_at': datetime.datetime(2017, 11, 10, 0, 49, 54)}]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM states\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
created_at: 2017-11-10 00:49:54
updated_at: 2017-11-10 00:49:54
      name: California
```

City creation:
```sh
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Francisco"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) 4b457e66-c7c8-4f63-910f-fd91c3b7140b
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all City' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[City] (4b457e66-c7c8-4f63-910f-fd91c3b7140b) {'id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'updated_at': datetime.datetime(2017, 11, 10, 0, 52, 53), 'state_id': '95a5abab-aa65-4861-9bc6-1da4a36069aa', 'name': 'San Francisco', 'created_at': datetime.datetime(2017, 11, 10, 0, 52, 53)]
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ echo 'create City state_id="95a5abab-aa65-4861-9bc6-1da4a36069aa" name="San_Jose"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
(hbnb) a7db3cdc-30e0-4d80-ad8c-679fe45343ba
(hbnb)
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM cities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
created_at: 2017-11-10 00:52:53
updated_at: 2017-11-10 00:52:53
      name: San Francisco
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
*************************** 2. row ***************************
        id: a7db3cdc-30e0-4d80-ad8c-679fe45343ba
created_at: 2017-11-10 00:53:19
updated_at: 2017-11-10 00:53:19
      name: San Jose
  state_id: 95a5abab-aa65-4861-9bc6-1da4a36069aa
```

### [ 7. DBStorage - User ](./models/user.py)
* Update User: (models/user.py)
  * User inherits from BaseModel and Base (respect the order)
  * Add or replace in the class User:
    * class attribute \_\_tablename\_\_
      * represents the table name, users
    * class attribute email
      * represents a column containing a string (128 characters)
      * can’t be null
    * class attribute password
      * represents a column containing a string (128 characters)
      * can’t be null
    * class attribute first_name
      * represents a column containing a string (128 characters)
      * can be null
    * class attribute last_name
      * represents a column containing a string (128 characters)
      * can be null

```sh
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="gui@hbtn.io" password="guipwd" first_name="Guillaume" last_name="Snow"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'all User' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[User] (4f3f4b42-a4c3-4c20-a492-efff10d00c0b) {'updated_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'last_name': 'Snow', 'first_name': 'Guillaume', 'email': 'gui@hbtn.io', 'created_at': datetime.datetime(2017, 11, 10, 1, 17, 26), 'password': 'f4ce007d8e84e0910fbdd7a06fa1692d'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM users\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
created_at: 2017-11-10 01:17:26
updated_at: 2017-11-10 01:17:26
     email: gui@hbtn.io
  password: guipwd
first_name: Guillaume
 last_name: Snow
```

### [ 8. DBStorage - Place ](./models/place.py)
* Update Place: (models/place.py)
  * Place inherits from BaseModel and Base (respect the order)
  * Add or replace in the class Place:
    * class attribute \_\_tablename\_\_
      * represents the table name, places
    * class attribute city_id
      * represents a column containing a string (60 characters)
      * can’t be null
      * is a foreign key to cities.id
    * class attribute user_id
      * represents a column containing a string (60 characters)
      * can’t be null
      * is a foreign key to users.id
    * class attribute name
      * represents a column containing a string (128 characters)
      * can’t be null
    * class attribute description
      * represents a column containing a string (1024 characters)
      * can be null
    * class attribute number_rooms
      * represents a column containing an integer
      * can’t be null
      * default value: 0
    * class attribute number_bathrooms
      * represents a column containing an integer
      * can’t be null
      * default value: 0
    * class attribute max_guest
      * represents a column containing an integer
      * can’t be null
      * default value: 0
    * class attribute price_by_night
      * represents a column containing an integer
      * can’t be null
      * default value: 0
    * class attribute latitude
      * represents a column containing a float
      * can be null
    * class attribute longitude
      * represents a column containing a float
      * can be null
* Update User: (models/user.py)
  * Add or replace in the class User:
class attribute places must represent a relationship with the class Place. If the User object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his User should be named user
* Update City: (models/city.py)
  * Add or replace in the class City:
class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his City should be named cities

```sh
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Place city_id="4b457e66-c7c8-4f63-910f-fd91c3b7140b" user_id="4f3f4b42-a4c3-4c20-a492-efff10d00c0b" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) ed72aa02-3286-4891-acbc-9d9fc80a1103
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Place' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Place] (ed72aa02-3286-4891-acbc-9d9fc80a1103) {'latitude': 37.774, 'city_id': '4b457e66-c7c8-4f63-910f-fd91c3b7140b', 'price_by_night': 120, 'id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'user_id': '4f3f4b42-a4c3-4c20-a492-efff10d00c0b', 'max_guest': 6, 'created_at': datetime.datetime(2017, 11, 10, 1, 22, 30), 'description': None, 'number_rooms': 3, 'longitude': -122.431, 'number_bathrooms': 1, 'name': '"Lovely place', 'updated_at': datetime.datetime(2017, 11, 10, 1, 22, 30)}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: ed72aa02-3286-4891-acbc-9d9fc80a1103
      created_at: 2017-11-10 01:22:30
      updated_at: 2017-11-10 01:22:30
         city_id: 4b457e66-c7c8-4f63-910f-fd91c3b7140b
         user_id: 4f3f4b42-a4c3-4c20-a492-efff10d00c0b
            name: "Lovely place"
     description: NULL
    number_rooms: 3
number_bathrooms: 1
       max_guest: 6
  price_by_night: 120
        latitude: 37.774
       longitude: -122.431
```

### [ 9. DBStorage - Review ](./models/review.py)
* Update Review: (models/review.py)
  * Review inherits from BaseModel and Base (respect the order)
  * Add or replace in the class Review:
    * class attribute \_\_tablename\_\_
      * represents the table name, reviews
    * class attribute text
      * represents a column containing a string (1024 characters)
      * can’t be null
    * class attribute place_id
      * represents a column containing a string (60 characters)
      * can’t be null
      * is a foreign key to places.id
    * class attribute user_id
      * represents a column containing a string (60 characters)
      * can’t be null
      * is a foreign key to users.id
* Update User: (models/user.py)
  * Add or replace in the class User:
class attribute reviews must represent a relationship with the class Review. If the User object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his User should be named user
* Update Place: (models/place.py)
  * for DBStorage: class attribute reviews must represent a relationship with the class Review. If the Place object is deleted, all linked Review objects must be automatically deleted. Also, the reference from a Review object to his Place should be named place
  * for FileStorage: getter attribute reviews that returns the list of Review instances with place_id equals to the current Place.id => It will be the FileStorage relationship between Place and Review

```sh
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create User email="bob@hbtn.io" password="bobpwd" first_name="Bob" last_name="Dylan"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) d93638d9-8233-4124-8f4e-17786592908b
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'create Review place_id="ed72aa02-3286-4891-acbc-9d9fc80a1103" user_id="d93638d9-8233-4124-8f4e-17786592908b" text="Amazing_place,_huge_kitchen"' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) a2d163d3-1982-48ab-a06b-9dc71e68a791
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'all Review' | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py 
(hbnb) [[Review] (f2616ff2-f723-4d67-85dc-f050a38e0f2f) {'text': 'Amazing place, huge kitchen', 'place_id': 'ed72aa02-3286-4891-acbc-9d9fc80a1103', 'id': 'f2616ff2-f723-4d67-85dc-f050a38e0f2f', 'updated_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'created_at': datetime.datetime(2017, 11, 10, 4, 6, 25), 'user_id': 'd93638d9-8233-4124-8f4e-17786592908b'}]
(hbnb) 
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM reviews\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: f2616ff2-f723-4d67-85dc-f050a38e0f2f
created_at: 2017-11-10 04:06:25
updated_at: 2017-11-10 04:06:25
      text: Amazing place, huge kitchen
  place_id: ed72aa02-3286-4891-acbc-9d9fc80a1103
   user_id: d93638d9-8233-4124-8f4e-17786592908b
```

### [ 10. DBStorage - Amenity... and BOOM!  ](./models/amenity.py)
* Update Amenity: (models/amenity.py)
  * Amenity inherits from BaseModel and Base (respect the order)
  * Add or replace in the class Amenity:
    * class attribute \_\_tablename\_\_
      * represents the table name, amenities
    * class attribute name
      * represents a column containing a string (128 characters)
      * can’t be null
    * class attribute place_amenities must represent a relationship Many-To-Many between the class Place and Amenity. Please see below more detail: place_amenity in the Place update
* Update Place: (models/place.py)
  * Add an instance of SQLAlchemy Table called place_amenity for creating the relationship Many-To-Many between Place and Amenity:
    * table name place_amenity
    * metadata = Base.metadata
    * 2 columns:
      * place_id, a string of 60 characters foreign key of places.id, primary key in the table and never null
      * amenity_id, a string of 60 characters foreign key of amenities.id, primary key in the table and never null
  * Update Place class:
    * for DBStorage: class attribute amenities must represent a relationship with the class Amenity but also as secondary to place_amenity with option viewonly=False (place_amenity has been define previously)
    * for FileStorage:
      * Getter attribute amenities that returns the list of Amenity instances based on the attribute amenity_ids that contains all Amenity.id linked to the Place
      * Setter attribute amenities that handles append method for adding an Amenity.id to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing.

```sh
guillaume@ubuntu:~/AirBnB_v2$ cat main_place_amenities.py 
```
```python
#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *

# creation of a State
state = State(name="California")
state.save()

# creation of a City
city = City(state_id=state.id, name="San Francisco")
city.save()

# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
place_1 = Place(user_id=user.id, city_id=city.id, name="House 1")
place_1.save()
place_2 = Place(user_id=user.id, city_id=city.id, name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")
```
```sh
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py
OK
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM amenities\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
        id: 47321eb8-152a-46df-969a-440aa67a6d59
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Cable
*************************** 2. row ***************************
        id: 4a307e7f-68f9-438f-81c0-8325898dda2a
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Oven
*************************** 3. row ***************************
        id: b80aec52-d0c9-420a-8471-3254572954b6
created_at: 2017-11-10 04:22:02
updated_at: 2017-11-10 04:22:02
      name: Wifi
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM places\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
              id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 1
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
*************************** 2. row ***************************
              id: db549ae1-4500-4d0c-9b50-4b4978ed229e
      created_at: 2017-11-10 04:22:02
      updated_at: 2017-11-10 04:22:02
         city_id: 9d60df6e-31f7-430c-8162-69e89f4a17aa
         user_id: 9b37bd51-6aef-485f-bf10-c7ab83fea2e9
            name: House 2
     description: NULL
    number_rooms: 0
number_bathrooms: 0
       max_guest: 0
  price_by_night: 0
        latitude: NULL
       longitude: NULL
guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ echo 'SELECT * FROM place_amenity\G' | mysql -uhbnb_dev -p hbnb_dev_db
Enter password: 
*************************** 1. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 2. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 47321eb8-152a-46df-969a-440aa67a6d59
*************************** 3. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: 4a307e7f-68f9-438f-81c0-8325898dda2a
*************************** 4. row ***************************
  place_id: 497e3867-d6e9-4401-9c7c-9687c18d2ac7
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
*************************** 5. row ***************************
  place_id: db549ae1-4500-4d0c-9b50-4b4978ed229e
amenity_id: b80aec52-d0c9-420a-8471-3254572954b6
```

## Authors
* [__Tu Vo__](https://github.com/tuvo1106)
* [__Drew Maring__](https://github.com/dmaring)
* [__Kevin Yook__](https://github.com/yook00627)
