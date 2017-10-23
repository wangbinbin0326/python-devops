#!/usr/bin/env python
#-*- coding:utf-8 -*-
import difflib

text1 = """This is line1
This is line2
This is line3
This is line4
"""

text1_lines = text1.splitlines()    #以行进行分隔，以便进行对比

text2 = """This is line2
This is line2
This is line4
This is line4
"""

text2_lines = text2.splitlines()

#普通格式
#d = difflib.Differ()    #创建Differ()对象
#diff = d.compare(text1_lines, text2_lines)    #采用compare方法对字符串进行比较
#print '\n'.join(list(diff))

#生成美观的对比HTML格式文档
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
