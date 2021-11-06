#  0x00. AirBnB clone - The console
<img align="left" src="https://github.com/Cr1st14n0l101/images/blob/master/68747470733a2f2f692e696d6775722e636f6d2f4a4f68615a356d2e706e67.png" style="float:right"></img>


# Project Description

This is the first of a series of projects, in order to clone the application known as AirBnB, in this first part the command interpreter is implemented using the Python programming language, different classes are used and different data of a user are added which are saved in a save file with the extension '.json'.
## Usage

The console is a program that shows us each of the options on the screen that the user can access.
| Command |         Description         |
|----------------|----------------------------------------------|
|`./console.py`|Starts the command interpreter showing the commands that can be used on the screen.|
|`create <class name>`|Create a new object and prints the id.|
|`show <class name> <id>`|Prints the string representation of an object based on the `class` name and `id`.|
|`destroy <class name> <id>`|Deletes an object based on the class name and `id`.|
|`all <class name>`|Prints all string representation of all instances based or not on the class name.|
|`update <class name> <id> <attribute> <value>`|Updates an instance based on the class name and `id` by adding or updating attribute.|

Non-interactive mode
~~~
$ echo "help" | ./console.py
(hbnb)


Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
~~~



## File storage

The folder  engine  manages the serialization and deserialization of all the data, following a JSON format.

A FileStorage class is defined in  file_storage.py  with methods to follow this flow:  `<object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>`

The  **init**.py  file contains the instantiation of the FileStorage class called  **storage**, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

## [](https://github.com/arthurdamm/AirBnB_clone#tests)Tests

All the code is tested with the  **unittest**  module. The test for the classes are in the  [test_models](https://github.com/arthurdamm/AirBnB_clone/blob/master/tests/test_models)  folder.
## Special Thanks

*First of all we want to thank Holberton School, who with their knowledge, resources and tools we have been able to carry out this project and each of its stages  to achieve the results we were looking for.
Thank you very much to all.*

## Authors
- [Cristian Oliveros](https://github.com/Cr1st14n0l101): *Four months ago I didn't know anything about programming, and today I feel like I can do a lot of things and I hope to continue learning a lot more with Holberton and have a promising future.*
- [Andrés Pirateque](https://github.com/4ndr3sxy):

