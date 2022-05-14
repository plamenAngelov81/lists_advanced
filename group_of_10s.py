number_list = list(map(int, input().split(", ")))

group = 10

while True:
    if len(number_list) == 0:
        break

    current_list = [x for x in number_list if x <= group]

    for y in current_list:
        number_list.remove(y)

    print(f"Group of {group}'s: {current_list}")
    group += 10
