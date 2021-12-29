#! /usr/bin/env python3
# -*- coding: utf-8 -*-

a = b"123"
b = b"456"
new_zip = []
for i, j in zip(a, b):
    new_zip.append(i ^ j)
print(new_zip)
