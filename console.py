#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def do_help(self, arg):
        print("help!")

    cmd.Cmd.prompt = '(hbnb)'

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
