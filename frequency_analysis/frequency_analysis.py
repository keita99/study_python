#
# 頻度分析
#

string = str(input(" Please input string : "))
string = string.lower() #入力された文字を小文字化
string = string.replace(' ','') #空白を削除

print (string)

check_char = 'a'
while check_char <= 'z': 
    c = string.count(check_char)
    print(check_char, ":", c)
    check_char = chr(ord(check_char) + 1)