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
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以【电话号码】为键，【通话总时长】为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""

phone_num = {}

def counter(records, i):
    """
    Iterate the record list

    i: 0 or 1, meansthe 1st or 2nd row of the phone numbers
    record[3]: the time of the call[i]
    """
    for record in records:
        if record[i] not in phone_num:
            phone_num[record[i]] = int(record[3])
        else:
            phone_num[record[i]] += int(record[3])
    return phone_num

def longest_call_num(calls):
    """Find the number of which the total call time is the longest"""

    counter(calls, 0)
    counter(calls, 1)

    #min(d.items(), key=lambda x: x[1])
    longest_call = max(phone_num.items(), key=lambda x: x[1])

    return "{} spent the longest time, {} seconds, on the phone during September 2016.".format(longest_call[0], longest_call[1])

print(longest_call_num(calls))
