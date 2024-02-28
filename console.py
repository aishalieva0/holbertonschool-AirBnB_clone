#!/usr/bin/python3
"""
this is console
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """ commands """
    def do_quit(self, arg):
        """ exit """
        return True

    def do_EOF(self, arg):
        """ end of file """
        return True

    cmd.Cmd.prompt = '(hbnb)'

    def emptyline(self):
        """ overrides emptyline """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
