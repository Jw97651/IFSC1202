start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))
print(f"Special Numbers between {start} and {end}")
def special_number(num):
    original = num
    power = 0
    while num > 0:
        num //= 10
        power += 1
    num = original
    sum_of_powers = 0
    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** power
        num //= 10
    return sum_of_powers == original
for num in range(start, end + 1):
    if special_number(num):
        print(num)