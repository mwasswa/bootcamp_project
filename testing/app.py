"""
Usage:
    (dojo) create_room (livingspace|office) <room_name>...
    (dojo) add_person <first_name> <last_name> <FELLOW> | <STAFF> [wants_accommodation]
    (dojo)
    (dojo) (-i | --interactive)
    (dojo) (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from dojo_app import dojo
from database.database import Database

#db = Database(dojo)


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as exit:
            # Thrown when args do not match

            print("You have entered an invalid command!")
            print(exit)
            return

        except SystemExit:
            # Prints the usage for --help

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class DocoptInterface(cmd.Cmd):

    #welcome = welcome_message()
    prompt = "(dojo)"

    file = None

    def do_quit(self, arg):
        """Quits out of the interactive mode"""
        exit()

options = docopt(__doc__, sys.argv[1:])
if options["--interactive"]:
    DocoptInterface().cmdloop()

print(options)