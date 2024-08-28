number = int(input("Enter a two digit number: "))
tens = number // 10
units = number % 10
swapped_number = units * 10 + tens
print("Digits Swapped: {}".format(swapped_number))

