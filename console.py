#!/usr/bin/python3
"""Module for class HBNBCommand and set the console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand for the console"""
    prompt = '(hbnb) '
    
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
