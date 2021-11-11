#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from Crypto.Hash import SHA256

h = SHA256.new()
h.update(b'Hello World')
print(h.hexdigest())
