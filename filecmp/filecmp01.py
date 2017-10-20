#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, sys
import filecmp
import re
import shutil

holderlist=[]

def compareme(dir1, dir2):             #递归获取不同的文件
    dircomp = filecmp.dircmp(dir1,dir2)
    only_in_one = dircomp.left_only    #dir1源目录新文件或目录
    diff_in_one = dircomp.diff_files   #dir1月dir2源目录不匹配文件
    dirpath=os.path.abspath(dir1)      #dir1源目录绝对路径

    #print "only_in_one: %s " % only_in_one
    #print "diff_in_one: %s " % diff_in_one
    #print "dirpath: %s " % dirpath
    #将更新文件名或目录追加到holderlist
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in only_in_one]
    [holderlist.append(os.path.abspath(os.path.join(dir1,x))) for x in diff_in_one]
    #等同于以下语句
    #for x in diff_in_one:
    #    holderlist.append(os.path.abspath(os.path.join(dir1,x)))


    #print dircomp.common_dirs

    if len(dircomp.common_dirs) > 0:
        for item in dircomp.common_dirs:
            compareme(os.path.abspath(os.path.join(dir1,item)), os.path.abspath(os.path.join(dir2,item)))
        return holderlist

#compareme("dir1","dir2")

def main():
    if len(sys.argv) > 2:
        dir1 = sys.argv[1]
        dir2 = sys.argv[2]
    else:
        print "Usage: ", "datadir backupdir"
        sys.exit()

    source_files=compareme(dir1,dir2)    #对比源目录与备份目录
    dir1=os.path.abspath(dir1)
    #print(dir1)

    if not dir2.endswith('/'): dir2=dir2+'/'   #备份目录路径加"/"
    #print(dir2)
    dir2=os.path.abspath(dir2)
    #print(dir2)

    destination_files=[]
    createdir_bool=False

    for item in source_files:
        destination_dir = re.sub(dir1, dir2, item)   #将源目录差异路径清单对应替换成备份目录
        destination_files.append(destination_dir)

        if os.path.isdir(item):    #如果差异路径为目录且不存在，则在备份目录中创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True    #再次调用compareme函数标记


    print("=========================================")
    print("##########update item:###################")
    print("source_files: %s" %source_files)
    print("destination_files: %s "%destination_files)
    copy_pair=zip(source_files, destination_files)    #将源目录与备份目录文件清单拆分成元组
    print("copy_pair: %s" %copy_pair)
    for item in copy_pair:
        if os.path.isfile(item[0]):    #判断是否为文件，是则进行复制操作
            shutil.copyfile(item[0], item[1])

if __name__ == '__main__':
    main()
