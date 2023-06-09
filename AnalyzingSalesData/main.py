import os
import datetime

folder_name = "output_folder"
os.makedirs(folder_name, exist_ok=True)

total_trades = 0

with open('sales_log.txt', 'r') as file:
    for line in file:
        if 'trades' in line:
            events = line.split(':')[-1].split(',')
            for event in events:
                key_value = event.strip().split('=')
                if key_value[0] == 'trades':
                    total_trades += int(key_value[1])

print(total_trades)


timestamp = datetime.datetime.now().strftime('%H-%M-%S-%m-%d-%Y')

output_folder = os.path.join(os.getcwd(), folder_name)
output_file = os.path.join(output_folder, f"{timestamp}.txt")

with open(output_file, 'w') as output:
    output.write(str(total_trades))

print(f"Output saved to {output_file}.")
