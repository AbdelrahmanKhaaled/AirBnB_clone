#!/usr/bin/python3
'''Console'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''HBNBCommand Class'''
    prompt = "(hbnb)"

    def do_quit(self, arg):
        '''Quit the program'''
        return True

    def do_EOF(self, arg):
        '''Quit the program'''
        print()
        return True

    def do_help(self, arg):
        '''help for progeam'''
        print("Quit command to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
