number_list = input().split(", ")

even_number_list = []

for i in range(len(number_list)):
    if int(number_list[i]) % 2 == 0:
        even_number_list.append(i)

print(even_number_list)
