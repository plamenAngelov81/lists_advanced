inventory = input().split(", ")

command = input().split(" - ")

while True:
    if command[0] == "Craft!":
        break

    if command[0] == "Collect":
        collect_item = command[1]
        if collect_item not in inventory:
            inventory.append(collect_item)

    elif command[0] == "Drop":
        drop_item = command[1]
        if drop_item in inventory:
            inventory.remove(drop_item)

    elif command[0] == "Combine Items":
        combine = command[1]
        old_new = combine.split(":")
        old_item = old_new[0]
        new_item = old_new[1]
        if old_item in inventory:
            inventory.insert(inventory.index(old_item) + 1, new_item)

    elif command[0] == "Renew":
        renew_item = command[1]
        if renew_item in inventory:
            inventory.remove(renew_item)
            inventory.append(renew_item)

    command = input().split(" - ")

print(", ".join(inventory))
