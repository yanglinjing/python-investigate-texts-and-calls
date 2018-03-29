"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务3:
(080)是【班加罗尔】的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被【班加罗尔bangalore】地区的【固定电话】【所拨打的】所有电话的【区号】和【移动前缀】（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以【 0 打头】。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的【前四个
   数字】，并且以【7,8或9开头】。
 - 电话促销员的号码没有括号或空格 , 但以【140开头】。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。
"""

phone_list = []

def whether_in_list(call):
    if call not in phone_list:
        phone_list.append(call)
    return phone_list


def area(call):
    area_code = []
    for i in range(len(call)):
        if call[i] != ")":
            area_code.append(call[i])
        else:
            break
    code_str = "".join(area_code[1:])
    return code_str


def calls_from_blr(calls):
    for call in calls:
        if call[0][:5] == "(080)":
            if call[1][0] =="7" or call[1][0] =="8" or call[1][0] =="9":
                whether_in_list(call[1][:4])
            elif call[1][0] == "(":
                whether_in_list(area(call[1]))

    ordered_phone_list = "\n" + "\n".join(sorted(phone_list))
    return "The numbers called by people in Bangalore have codes:{}".format(ordered_phone_list)

print(calls_from_blr(calls))


"""
第二部分: 由【班加罗尔】【固话】打往【班加罗尔】的电话所占比例是多少？
换句话说，所有由【（080）开头】的号码拨出的通话中，
打往由【（080）开头】的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""

def percentage(calls):

    rate_080 = (1 / len(calls_from_blr(calls))) * 100
    percentage_080 = round(rate_080, 2)

    return "{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage_080)

print(percentage(calls))
