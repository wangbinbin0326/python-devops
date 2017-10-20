#!/usr/bin/env python
#-*- coding:utf-8 -*-
import difflib

text1 = """aThisisline1
"""

text1_lines = text1.splitlines()    #以行进行分隔，以便进行对比

text2 = """abThisisline2
"""

text2_lines = text2.splitlines()

#生成美观的对比HTML格式文档
d = difflib.HtmlDiff()
print d.make_file(text1_lines, text2_lines)
