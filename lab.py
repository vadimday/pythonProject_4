1.
total = 0

list1 = [27, 9, 2, 9, 29]



for ele in range(0, len(list1)):
	total = total + list1[ele]


print("Сумма: ", total)

2.
def large(arr):
    max_ = arr[0]
    for ele in arr:
        if ele > max_:
           max_ = ele
    return max_


list1 = [1,4,5,2,6]
result = large(list1)
print(result)


3.
def analyze_numbers(numbers):
    even_count = 0

    odd_count = 0

    positive_count = 0

    negative_count = 0
    for number in numbers:
        if number % 2 == 0:

            even_count += 1

        else:

            odd_count += 1
            if number > 0:

                positive_count += 1

            elif number < 0:

                negative_count += 1
                return even_count, odd_count, positive_count, negative_count

numbers_list = [1, 2, 3, -4, 0, -5, 6]

result = analyze_numbers(numbers_list)
print("Количество парных елементов:", result[0])

print("Количество непарных елементов:", result[1])

print("Количество положительных елементов:", result[2])

print("Количество отрицательных елементов:", result[3])


4.
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst
lst = [5,9,11,27,56]
print(Reverse(lst))


5.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def calculate_factorials(input_list):
    return [factorial(num) for num in input_list]


input_list = [17, 9, 1]
result = calculate_factorials(input_list)
print(result)
