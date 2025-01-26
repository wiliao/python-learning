def list_contain(list_data, n):
    for value in list_data:
        if n == value:
            return True
    return False
print(list_contain([3, 4, 3, 4], 4))