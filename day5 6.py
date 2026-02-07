numbers = [10, 20, 30, 40, 50]


new_num = int(input("Enter a number: "))


closest = numbers[0]
min_diff = abs(new_num - closest)

for num in numbers:
    diff = abs(new_num - num)
    if diff < min_diff:
        min_diff = diff
        closest = num

print("Closest number is:", closest)
