#!/usr/bin/python3
"""
this is console
"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

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

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        cls_name = args[0]

        if len(args) < 2:
            print("** instance id missing **")
            return

        if cls_name not in globals():
            print("** class doesn't exist **")
            return

        key = "{}.{}".format(cls_name, args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")           
   
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0] 
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            key = class_name + "." + args[1]
        except IndexError:
            print("** instance id missing **")
            return
        if not key in storage.all():
            print("** no instance found **")
            return 
        for k in storage.all():
            if (k == key):
                del storage.all()[key]
                storage.save()
                return

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        args = arg.split()

        
        if len(arg) == 0:
            for value in storage.all().values():
                print(value)
            return

        class_name = args[0] 
        
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        
        for value in storage.all().values():
            if value.__class__.__name__ == class_name:
                print(value)

    def do_update(self, arg):
        """Updates instance based on class name and id by adding"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        args = arg.split()
        try:
            class_name = args[0] 
            if class_name not in globals():
                print("** class doesn't exist **")
                return
            key = class_name + "." + args[1]
        except IndexError:
            print("** instance id missing **")
            return
        if not key in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        elif len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        attr_val = args[3]
        setattr(storage.all()[key], attr_name, attr_val)
        storage.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
