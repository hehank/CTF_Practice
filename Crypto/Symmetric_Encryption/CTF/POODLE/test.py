#! /usr/bin/env python3
# -*- coding: utf-8 -*-

a = "12345678"
a_new = []
for i in range(0, len(a), 3):
    a_new.append([a[i:i+3]])
print(a_new)
