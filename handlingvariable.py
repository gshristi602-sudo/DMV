n = int(input("Enter the value of n: "))
numbers = list(map(int, input("Enter the numbers separated by space: ").split()))
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing_number = expected_sum - actual_sum
if missing_number == 0:
    print("No number is missing.")
else:
    print("Missing number is:", missing_number)
