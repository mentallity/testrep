# Задание 1
def display_quote():
    print("\"Don't compare yourself with anyone in this world…\nif you do so, you are insulting yourself.\"\nBill Gates")

display_quote()

# Задание 2
def display_even_numbers(num1, num2):
    for num in range(num1, num2 + 1):
        if num % 2 == 0:
            print(num)

display_even_numbers(3, 10)

# Задание 3
def display_square(side_length, symbol, filled):
    if filled:
        for _ in range(side_length):
            print(symbol * side_length)
    else:
        print(symbol * side_length)
        for _ in range(side_length - 2):
            print(symbol + " " * (side_length - 2) + symbol)
        print(symbol * side_length)

display_square(5, '*', True)
display_square(5, '*', False)

# Задание 4
def min_of_five_nums(*args):
    return min(args)

min_num = min_of_five_nums(5, 3, 8, 2, 7)
print(min_num)

# Задание 5
def product_in_range(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    product = 1
    for num in range(num1, num2 + 1):
        product *= num
    return product

result = product_in_range(2, 5)
print(result)

# Задание 6
def count_digits(num):
    return len(str(num))

num_digits = count_digits(3456)
print(num_digits)

# Задание 7
def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

palindrome_check = is_palindrome(123321)
print(palindrome_check)
