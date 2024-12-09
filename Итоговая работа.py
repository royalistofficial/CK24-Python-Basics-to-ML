#!/usr/bin/env python
# coding: utf-8

# # Конторальная работа

# ## Порядок сдачи

# Каждое задание оценивается в 10 баллов. Код нужно отправить напрямую в СДО как текст. Перед сдачей проверьте код, напишите тесты. Не забудьте про `PEP8`, например, с помощью `flake8`.
# 
# Дедлайн - 9 декабря 10:00

# ## Разворот строки

# Напишите функцию, которая принимает строку в качестве входного параметра и возвращает новую строку, в которой символы исходной строки расположены в обратном порядке.

# In[174]:


def reverse_string(s):
    return s[::-1]

assert reverse_string("hello") == "olleh", "Тест 1 не пройден"
assert reverse_string("Привет") == "тевирП", "Тест 2 не пройден"
assert reverse_string("12345") == "54321", "Тест 3 не пройден"
assert reverse_string("") == "", "Тест 4 не пройден"
assert reverse_string("a") == "a", "Тест 5 не пройден"
assert reverse_string("racecar") == "racecar", "Тест 6 не пройден"

print(reverse_string("hello"))    # Вывод: "olleh"
print(reverse_string("Привет"))   # Вывод: "тевирП"
print(reverse_string("12345"))    # Вывод: "54321"


# # Ромб

# Напишите функцию, которая выводит на экран ромб, составленный из символов звёздочек `*`. Размер ромба определяется введённым пользователем нечётным числом n, которое задаёт ширину (и высоту) ромба в его самой широкой части.

# In[175]:


def draw(n):
    upper_height = n // 2
    lower_height = n - upper_height

    for i in range(upper_height):
        spaces = ' ' * (upper_height - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

    for i in range(lower_height):
        spaces = ' ' * (i)
        stars = '*' * (2 * (lower_height - i) - 1)
        print(spaces + stars)


print(draw(7))
#   *
#  ***
# *****
#*******
# *****
#  ***
#   *


# # НОД

# Напишите функцию, которая вычисляет наибольший общий делитель (НОД) двух целых чисел.

# In[176]:


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

assert gcd(48, 18) == 6, "Тест 1 не пройден"
assert gcd(100, 25) == 25, "Тест 2 не пройден"
assert gcd(17, 13) == 1, "Тест 3 не пройден"
assert gcd(0, 5) == 5, "Тест 4 не пройден" 
assert gcd(5, 0) == 5, "Тест 5 не пройден"  
assert gcd(0, 0) == 0, "Тест 6 не пройден"

print(gcd(48, 18))   # Вывод: 6
print(gcd(100, 25))  # Вывод: 25
print(gcd(17, 13))   # Вывод: 1


# # Система счисления

# Напишите функцию, которая принимает строковое представление числа в произвольной системе (макс. 36) счисления и его основание, и возвращает это число в десятичной системе счисления.

# In[177]:


def convert_to_decimal(number_str, base):
    return int(number_str, base)

assert convert_to_decimal("1010", 2) == 10, "Тест 1 не пройден"
assert convert_to_decimal("1A", 16) == 26, "Тест 2 не пройден"
assert convert_to_decimal("123", 8) == 83, "Тест 3 не пройден"
assert convert_to_decimal("Z", 36) == 35, "Тест 4 не пройден"
assert convert_to_decimal("10", 10) == 10, "Тест 5 не пройден" 
assert convert_to_decimal("FF", 16) == 255, "Тест 6 не пройден"  
assert convert_to_decimal("7B", 16) == 123, "Тест 7 не пройден" 

print(convert_to_decimal("1010", 2))    # Вывод: 10
print(convert_to_decimal("1A", 16))     # Вывод: 26
print(convert_to_decimal("123", 8))     # Вывод: 83
print(convert_to_decimal("Z", 36))      # Вывод: 35


# # Палиндром

# Напишите функцию, которая проверяет, является ли заданная строка палиндромом.

# In[178]:


def is_palindrome(s):
    return s == s[::-1]

assert is_palindrome("мадам") == True, "Тест 1 не пройден"
assert is_palindrome("топот") == True, "Тест 2 не пройден"
assert is_palindrome("привет") == False, "Тест 3 не пройден"
assert is_palindrome("12321") == True, "Тест 5 не пройден" 
assert is_palindrome("12345") == False, "Тест 6 не пройден" 
assert is_palindrome("") == True, "Тест 7 не пройден"

print(is_palindrome("мадам"))                  # Вывод: True
print(is_palindrome("топот"))                  # Вывод: True
print(is_palindrome("привет"))                 # Вывод: False


# # k порядковая статистика

# Напишите функцию, которая принимает массив чисел и целое число $k$, и вычисляет количество элементов в массиве, которые больше, чем элемент, находящийся на позиции $k$ в упорядоченном по возрастанию массиве (т.е. больше, чем $k$-я порядковая статистика).

# In[179]:


def count_greater_than_kth(arr, k):
    if not arr:
        return 0
    sort_arr = sorted(arr)
    i = k
    while i < len(sort_arr) and sort_arr[i] == sort_arr[k-1]:
        i += 1
    return len(sort_arr) - i


assert count_greater_than_kth([5, 3, 8, 6, 2], 3) == 2, "Тест 1 не пройден"  
assert count_greater_than_kth([1, 2, 3, 4, 5], 2) == 3, "Тест 2 не пройден"  
assert count_greater_than_kth([10, 20, 30, 40, 50], 1) == 4, "Тест 3 не пройден" 
assert count_greater_than_kth([5, 5, 5, 5, 5], 3) == 0, "Тест 4 не пройден" 
assert count_greater_than_kth([1, 2, 3, 4, 5], 5) == 0, "Тест 5 не пройден" 
assert count_greater_than_kth([], 1) == 0, "Тест 6 не пройден"

arr = [5, 3, 8, 6, 2]
k = 3
result = count_greater_than_kth(arr, k)
print(result)  # Вывод: 2


# # Уникальные подстроки

# Напишите функцию, которая принимает строку и целое число k, и подсчитывает количество уникальных подстрок длины k в этом тексте.

# In[180]:


def count_unique_substrings(text, k):
    substrings_set = set()
    for i in range(len(text)-k+1):
        substrings_set.add(text[i:i+k])
    return len(substrings_set)

assert count_unique_substrings("abcabc", 3) == 3, "Тест 1 не пройден"  # "abc", "bca", "cab"
assert count_unique_substrings("aaaaa", 1) == 1, "Тест 2 не пройден"  # "a"
assert count_unique_substrings("hello", 2) == 4, "Тест 3 не пройден"  # "he", "el", "ll", "lo"
assert count_unique_substrings("abcdef", 3) == 4, "Тест 4 не пройден"  # "abc", "bcd", "cde", "def"
assert count_unique_substrings("abcabc", 4) == 3, "Тест 5 не пройден"  # "abca", "bcab", "cabc"
assert count_unique_substrings("", 1) == 0, "Тест 6 не пройден"  # Пустая строка
assert count_unique_substrings("abc", 4) == 0, "Тест 7 не пройден"  # k больше длины строки

text = "abcabc"
k = 3
result = count_unique_substrings(text, k)
print(result)  # Вывод: 3


# # Минимум

# Напишите функцию, которая для заданного целого числа N находит такие целые положительные числа $a, b, c$, что произведение $a * b * c = N$, и сумма $a + b + c$ минимальна.

# In[181]:


def minimum(n):
    def helper(n):
        min_sum = float('inf')
        result = (None, None)
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                if i + n // i < min_sum:
                    min_sum = i + n // i
                    result = (i, n // i)
        return min_sum, result
    
    min_sum_3 = float('inf')
    result = (None, None, None)
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            min_sum_2, (k2, k3) = helper(n // i)
            if i + min_sum_2 < min_sum_3:
                min_sum_3 = i + min_sum_2
                result = (i, k2, k3)

    return result

assert minimum(12) == (2, 2, 3), "Тест 1 не пройден" 
assert minimum(27) == (3, 3, 3), "Тест 2 не пройден" 
assert minimum(7) == (1, 1, 7), "Тест 3 не пройден" 
assert minimum(1) == (1, 1, 1), "Тест 4 не пройден"  
assert minimum(100) == (4, 5, 5), "Тест 5 не пройден"


print(minimum(12))                  # Вывод: 2, 2, 3
print(minimum(27))                  # Вывод: 3, 3, 3
print(minimum(7))                   # Вывод: 1, 1, 7


# # Определитель

# Напишите функцию, которая вычисляет определитель заданной квадратной матрицы.

# In[182]:


def create_submatrix(matrix, c):
    submatrix = []
    for row_index in range(1, len(matrix)): 
        row = []
        for col_index in range(len(matrix[row_index])):
            if col_index != c: 
                row.append(matrix[row_index][col_index])
        submatrix.append(row)
    return submatrix

def determinant(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        raise ValueError("Матрица должна быть квадратной")
    
    if len(matrix) == 1:
        return matrix[0][0]

    det = 0
    for c in range(len(matrix)):
        submatrix = create_submatrix(matrix, c)
        det += ((-1) ** c) * matrix[0][c] * determinant(submatrix)

    return det


assert determinant([[1, 2], [3, 4]]) == -2, "Тест 1 не пройден" 
assert determinant([[5]]) == 5, "Тест 2 не пройден" 
assert determinant([[1, 2], [2, 1]]) == -3, "Тест 3 не пройден" 
assert determinant([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 1, "Тест 4 не пройден" 
assert determinant([[2, 3], [1, 4]]) == 5, "Тест 5 не пройден"
assert determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 0, "Тест 6 не пройден"

matrix = [
    [1, 2],
    [3, 4]
]
result = determinant(matrix)
print(result)  # Вывод: -2


# # Скобочная последовательность

# Напишите функцию, которая проверяет правильность скобочной последовательности в заданной строке. Последовательность считается правильной, если все открывающиеся скобки корректно закрываются соответствующими закрывающими скобками в правильном порядке.

# In[183]:


def is_valid_sequence(s):
        i = 1
        counter = 1
        while i < len(s):
            if s[i] == s[0]:
                counter += 1
            elif s[0] == '(' and s[i] == ')' or s[0] == '[' and s[i] == ']' or s[0] == '{' and s[i] == '}':
                counter -= 1
                if counter == 0:
                    if is_valid_sequence(s[1:i]):
                        s = s[i+1:]
                        i = 0
                        counter = 1
                    else:
                        return False

            i += 1
        if s == "":
            return True
        return False


assert is_valid_sequence("({[]})") == True, "Тест 1 не пройден"  
assert is_valid_sequence("()") == True, "Тест 2 не пройден"      
assert is_valid_sequence("([])") == True, "Тест 3 не пройден"   
assert is_valid_sequence("{[()]}") == True, "Тест 4 не пройден"  
assert is_valid_sequence("{[(])}") == False, "Тест 5 не пройден"  
assert is_valid_sequence("((()))") == True, "Тест 6 не пройден"   
assert is_valid_sequence(")(") == False, "Тест 7 не пройден"     
assert is_valid_sequence("") == True, "Тест 8 не пройден"      

s = "({[]})"
result = is_valid_sequence(s)
print(result)  # Вывод: True

