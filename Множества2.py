first_list = set(map(int, input().split()))
second_list = set(map(int, input().split()))

common_numbers = first_list.intersection(second_list)
count = len(common_numbers)

print(count)