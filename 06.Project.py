def merge_files(input_file_path, merge_file_path, output_file_path):
    input_records = 0
    merge_records = 0
    output_records = 0
    with open(output_file_path, 'w') as output_file:
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                if line.strip() == '**Insert Merge File Here**':
                    with open(merge_file_path, 'r') as merge_file:
                        for merge_line in merge_file:
                            output_file.write(merge_line)
                            merge_records += 1
                            output_records += 1
                else:
                    output_file.write(line)
                    input_records += 1
                    output_records += 1
    print(f"Input Records: {input_records}")
    print(f"Merge Records: {merge_records}")
    print(f"Output Records: {output_records}")
input_file_path = '06.Project Input File.txt'
merge_file_path = '06.Project Merge File.txt'
output_file_path = '06.Project Output File.txt'
merge_files(input_file_path, merge_file_path, output_file_path)
