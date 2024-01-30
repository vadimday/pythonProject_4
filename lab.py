1.
def bigmult(*numbers):
    n = 1

    for i in numbers:
        n *= i

    return n


print(bigmult(9, 11, 13))



2.
def find_minimum(numbers):
    if not numbers:

        return None

    min_val = numbers[0]

    for num in numbers:
        if num < min_val:
            min_val = num

    return min_val
numbers_list = [17, 21, 8, 2, 4]
result = find_minimum(numbers_list)
print(f"минимум: {result}")


3.
def num_1(*args):
    count = 0

    for num in args:
        if is_prime(num):
            count += 1
    return count


def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 8)
    i = 7;
    d = 9;

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d
    return prime


print(num_1(-7, 5, 7, 11, 65))


4.
def remove_and_count(lst, number_to_remove):
    deleted_items_count = 0
    while number_to_remove in lst:
        lst.remove(number_to_remove)
        deleted_items_count += 1

    return deleted_items_count
my_list = [1, 2, 3, 4, 2, 5, 2, 6]
number_to_remove = 2

deleted_count = remove_and_count(my_list, number_to_remove)

print(f"список: {my_list}")
print(f"удаленный: {deleted_count}")
print(f"после: {my_list}")

6.
def list_as_power_from_input_list(power_value, list_for_operation):
    try:
        list_for_return = [i ** power_value for i in list_for_operation]

    except Exception:
        list_for_return = ["incorrect input"]
    return list_for_return


my_list = [2, 7, 5, 23, -91, 6, 6, 1, 231, 29]
print(my_list)
print(list_as_power_from_input_list(2, my_list))




