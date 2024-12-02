class House:
    def __init__(self, address, sqft, price):
        self.address = address
        self.sqft = int(sqft)
        self.price = int(price)
    def costpersqft(self):
        return self.price / self.sqft
    def payment(self, ar, ny):
        r = ar / 12
        n = ny * 12
        if r == 0:
            return self.price / n
        else:
            return (self.price * r * (1 + r)**n) / ((1 + r)**n - 1)
house_list = []
with open("Exam Three Houses.txt", "r") as file:
    for line in file:
        data = line.strip().split(", ")
        house_list.append(House(data[0], data[1], data[2]))
interest_rate = float(input("Enter the Interest Rate: ")) / 100 
years = int(input("Enter the total Years for the Mortgage: "))
print(f"\n{'Address':<15} {'Sq Ft':<8} {'SqFt Cost':<10} {'Price':<10} {'Payment':<10}")
print("-" * 55)
for house in house_list:
    sqft_cost = house.costpersqft()
    monthly_payment = house.payment(interest_rate, years)
    print(f"{house.address:<15} {house.sqft:<8} {sqft_cost:<10.2f} {house.price:<10} {monthly_payment:<10.2f}")