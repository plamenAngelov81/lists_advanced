words = input().split(" ")
check_word = input()
palindrome_list = []
for word in words:
    palindrome = reversed(word)
    palindrome = "".join(palindrome)
    if palindrome == word:
        palindrome_list.append(word)

print(palindrome_list)
palindrome_count = words.count(check_word)
print(f"Found palindrome {palindrome_count} times")