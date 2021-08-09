import os,sys
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
    
