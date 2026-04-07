import csv
import os

filename = "snvk-tool-data_epsg25832.csv"
fields = ['id', 'name', 'kategorie', 'nutzung', 'räume_funktionen', 'nutzungsfläche', 'lhm_orga', 'x', 'y', 'bezirk', 'hausnummer', 'gebäude', 'flurstück', 'träger', 'eigentumsverhältnis', 'objektstatus']
rows = [
            ["test1", "test2", "test3"],
            ["test4", "test5"]
        ]

# Get the user's home directory
home = os.path.expanduser("~")

# Set the desktop path based on the operating system
if os.name == 'nt':  # Windows
    desktop = os.path.join(home, 'Desktop')
elif os.name == 'posix':  # macOS or Linux
    desktop = os.path.join(home, 'Desktop')

# Change the current working directory to the desktop
os.chdir(desktop)

print(f"Current working directory is now: {os.getcwd()}")

file_path = os.getcwd()+filename
print(file_path)

# TODO: maybe check if file already exists...
try:
    with open(file_path, 'w') as file:
        file.write("Hello, World!")
except FileExistsError:
    print(f"The file '{file_path}' already exists.")

with open(filename, 'w', newline='', encoding='utf-8') as csvfile:       
    writer = csv.writer(csvfile, delimiter=';') # Create writer object
    writer.writerow(fields)             # Write header
    writer.writerows(rows)              # Write multiple rows
    print('data is written in ' + filename)
