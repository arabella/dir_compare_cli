# CLI APP TO COMPARE TWO DIRECTORIES RECURSIVELY

## How to run
1. Install Python 2.7.15
2. Clone the project
3. Run _pip install requirements.txt_
4. Open a terminal in the project folder and run _python dircompare.py --help_
5. To run the tests execute _python -m unittest discover -p 'dircmp_tests.py'

## TODO
-[] fix recursive function when running on Windows

-[] continue program execution if a file with permission denied is found
(currently the program exits)

-[] add [OPTION] for accessing a directory on a remote server
(once entered by the user upon _prompt_ store credentials in a config file and pass them to the main function using @pass_context)

-[] add check for the last time a file was updated and separate files wth different versions even if content is identical
