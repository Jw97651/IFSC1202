import csv
def read_distances(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        distances = [row for row in reader]
    return distances
def print_distances(distances):
    for row in distances:
        print("\t".join(row))
def find_distance(distances, from_city, to_city):
    try:
        from_index = next(i for i, row in enumerate(distances) if row[0] == from_city)
        to_index = distances[0].index(to_city)
        distance = distances[from_index][to_index]
        print(f"{from_city} to {to_city} - {distance} miles")
    except StopIteration:
        print("Invalid From City")
    except ValueError:
        print("Invalid To City")
def main():
    distances_file = '09.Project Distances.csv'
    distances = read_distances(distances_file)
    print_distances(distances)
    from_city = input("Enter From City: ")
    to_city = input("Enter To City: ")
    find_distance(distances, from_city, to_city)
if __name__ == "__main__":
    main()
