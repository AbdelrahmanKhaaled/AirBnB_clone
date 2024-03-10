#!/usr/bin/python3
'''Console'''
import cmd


class HBNBCommand(cmd.Cmd):
    print((hbnb))

    def do_quit(self, arg):
        '''Quit the program'''
        return True

    def do_EOF(self, arg):
        '''Quit the program'''
        return True

    def do_help(self, arg):
        '''help for progeam'''
        print("Quit command to exitthe program")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
