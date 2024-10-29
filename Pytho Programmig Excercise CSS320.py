# Python Programming 1
numbers = [4, 2, 7, 3, 8, 5]
smallest = numbers[0]
largest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
    if number > largest:
        largest = number
print("Smallest number:", smallest)
print("Largest number:", largest)
# Python Programming 2
numbers = [1, 2, 3, 5, 6, 7, 9]
expected = 1
for number in numbers:
    if number != expected:
        break
    expected += 1
print("Smallest missing element:", expected)
# Python Programming 3
numbers = [1, 2, 2, 2, 5, 7, 7, 7, 8, 9]
count = 0
for number in numbers:
    if number == 7:
        count += 1
print("Number of occurrences of 7:", count)
