# s = "hello, python"
# lst = [1, 2, 3, 4, 5]
# number_list_iterator = lst.__iter__()
# number_list_iterator = iter(lst)
# print(number_list_iterator)
# print(type(number_list_iterator))
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())
# print(number_list_iterator.__next__())

# a = 1555
# print(len(a))

# |--------------------------------------------------------------------------------------------------------------------|

# print(name)
# temp = int("W")

try:
    a = int(input('A '))
    b = int(input('B '))
    result = a / b
    print('try', result)
    number = int([1, 2, 3])
except TypeError:
    print("Преобразование")
except Exception:
    print('---')

except ZeroDivisionError:
    result = a / 1
    print('except', result)