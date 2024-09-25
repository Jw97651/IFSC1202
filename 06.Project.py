# Initialize counters
input_count = 0
merge_count = 0
output_count = 0

# Open output file for writing
with open('06.Project Output File.txt', 'w') as output_file:
    # Open input file for reading
    with open('06.Project Input File.txt', 'r') as input_file:
        lines = input_file.readlines()
        
        for line in lines:
            input_count += 1
            output_file.write(line)
            
            # Check for the merge line
            if "**Insert Merge File Here**" in line:
                # Open merge file for reading
                with open('06.Project Merge File.txt', 'r') as merge_file:
                    merge_lines = merge_file.readlines()
                    for merge_line in merge_lines:
                        merge_count += 1
                        output_file.write(merge_line)
                
                # Break after merging
                break

        # Continue writing remaining lines of the input file
        for line in lines[input_count:]:
            output_file.write(line)

# Count output records
with open('06.Project Output File.txt', 'r') as output_file:
    output_count = sum(1 for _ in output_file)

# Print the counts
print(f"{input_count} input file records")
print(f"{merge_count} merge file records")
print(f"{output_count} output file records")
