import csv
from tabulate import tabulate
import os

csv_file_path = 'players.csv'

schema = ['First Name', 'Last Name', 'Age', 'Nationality', 'Role', 'Runs', 'Balls', 'Wickets', 'Strike Rate']

def create_csv_file(csv_file, schema):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(schema)

if not os.path.exists(csv_file_path):
    create_csv_file(csv_file_path, schema)

while True:
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    choice = input("Enter '1' to add a player, '2' to delete a player, '3' to update a player, '4' to search for players, '5' to display the table or '0' to exit: ")

    if choice == '5':
        for player in data:
            player['Runs'] = int(player['Runs'])
            player['Balls'] = int(player['Balls'])
            player['Wickets'] = int(player['Wickets'])
            if player['Strike Rate'] != 'none':
                player['Strike Rate'] = float(player['Strike Rate'])

        print(tabulate(data, headers='keys', tablefmt='grid'))

    if choice == '0':
        break
        
    if choice == '1':
        print("Enter Details:")
        fName = input("First Name: ")
        lName = input("Last Name: ")
        age = input("Age: ")
        country = input("Nationality: ")
        role = input("Role(Batsmen, Bowler, All-rounder, Wk-Batsmen): ")
        runs = int(input("Runs: "))
        balls = int(input("Balls: "))
        wickets = int(input("Wickets: "))
        sRate = input("Strike Rate (none/number): ")

        if sRate == "none":
            if role == "Batsmen" or role == "Wk-Batsmen":
                new_sRate = round(runs / balls, 3)
            elif role == "Bowler":
                new_sRate = round(wickets / balls, 3)
            elif role == "All-rounder":
                new_sRate = max(round(runs / balls, 3), round(wickets / balls, 3))
        else:
            new_sRate = round(float(sRate), 3)

        new_player = {
            "First Name": fName,
            "Last Name": lName,
            "Age": age,
            "Nationality": country,
            "Role": role,
            "Runs": runs,
            "Balls": balls,
            "Wickets": wickets,
            "Strike Rate": new_sRate,
        }

        fieldnames = schema  # Get the fieldnames from the schema
        if not os.path.exists(csv_file_path):
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(new_player)
        else:
            with open(csv_file_path, mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writerow(new_player)

    if choice == '2':
        last_name = input("Enter the last name of the player you want to delete: ")
        first_name = input("Enter the first name of the player you want to delete: ")
        player_deleted = False
        rows = []

        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            fieldnames = reader.fieldnames
            for row in reader:
                if row['First Name'].strip().lower() == first_name.strip().lower() and row['Last Name'].strip().lower() == last_name.strip().lower():
                    player_deleted = True
                else:
                    rows.append(row)

        if player_deleted:
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)

        if player_deleted:
            print(f"Player {first_name} {last_name} deleted successfully.")
        else:
            print(f"Player {first_name} {last_name} not found in the data.")

    if choice == '4':
        attribute = input("Enter the attribute you want to search for (First Name, Last Name, Age, Nationality, Role, Runs, Balls, Wickets, Strike Rate): ")
        value = input(f"Enter the value for the {attribute}: ")
        found_players = []

        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if attribute in row and value.lower() in row[attribute].lower():
                    found_players.append(row)

        if found_players:
            print(f"Players with {attribute} equal to '{value}':")
            print(tabulate(found_players, headers='keys', tablefmt='grid'))
        else:
            print(f"No players found with {attribute} equal to '{value}'.")

    if choice == '3':
        last_name = input("Enter the last name of the player you want to update: ")
        first_name = input("Enter the first name of the player you want to update: ")
        attribute = input("Enter the attribute you want to update (First Name, Last Name, Age, Nationality, Role, Runs, Balls, Wickets, Strike Rate): ")
        new_value = input("Enter the new value for the attribute: ")
        fieldnames = schema
        updated_data = []
        player_updated = False

        with open(csv_file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['First Name'].strip().lower() == first_name.strip().lower() and row['Last Name'].strip().lower() == last_name.strip().lower():
                    player_updated = True
                    if attribute in ['First Name', 'Last Name', 'Age', 'Nationality']:
                        row[attribute] = new_value
                    elif attribute in ['Runs', 'Balls', 'Wickets']:
                        row[attribute] = int(new_value)
                        if row['Role'] in ['Batsmen', 'Bowler', 'All-rounder']:
                            row['Strike Rate'] = round(float(row['Runs']) / float(row['Balls']), 3)
                    elif attribute == 'Role':
                        row[attribute] = new_value
                    elif attribute == 'Strike Rate':
                        row[attribute] = round(float(new_value), 3)
                    else:
                        print("Invalid attribute. No changes were made.")
                updated_data.append(row)

        if player_updated:
            with open(csv_file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(updated_data)

        if player_updated:
            print(f"Player {first_name} {last_name}'s {attribute} updated successfully.")
        else:
            print(f"Player {first_name} {last_name} not found in the data.")
