start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))
print(f"Prime Numbers between {start} and {end}")
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)