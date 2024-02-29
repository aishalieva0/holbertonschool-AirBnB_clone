#!/usr/bin/python3
"""
this is console
"""


import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ commands """
    def do_quit(self, arg):
        """ exit """
        return True

    def do_EOF(self, arg):
        """ end of file """
        return True

    def do_help(self, arg):
        """ help info """
        cmd.Cmd.do_help(self, arg)

    cmd.Cmd.prompt = '(hbnb)'

    def emptyline(self):
        """ overrides emptyline """
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")
"""
    def do_show(self, arg1, arg2):
        if not arg1:
            print("** class name missing **")
        elif :
            print("** class doesn't exist **")

"""     

if __name__ == '__main__':
    HBNBCommand().cmdloop()
