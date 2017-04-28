# PROJECT TITLE
DOJO ROOM ALLOCATION FOR ANDELA FELLOWS AND STAFF

#DESCRIPTION AND BACKGROUND
Andela Kenya building also known as the DOJO houses a number of offices and Living rooms for Fellows and Staff.
The project is meant to assist the building administrators assign offices and Living spaces to the different Staff
and Fellows while also tracking room occupancy at any point in time. These rooms are issued randomly as long as there is
still some free slots in the said room. An office can only sit up to six (6) people while a living room can house up to four (4) people

#PROJECT INSTALLATION BRIEF
The project has been built in Python and recommends Python 3 and above. Ensure you have installed everything in the requirements.txt file, then on the commandline launch the application
from the command:

python cli_interactive.py

The above command should usher you in the (The Dojo) prompt

    (The Dojo) create_room (livingspace|office) <room_name>...
    (The Dojo) add_person <first_name> <last_name> <FELLOW> | <STAFF> [wants_accommodation]
    (The Dojo) reallocate_person <first_name> <last_name> <new_room>
    (The Dojo) load_people <filename>
    (The Dojo) print_allocations [--o=<filename>]
    (The Dojo) print_unallocated [--o=<filename>]

