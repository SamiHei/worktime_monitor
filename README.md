# Time It Monitor

Motivation: Program to monitor my own time usage when studying, programming etc.

## Running the program

Run the program from the root folder by using following command:
```
Python3 main.py
```

## Usage

This is a monitoring program to keep up with your time usage

On periods and export menu you can navigate back by using BACKSPACE
On about view you can exit using BACKSPACE

## Programming language and libraries

Program is made with Python3 and uses following standard libraries:

- Curses - https://docs.python.org/3/howto/curses.html
- Time - https://docs.python.org/3/library/time.html
- Datetime - https://docs.python.org/3/library/datetime.html
- Os - https://docs.python.org/3/library/os.html
- Sqlite3 - https://docs.python.org/3/library/sqlite3.html
- Csv - https://docs.python.org/3/library/csv.html
- Json - https://docs.python.org/3/library/json.html

## Technical solutions

This program uses sqlite on creating local database and handling it
Periods are saved and loaded from the local database
You can export your data to .csv and .json formats and those are created on the root folder

