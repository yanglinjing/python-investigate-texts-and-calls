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
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""

phone_num = []

def counter(records, i):
    """
    Iterate the record list

    i: the 1st or 2nd row of the phone numbers
    """
    for record in records:
        if record[i] not in phone_num:
            phone_num.append(record[i])
    return phone_num

def total_num(texts, calls):
    """The total number of the phone numbers appearing in the call and text records"""
    counter(texts, 0)
    counter(texts, 1)
    counter(calls, 0)
    counter(calls, 1)
    count = len(phone_num)
    return "There are {} different telephone numbers in the records.".format(count)

print(total_num(texts, calls))
