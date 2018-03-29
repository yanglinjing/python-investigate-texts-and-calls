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

def count_number(textfile,callfile):
    #使用set这种天然去重的数据结构进行计算
    target= set()
    for ele1 in textfile:
        target.add(ele1[0])
        target.add(ele1[1])
    for ele2 in callfile:
        target.add(ele2[0])
        target.add(ele2[1])
    return len(target)

print("There are {} different telephone numbers in the records.".format(count_number(texts,calls)))

"""
第二次写的，第一行没问题，第二行出现unhashable的错误
phone_num = [[text[0], text[1]] for text in texts] + [[call[0], call[1]] for call in calls]
print("There are " + len(set(phone_num)) + "different telephone numbers in the records.")
"""

"""
我第一次写的，结果正确
def counter(records, i):
    for record in records:
        if record[i] not in phone_num:
            phone_num.append(record[i])
    return phone_num

def total_num(texts, calls):
    counter(texts, 0)
    counter(texts, 1)
    counter(calls, 0)
    counter(calls, 1)
    count = len(phone_num)
    return "There are {} different telephone numbers in the records.".format(count)

print(total_num(texts, calls))
"""
