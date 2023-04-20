
def remove_letter (letter , s):
    result = ""
    index = 0
    for i in s :
        if i == letter : 
            continue
        else:
            result = result + i
        index = index + 1
    print (result)
    return result

assert(remove_letter("a", "apple") == "pple")
assert(remove_letter("a", "banana") == "bnn")
assert(remove_letter("z", "banana") == "banana")
assert(remove_letter("i", "Mississippi") == "Msssspp")
assert(remove_letter("b", "") == "")
assert(remove_letter("b", "c") == "c")