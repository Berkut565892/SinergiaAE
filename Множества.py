N = int(input())
numbers = list(map(int, input().split()))

unique_numbers = set(numbers)
count = len(unique_numbers)

print(count)