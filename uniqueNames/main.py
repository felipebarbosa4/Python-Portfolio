# Initialize an empty dictionary to store the frequency of names
name_count = dict()

# Define the path to the input file containing the duplicate names
input_filepath = 'duplicates.txt'

# Define the path to the output file where the deduplicated names will be stored
output_filepath = 'output.txt'

# Open the input file in read mode and the output file in write mode
with open(input_filepath, 'r') as infile, open(output_filepath, 'w') as outfile:
    # Iterate over each line in the input file
    for line in infile:

        # Remove leading and trailing whitespace from the line and split it into words
        names = line.strip().split()

        # Iterate over each name in the list of names
        for name in names:

            # Check if the name already exists in the name_count dictionary
            if name in name_count:

                # If the name exists, increment its count by 1
                name_count[name] += 1

                # Create a new name by appending the count to the original name
                new_name = f"{name}{name_count[name]}"

                # Print the new name
                print(new_name, end='\n')

                # Write the new name to the output file, followed by a newline character
                outfile.write(new_name + '\n')

            else:
                # If the name does not exist in the dictionary, add it with a count of 0
                name_count[name] = 0

                # Print the original name, as it is its first occurrence
                print(name, end='\n')

                # Write the original name to the output file, followed by a newline character
                outfile.write(name + '\n')
