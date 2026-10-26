start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []

for i in range(start, end + 1):
    squares.append(i ** 2)

odd = []
even = []

for num in squares:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Square values:", squares)
print("Odd square values:", odd)
print("Even square values:", even)