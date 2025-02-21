# todo: Преобразуйте переменную age и foo в число
age = "23"
foo = "23abc"
# int(foo) value error
print ("1 ", int(age))

# Преобразуйте переменную age в Boolean
age = "123abc"
print ("2 ",bool(age))

# Преобразуйте переменную flag в Boolean
flag = 1
print ("3 ",bool(flag))

# Преобразуйте значение в Boolean
str_one = "Privet"
str_two = ""
bool(str_one)
bool(str_two)
print ("4 ",bool(str_one))
print ("5 ",bool(str_two))

# Преобразуйте значение 0 и 1 в Boolean
a=0
b=1
print ("6 ",bool(a))
print ("7 ",bool(b))

# Преобразуйте False в строку
f=False
print ("8 ",str(f))