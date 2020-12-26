# Time It Monitor

Motivation: Program to monitor my own time usage when studying, programming etc.

## Running the program

Run the program from the root folder by using following command:
```
python3 main.py
```

## Usage

Periods with recorded time of 0 are not saved!

On periods and export menu you can navigate back by using BACKSPACE or LEFT key

On about view you can exit using BACKSPACE

## Programming language and libraries

Program is made with Python3 (version 3.6.9) and uses following standard libraries:

- Curses - https://docs.python.org/3/howto/curses.html
- Time - https://docs.python.org/3/library/time.html
- Datetime - https://docs.python.org/3/library/datetime.html
- Os - https://docs.python.org/3/library/os.html
- Sqlite3 - https://docs.python.org/3/library/sqlite3.html
- Csv - https://docs.python.org/3/library/csv.html
- Json - https://docs.python.org/3/library/json.html

## Technical solutions

This program uses sqlite on creating local database and handling it.

Periods are saved and loaded from the local database.

You can export your data to .csv and .json formats and those are created on the root folder.

## Tested operating systems

At the moment this program is only tested on Ubuntu 18.04 LTS

If you are using Windows you need to install:
```
pip install windows-curses
```

## Notes

Program scales some, but probably wont work when using too small terminal size!
