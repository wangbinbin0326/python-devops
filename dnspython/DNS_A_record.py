#!/usr/bin/env python
#-*- coding:utf-8 -*-
import dns.resolver

domain = raw_input('Please input an dns domain: ')
A = dns.resolver.query(domain, 'A')

for i in A.response.answer:
    for j in i.items: # items 得到一组键值对列表
        print j
