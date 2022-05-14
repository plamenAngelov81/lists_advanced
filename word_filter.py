fruits = input().split(" ")

result = [x for x in fruits if len(x) % 2 == 0]

for i in result:
    print(i)

# друга верси за принтиране;
# print("\n".join(result))
