string = str(input(" Please input string : "))

check_char = 'a'
while check_char <= 'z': 
    c = string.count(check_char)
    print(check_char, " : ", c)
    check_char = chr(ord(check_char) + 1)