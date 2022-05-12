num = int(input())

train = [0 for i in range(num)]

event = input().split(" ")

while event[0] != "End":

    if event[0] == "add":
        train[len(train) - 1] += int(event[1])         # train[-1] += int(event[1])

    elif event[0] == "insert":
        train[int(event[1])] += int(event[2])

    elif event[0] == "leave":
        train[int(event[1])] -= int(event[2])

    event = input().split(" ")
print(train)
