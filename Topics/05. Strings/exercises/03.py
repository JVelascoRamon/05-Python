
def count_letters (letter , s):
    result = 0
    for char in s:
        if char == letter:
            result += 1
    return result

fruit = "banana"
char = "a"

print (count_letters (char , fruit))