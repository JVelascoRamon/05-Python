str1 = 'abc'
str2 = 'abc'
str3 = '13'

if str1 > str2:
    print ("srt1 es mayor que str2")
elif str1 == str2:
    print ("srt1 es igual que str2")
else:
    print ("srt1 es menor que str2")

word = 'banana'
count = 0
for letter in word :
    if letter == 'a' : 
       count = count + 1
print(count) # Así sabemos cuántas veces aparece la letra 'a'


#print (dir(str2))
#print (str3.isdigit())
print (str2.center(10))