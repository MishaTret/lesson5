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
#
# try:
#     a = int(input('A '))
#     b = int(input('B '))
#     result = a / b
#     print('try', result)
#     number = int([1, 2, 3])
# except TypeError:
#     print("Преобразование")
# except Exception:
#     print('---')
#
# except ZeroDivisionError:
#     result = a / 1
#     print('except', result)

# |---------------------------------------------------2.0--------------------------------------------------------------|

# def checker(var):
#     if type(var) != str:
#         raise TypeError(f'Sorry, we do not work with {type(var)}')
#     else:
#         print(var * 5)
#
# checker(10)

# class BuildingError(Exception):
#     def __str__(self):
#         return f"Вы не можете строить с данным количеством материалов"
#
# def check_materials(material, limit):
#     if material > limit:
#         return  "Материалов достаточно"
#     else:
#         raise BuildingError(material)
#
# material = 200
# limit = 150
# print(check_materials(material, limit))

# |---------------------------------------------------2.0--------------------------------------------------------------|

def raise_of_the_degrees(number, max_degrees):
    i=0
    for _ in range(max_degrees):
        yield number**i
        i += 1
result = raise_of_the_degrees(1220155, 500)
print(result)
print(result.__next__())
print(result.__next__())

for _ in result:
    print(_)
    break

