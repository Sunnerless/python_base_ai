from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# contents = contents.rstrip()  # 删除末尾的换行符
#
# lines = contents.splitlines()
# pi_string = ''
# print(lines)
# for line in lines:
#     pi_string += line.lstrip()  # 删除左端空格
#
# print(pi_string)
# print(len(pi_string))

# path = Path('programming.txt')
# path.write_text('I love programming.')
# Python只能将字符串写⼊⽂本⽂件。如果要将数值数据存储到⽂本⽂件中，必须先使⽤函数str() 将其转换为字符串格式
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path = Path('programming.txt')
path.write_text(contents)


# 异常（exception）
try:
    print(5/0)
except ZeroDivisionError:
    print("Something went wrong")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)

# 处理 FileNotFoundError 异常

