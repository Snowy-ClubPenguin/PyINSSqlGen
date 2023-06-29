# Python SQL Insert Generator

This project provides a Python-based solution for managing chat filters in a Club Penguin Private Server (CPPS), or any similar platform. 

## Features 

**1. Ban List Generator (`main.py`):** 

This script generates SQL insert statements to create a ban list based on a provided text file. The generated SQL statements are then ready to be executed on your database. 

Please note that a list of banned words is not included with this project. You will need to supply your own text file with a list of words you wish to ban.

**2. Warn and Ban Flag Modifier (`main2.py`):** 

This script scans an existing SQL file for specific words and modifies the associated warn and ban flags. 

More specifically, it does the following:
- Finds instances of a specified word (default is set to a placeholder)
- Changes the warn (kick) flag from `True` to `False`
- Changes the ban flag from `False` to `True`

The updated SQL statements are then written to `updated_sql_insertions.sql`.

## How to Use

1. Run `main.py` with a text file containing words to ban as input. This generates an SQL file with the appropriate insert statements.
2. Run `main2.py` to modify the generated SQL file, updating the warn and ban flags as described above. 

Please ensure you test these scripts in a controlled environment before running them on production data.
