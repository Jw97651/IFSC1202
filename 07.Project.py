def ParseDegreeString(ddmmss):
    degree_pos = ddmmss.find('°')
    minute_pos = ddmmss.find("'")
    second_pos = ddmmss.find('"')
    degrees = float(ddmmss[:degree_pos])
    minutes = float(ddmmss[degree_pos + 1:minute_pos])
    seconds = float(ddmmss[minute_pos + 1:second_pos])
    return degrees, minutes, seconds
def DDMMSStoDecimal(degrees, minutes, seconds):
    return degrees + minutes / 60 + seconds / 3600
def process_angle_file(input_file, output_file):
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w')
    count = 0
    for line in infile:
        line = line.strip()
        if line:
            degrees, minutes, seconds = ParseDegreeString(line)
            decimal_degrees = DDMMSStoDecimal(degrees, minutes, seconds)
            outfile.write(str(decimal_degrees) + '\n')
            count += 1
    infile.close()
    outfile.close()
    print(count, "records processed.")
input_filename = "07.Project Angles Input.txt"
output_filename = "07.Project Angles Output.txt"
process_angle_file(input_filename, output_filename)
