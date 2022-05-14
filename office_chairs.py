rooms = int(input())
free_chairs = 0
game_on_condition = True
for room in range(1, rooms + 1):
    event = input().split(" ")
    chairs = event[0]
    visitors = int(event[1])
    if len(chairs) < visitors:
        game_on_condition = False
        diff = abs(len(chairs) - visitors)
        print(f"{diff} more chairs needed in room {room}")
    else:
        diff = abs(len(chairs) - visitors)
        free_chairs += diff

if game_on_condition:
    print(f"Game On, {free_chairs} free chairs left")
