number = int(input())

distribution_list = []

counter = 1

while True:
    electrons = 2 * (counter ** 2)
    if electrons < number:
        distribution_list.append(electrons)
        number -= electrons
    else:
        distribution_list.append(number)
        break

    counter += 1


print(distribution_list)
