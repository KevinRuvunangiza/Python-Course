# 1. Get input and convert to float immediately
bill = float(input("What is the bill amount? "))

# 2. Math
tip = bill * 0.15
total = bill + tip

# 3. Print
print(f"The tip is: ${tip}")
print(f"The total is: ${total}")