import os
import datetime

# Create a folder to store the output file
folder_name = "output_folder"
os.makedirs(folder_name, exist_ok=True)

# Initializing the variable
total_trades = 0

# Open the log file
with open('logfile.txt', 'r') as file:
    for line in file:
        # If trades are present in the line, we process it
        if 'trades' in line:
            # Split the line using ':' and take the last part which contains the key–value pairs.
            # Using ',' to get individual events
            events = line.split(':')[-1].split(',')
            for event in events:
                # For each event, split using '=' to get the key and value
                key_value = event.strip().split('=')
                # If key is 'trades', we add the value to 'total_trades'
                if key_value[0] == 'trades':
                    total_trades += int(key_value[1])

# Get the current timestamp
timestamp = datetime.datetime.now().strftime('%H-%M-%S-%m-%d-%Y')

# Format the output file path
output_folder = os.path.join(os.getcwd(), folder_name)
output_file = os.path.join(output_folder, f"{timestamp}.txt")

# Save the output to the new file
with open(output_file, 'w') as output:
    output.write(str(total_trades))

print(f"Output saved to {output_file}.")
