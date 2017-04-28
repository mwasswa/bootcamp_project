#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    (dojo) create_room (livingspace|office) <room_name>...
    (dojo) add_person <first_name> <last_name> <FELLOW> | <STAFF> [wants_accommodation]
    (dojo) reallocate_person <first_name> <last_name> <new_room>
    (dojo) load_people <filename>
    (dojo) print_allocations [--o=<filename>]
    (dojo) print_unallocated [--o=<filename>]
    (dojo)
    (dojo) (-i | --interactive)
    (dojo) (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
    --o=<filename>
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo_app.dojo import Dojo
#from Dojo import dojo
#from database.database import Database
dojo = Dojo()
#db = Database()
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to Dojo interactive Application!' \
        + ' (type help for a list of commands.)'
    prompt = '(The Dojo) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (Living|Office) <room_name>..."""
        dojo.create_room(args)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: \
        add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]"""
        dojo.add_person(args)

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <first_name> <last_name> <new_room>"""
        dojo.reallocate_person(args)

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people <filename>"""
        dojo.load_people(args)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [--o=filename.txt]"""
        dojo.print_allocations(args)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [--o=filename.txt]"""
        dojo.print_unallocated(args)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        dojo.print_room(args)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""
        print('Thanks for using the Dojo Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)