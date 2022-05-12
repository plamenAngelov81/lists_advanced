names_list = input().split(", ")

sorted_names = sorted(names_list)
sorted_names = sorted(sorted_names, key=lambda name: -len(name))

second_sort_names = sorted(names_list, key=lambda name: (-len(name), name))

print(sorted_names)
print(second_sort_names)
