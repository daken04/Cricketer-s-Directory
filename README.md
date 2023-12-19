# Cricketer's Directory

The "Cricketer's Directory" is a Python program designed for the IPL team "Gachibowli Gorillas." This directory manages a list of cricket player entries, storing details such as first name, last name, age, nationality, role (batsmen, bowler, all-rounder, wk-batsmen), runs, balls, wickets, and strike rate.

## Functionality

The program provides a menu-driven interface with the following functionalities:

### 1. Load Entries from .csv file

Load existing entries from a CSV file to populate the cricketer's directory.

### 2. Display Directory

Display the cricketer's directory on the terminal in a table-like format.

### 3. Add New Entry

Allow users to add a new entry to the directory. The user may or may not provide the strike rate.

### 4. Remove and Update Entries

Enable users to remove and update existing entries in the directory.

### 5. Search Entries

Search for entries in the directory based on specified attribute(s).

### 6. Write Back to CSV

Write back the updated data to a CSV file, ensuring data persistence.

### 7. Exit

Exit the program.

## Strike Rate Calculation

For calculating the strike rate:
- If the player is a batsman, then Batting Strike rate = Runs/Balls.
- If the player is a bowler, then Bowling Strike rate = Wickets/Balls.
- If the player is an all-rounder, then Strike rate = max(Batting Strike rate, Bowling Strike rate).

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/daken04/Cricketer-s-Directory
    cd Cricketer-s-Directory
    ```

2. Run the program:

    ```bash
    python cricketers_directory.py
    ```

3. Follow the menu-driven options to interact with the Cricketer's Directory.

## CSV File Format

The CSV file format is designed to store the cricketer's directory data. Feel free to customize the format based on your preferences.

## Notes

- Data persistence is maintained by writing back to a CSV file upon program exit.
- For any issues or suggestions, please open an issue or submit a pull request.
