current_version = input().split(".")
result = ""
for i in current_version:
    result += i

next_version = int(result) + 1

new_version = str(next_version)

print(".".join(new_version))

