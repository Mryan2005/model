import os,sys
print("1.现写现用\n2.TXT转xml")
choose=input("请选择(输入数字)：")
if choose == '1':
    event=["sentence","source","author","type","usage_first","usage_second","history"]
    sql_file = open('./Excerpt.xml','w')
    sql_file.write('<?xml version="1.0" standalone="yes"?>\n<DocumentElement>\n')
    while True:
        time_null = 0
        sql_file.write("  <sentences>\n")
        for i in event:
            c = input(i+":")
            print("    <"+i+">"+c+"</"+i+">")
            sql_file.write("    <"+i+">"+c+"</"+i+">\n")
            if c == "":
                time_null = time_null + 1
                print('null')
        if time_null == 4 or time_null > 4:
            sql_file.write("  </sentences>\n")
            sql_file.write("</DocumentElement>")
            break
elif choose == '2':
    x=[]
    project = ""
    file = input("请输入文件名（请将文件放在当前目录下）：")
    sql_file = open('./'+file,'r')
    c = sql_file.read()
    for i in c:
        if i == '\n' or i == '|':
            x.append(project)
            project = ""
        else:
            project = project + i
    for i in x:
        print(i)
