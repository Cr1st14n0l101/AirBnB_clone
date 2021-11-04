#!/usr/bin/python3
"""Module for class HBNBCommand and set the console"""
import cmd
from models.base_model import BaseModel
from models.user import User
import models


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand for the console"""
    prompt = '(hbnb) '

    def do_create(self, line):
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
                        if split_line[1] == splited[1] and splited[0] == split_line[0]:
                            return print(value)
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_destroy(self, line):
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
                        if split_line[1] == splited[1] and splited[0] == split_line[0]:
                            del dictionary_isntance[key]
                            models.storage.save()
                            return
                    print("** no instance found **")
            except Exception:
                print("** class doesn't exist **")

    def do_all(self, line):
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

    def do_quit(self, line):
        """Command to exit from the console\n"""
        return True

    def emptyline(self):
        """It repeats the last nonempty command entered"""
        pass

    def do_EOF(self, line):
        """It exit from the console when the user type Ctrl + D\n"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
