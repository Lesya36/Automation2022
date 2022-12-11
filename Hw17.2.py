# Assume you have the list xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
# Write a loop that prints each of the numbers on a new line.
# Write a loop that prints each number and its square on a new line.
# Write a loop that adds all the numbers from the list into a variable called total.
#Print the product of all numbers in the list

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(i)

for i in xs:
    print("square of",i, i*i)


total=0
for i in xs:
    total += i

print(total)


product = 1
for i in xs:
    product *= i

print(product)


