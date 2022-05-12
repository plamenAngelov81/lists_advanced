employees_happiness = list(map(int, input().split(" ")))
factor = int(input())

# employees_happiness = list(map(lambda x: x * factor, employees_happiness))

employees_happiness = [x * factor for x in employees_happiness]

average_happy = sum(employees_happiness) / len(employees_happiness)
happy_list = []

for i in employees_happiness:
    if i >= average_happy:
        happy_list.append(i)

if len(happy_list) >= len(employees_happiness) / 2:
    print(f"Score: {len(happy_list)}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_list)}/{len(employees_happiness)}. Employees are not happy!")