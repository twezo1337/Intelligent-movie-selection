def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[slice(1, -1)])
        else:
            return False

a = str(input("Введите строку:"))
if (is_palindrome(a) == True):
    print("Данная строка палиндром!")
else:
    print("Данная строка не палиндром!")

def palindrome_check(s):
    # Цикл не закончится, пока не закончится строка делённая напополам
    for i in range(0, int(len(s)/2)):
        # Если элементы не совпали, то строка не является палиндромом
        if s[i] != s[len(s)-i-1]:
            return "Строка не является палиндромом"
    # Если все элементы совпали, то строка является палиндромом
    return "Строка является палиндромом"

# Ввод проверяемой строки
s = input("Введите строку: ")
# Вызов функции с передачей введённой строки в параметр s
print(palindrome_check(s))


