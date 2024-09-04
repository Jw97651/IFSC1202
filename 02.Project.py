import math
def main():
    side1 = float(input("Enter Side 1: "))
    side2 = float(input("Enter Side 2: "))
    side3 = float(input("Enter Side 3: "))
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    print(f"Area: {area:.1f}")
if __name__ == "__main__":
    main()