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

#使用set数据类型，这种数据天然带有去重功能

#创建最后结果和需要移除的变量
result = set()
remove = set()

#遍历calls列表
for call in calls:
    result.add(call[0])
    remove.add(call[1])

#遍历texts列表
for text in texts:
    remove.add(text[0])
    remove.add(text[1])
#进行条件筛选
result = result - remove

print("These numbers could be telemarketers: "+ "\n" + "\n".join(sorted(result)))
