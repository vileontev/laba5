def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

my_list = [10, 20, 30, 20, 40, 50, 10, 30, 60]

# Находим повторяющиеся элементы
duplicate_values = find_duplicates(my_list)

# Выводим повторяющиеся элементы при их наличии
if duplicate_values:
    print("Повторяющиеся элементы в списке:", duplicate_values)
else:
    print("В списке нет повторяющихся элементов.")
