# I need a program that select what's inside a txt file, separate the things inside it and output the sum of what I need
# I need to get the trades=X , so in the end , i'll sum every X that I found and have an output

import os
import datetime

output_folder_name = "test_folder"
os.makedirs(output_folder_name, exist_ok=True)
totalTrades = 0

with open('testfile.txt', 'r') as file:
    for line in file:
        if 'trades' in line:
            events = line.split(',')
            for event in events:
                catchTrade = event.strip().split('=')
                if catchTrade[0] == 'trades':
                    totalTrades += int(catchTrade[1])
                    print(f'Total Trades = {totalTrades}')

timestamp = datetime.datetime.now().strftime('%H-%M-%S-%m-%d-%Y')
print(timestamp)
output_folder = os.path.join(os.getcwd(), output_folder_name)
output_file = os.path.join(output_folder, f"{timestamp}.txt")

with open(output_file, 'w') as output:
    output.write(str(totalTrades))

print(f"Saved File inside {output_file}")