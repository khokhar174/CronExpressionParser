# Expression Parser

This program takes a raw expression with info regarding minute, hour, day of month, month, and day of week and a command
and output a formatted/expanded cron expression.

# System Requirements
```python==3.8.5```
```pip```
```git```

## Usage
To run this program, following are the steps:

1. Clone the repository to your local machine.
   1. ```git clone https://github.com/khokhar174/CronParser.git```
2. Open a terminal in the project main/root folder.
3. Install required packages
   1. ```pip install -m requirements.txt```
4. Run program with expression as an argument. Example:
    1. ```python main.py "*/15 0 1,15 * 1-5 /usr/bin/find" ```
5. The program will output the expanded values for expression. Example:

   ```
   minute        0 15 30 45
   hour          0
   day of month  1 15
   month         1 2 3 4 5 6 7 8 9 10 11 12
   day of week   1 2 3 4 5
   command       /usr/bin/find
   ```

6. Run tests using following command after making any change to code:
   ```python -m pytest ```

## Features

- Handles values with interval (`*/2` or `1-4/3`), range of values(`1-6`), any value (`*`), and comma seprated values (`1,2,4,5`) for each sub expression and validates if expression values are within the limits.
- Prints an output with expression part names and corresponding values.
