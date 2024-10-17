def word_count(file_path):
    word_freq = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.lower()
            words = line.split()
            for word in words:
                if word in word_freq:
                    word_freq[word] += 1
                else:
                    word_freq[word] = 1
    return word_freq

file_path = r'c:\Users\ADMIN\Documents\PY\test.txt'  # Sử dụng raw string
result = word_count(file_path)
for word, count in result.items():
    print(f"'{word}': {count}")
