"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    #print(texts) [[记录1],[记录2],。。。]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务0:
【短信】 记录的【第一条】记录是什么？【通话】 记录【最后一条】记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def first_text_record():
    """Print the first record of the text records"""
    incoming_number = texts[0][0]
    answering_number = texts[0][1]
    time = texts[0][2]
    return "First record of texts, {} texts {} at time {}".format(incoming_number, answering_number, time)
print(first_text_record())

def last_call_record():
    """Print the last record of the call records"""
    incoming_number = calls[0][0]
    answering_number = calls[0][1]
    time = calls[0][2]
    during = calls[0][3]
    return "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming_number, answering_number, time, during)
print(last_call_record())
