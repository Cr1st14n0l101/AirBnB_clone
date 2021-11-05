#!/usr/bin/python3
"""Module for class HBNBCommand and set the console"""
import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.place import Place
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand for the console"""
    prompt = '(hbnb) '

    def do_create(self, line):
        """Create an object"""
        if line == "":
            print("** class name missing **")
        else:
            try:
                instance = eval("{}()".format(line))
                instance.save()
                print(instance.id)
            except Exception:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Show the information about an object"""
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                instance = eval("{}()".format(split_line[0]))
                if len(split_line) != 2:
                    print("** instance id missing **")
                else:
                    dictionary_isntance = models.storage.all()
                    for key, value in dictionary_isntance.items():
                        splited = key.split('.')
                        if (split_line[1] == splited[1] and
                                splited[0] == split_line[0]):
                            return print(value)
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Delete an object"""
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                instance = eval("{}()".format(split_line[0]))
                if len(split_line) != 2:
                    print("** instance id missing **")
                else:
                    dictionary_isntance = models.storage.all()
                    for key, value in dictionary_isntance.items():
                        splited = key.split('.')
                        if (split_line[1] == splited[1] and
                                splited[0] == split_line[0]):
                            del dictionary_isntance[key]
                            models.storage.save()
                            return
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Show all objects of the same class"""
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                eval("{}()".format(split_line[0]))
                models.storage.reload()
                dictionary_isntance = models.storage.all()
                new_list = []
                for key, value in dictionary_isntance.items():
                    splited = key.split('.')
                    if splited[0] == split_line[0]:
                        new_list.append(str(value))
                print(new_list)
            except Exception:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Usage: update <class name> <id> <attribute name> "<attribute value>
        update attribute instance object
        """
        flag = False
        key_dictionary = ""
        copy_object = object
        split_line = line.split()
        if len(split_line) == 0:
            print("** class name missing **")
        elif len(split_line) > 0:
            try:
                instance = eval("{}()".format(split_line[0]))
                if len(split_line) < 2:
                    print("** instance id missing **")
                else:
                    dictionary_isntance = models.storage.all()
                    for key, value in dictionary_isntance.items():
                        splited = key.split('.')
                        if (split_line[1] == splited[1]
                                and splited[0] == split_line[0]):
                            key_dictionary = key
                            copy_object = value
                            flag = True
                    if flag is False:
                        print("** no instance found **")
                    elif len(split_line) < 3:
                        print("** attribute name missing **")
                    elif len(split_line) < 4:
                        print("** value missing **")
                    else:
                        value_string = HBNBCommand.group_word(self, line)
                        if value_string == "":
                            value_string = split_line[3]
                        setattr(copy_object, split_line[2], value_string)
                        dictionary_isntance[key_dictionary] = copy_object
                        models.storage.save()
            except Exception:
                print("** class doesn't exist **")

    def do_quit(self, line):
        """Command to exit from the console\n"""
        return True

    def emptyline(self):
        """It repeats the last nonempty command entered"""
        pass

    def do_EOF(self, line):
        """It exit from the console when the user type Ctrl + D\n"""
        return True

    def group_word(self, line):
        """Convert a single string inside double quotes"""
        result_string = ""
        flag = False
        i = 0

        while len(line) > i:
            if line[i] == '"' or flag is True:
                flag = True
                result_string += line[i + 1]
                if line[i + 1] == '"':
                    result_string = result_string[:-1]
                    break
            i += 1
        return result_string

    def default(self, line):
        HBNBCommand.flag_global = True
        split_line = line.split('.')
        name_class = split_line[0]
        name_method = split_line[1].split('(')[0]
        if name_method == "all":
            HBNBCommand.do_all(self, name_class)
        elif name_method == "count":
            HBNBCommand.count_instances(self, name_class)
        elif name_method == "show":
            id_instance = HBNBCommand.group_word(self, line)
            string_to_show = ""
            string_to_show = name_class + " " + id_instance
            HBNBCommand.do_show(self, string_to_show)
        elif name_method == "destroy":
            string_to_destroy = ""
            id_instance = HBNBCommand.group_word(self, line)
            string_to_destroy = name_class + " " + id_instance
            HBNBCommand.do_destroy(self, string_to_destroy)
        elif name_method == "update":
            new_list = []
            string_to_destroy = ""
            id_instance = ""
            attr = ""
            value = ""
            new_list = line.split(',')
            id_instance = HBNBCommand.group_word(self, line)
            if id_instance == "":
                print("** instance id missing **")
            elif len(new_list) < 2:
                print("** attribute name missing **")
            elif len(new_list) < 3:
                print("** value missing **")
            else:
                if HBNBCommand.validate_bracket(self, line):
                    attr = HBNBCommand.group_word(self, new_list[1])
                    value = HBNBCommand.group_word(self, new_list[2])
                    string_to_destroy = (name_class + " " + id_instance +
                                         " " + attr + " " + value)
                    HBNBCommand.do_update(self, string_to_destroy)
                else:
                    new_dict = line.split('{')
                    new_dict = "{" + new_dict[1][:-1]
                    new_dict = eval(new_dict)
                    objects_dict = models.storage.all()
                    for key, value in objects_dict.items():
                        if id_instance == key.split('.')[1]:
                            for key2, value2 in new_dict.items():
                                value.__dict__[key2] = value2
                            models.storage.save()
                            break

    def count_instances(self, line):
        counter = 0
        for key in models.storage.all():
            if key.split('.')[0] == line:
                counter += 1
        print(counter)

    def validate_bracket(self, line):
        i = 0
        while len(line) > i:
            if line[i] == '{':
                return False
            i += 1
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
