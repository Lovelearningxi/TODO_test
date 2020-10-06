#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 17:01
# @Author  : WangXi
# @Site    : 
# @File    : test.py
# @Software: PyCharm



#testfile NO use




from config import *

db = SQlManager()
db1 = db.get_list('select todo_id from TODOS')
db2 = db.get_list('select task from TODOS')
db.close()
res1 = [item[key] for item in db1 for key in item]
res2 = [item[key] for item in db2 for key in item]
print(res1)
dic = dict(map(lambda x,y:[x,y],res1,db2))

db.moddify('insert into TODOS (todo_id,task) values({},{});'.format(task_id, TODOS[todo_id]))
db.moddify('delete from TODOS where todo_id = {}'.format())

db.moddify('update TODOS set todo_id="{}",task="{}" where todo_id=:"{}";'.format())
print(dic)
# for item in db1:
#    for key in item:
#       print(item[key])
#
#
#
# def abort_if_todo_doesnt_exist(todo_id):
#     if todo_id not in res1:
#         print('X')
#     else:
#         print('yes')
#
#
# todo_id = 'todo3'
# abort_if_todo_doesnt_exist(todo_id)
