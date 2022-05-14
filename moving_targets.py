targets = list(map(int, input().split(" ")))

command = input().split()

while True:
    if command[0] == "End":
        break

    if command[0] == "Shoot":
        index = int(command[1])
        power = int(command[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif command[0] == "Add":
        add_index = int(command[1])
        value = int(command[2])
        if 0 <= add_index < len(targets):
            targets.insert(add_index, value)
        else:
            print("Invalid placement!")

    elif command[0] == "Strike":
        strike_index = int(command[1])
        radius = int(command[2])
        left_strike = strike_index - radius
        right_strike = strike_index + radius
        if 0 <= left_strike and right_strike < len(targets):
            targets = targets[0: left_strike] + targets[right_strike + 1::]
        else:
            print("Strike missed!")
    command = input().split()

result = [str(target) for target in targets]

print("|".join(result))
