def count_chars(s):
    char_count = {}
    for char in s :
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
s = "HofgNhunn"
print(count_chars(s))
            