# Question No 3 - 10 Numbers

numbers = [12, 5, 8, 23, 45, 2, 90, 33, 17, 6]

total_sum = sum(numbers)
average = total_sum / len(numbers)
largest = max(numbers)
smallest = min(numbers)

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Numbers are: {numbers}")
print(f"Sum = {total_sum}")
print(f"Average = {average}")
print(f"Largest number = {largest}")
print(f"Smallest number = {smallest}")
print(f"Number of even numbers = {even_count}")
print(f"Number of odd numbers = {odd_count}")
