#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Hash import MD5

h = MD5.new()
h.update(b'Hello World')
print(h.hexdigest())
