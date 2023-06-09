
name_count = dict()
filepath = 'duplicates.txt'
with open(filepath, 'r') as file:
    for line in file:
        names = line.strip().split()
        for name in names:
            if name in name_count:
                name_count[name] += 1
                print(f"{name}{name_count[name]}", end='\n')
            else:
                name_count[name] = 0
                print(name, end='\n')
print()