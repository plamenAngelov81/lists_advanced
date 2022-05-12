to_do_notes = input().split("-")

order_list = ["" for i in range(11)]

while to_do_notes[0] != "End":

    order_list.pop(int(to_do_notes[0]))
    order_list.insert(int(to_do_notes[0]), to_do_notes[1])

    to_do_notes = input().split("-")

order_list = [x for x in order_list if x != ""]

print(order_list)