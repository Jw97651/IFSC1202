def read_constitution(file_path):
    with open(file_path,'r') as file:
        lines=[line.strip() for line in file.readlines()]
    return lines
def find_section(lines,search_term):
    found_sections=set()
    for i,line in enumerate(lines):
        if search_term.lower() in line.lower():
            start_index=i
            while start_index>0 and lines[start_index-1]!='':
                start_index-=1
            end_index=i
            while end_index<len(lines)-1 and lines[end_index+1]!='':
                end_index+=1
            section=(start_index,end_index)
            found_sections.add(section)
    for start,end in found_sections:
        print(f"Line {start+1}:")
        for j in range(start,end+1):
            print(lines[j])
        print()
def main():
    constitution_file='constitution.txt'
    lines=read_constitution(constitution_file)
    while True:
        search_term=input("Enter search term: ")
        if not search_term:
            break
        find_section(lines,search_term)
if __name__=="__main__":
    main()
