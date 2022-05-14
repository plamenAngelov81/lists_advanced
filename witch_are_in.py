strings = input().split(", ")

sentence = input()

result = [x for x in strings if x in sentence]

print(result)