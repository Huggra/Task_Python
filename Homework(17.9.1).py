random_list = input("Введите последовательность чисел через пробел: ")
any_number = int(input("Введите любое число: "))
# 112 186 11 64 38 92 127 30 86 117 193 146 128 161 115
a_list = list(map(int, random_list.split()))

def sorted_list(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
    return a_list

def normalize(index):
    if index < 0:
        return 0
    return index

def handle_binary(split_list, any_number, left, right):
    while right - left > 1:
        middle = (left + right) // 2
        if a_list[middle] == any_number:
            return normalize(middle - 1)
        if a_list[middle] < any_number:
            left = middle
        else:
            right = middle
    return left

def handle_special_cases(a_list, any_number):
    for index in range(len(a_list)):
        if a_list[index] >= any_number:
            return normalize(index - 1)
    return len(a_list) - 1

def index_lookop(a_list, any_number, left, right):
    if (any_number not in a_list) or a_list.count(any_number)>1:
        return handle_special_cases(a_list, any_number)
    return handle_binary(a_list, any_number, left, right)

print(sorted_list(a_list))
print(index_lookop(a_list, any_number, 0, len(a_list)-1))
