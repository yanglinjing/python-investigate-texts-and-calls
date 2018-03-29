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
任务4:
电话公司希望辨认出可能正在用于进行【电话推销】的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人【拨出电话】，
但从来【不发短信】、【接收短信】或是【收到来电】


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""
phone_list = []

def ever_done(records, i):
    for record in records:
        if record[i] not in phone_list:
            phone_list.append(record[i])
    return phone_list

def sales(texts, calls):
    ever_done(texts, 0)
    ever_done(texts, 1)
    ever_done(calls, 1)

    sales_num = []

    for call in calls:
        if (call[0] not in phone_list) and (call[0] not in sales_num):
            sales_num.append(call[0])

    ordered_sales_num = "\n" + "\n".join(sorted(sales_num))
    return "These numbers could be telemarketers:{}".format(ordered_sales_num)

print(sales(texts, calls))
