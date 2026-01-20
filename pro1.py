#1Write a program to input p, r, n and find out interest using simple input output statement.

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
n = float(input("Enter the time (in years): "))

si = (p * r * n) / 100

print("Simple Interest is:", si)

