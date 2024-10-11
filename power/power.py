def power(base, exponent):
    return base**exponent
   

if __name__ == "__main__":
    base = float(input("Enter the base number: "))
    exponent = int(input("Enter the exponent (integer): "))
    print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")
