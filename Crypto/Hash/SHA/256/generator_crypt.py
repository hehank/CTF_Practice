#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())
digest.update(b"Hello World")
out = digest.finalize().hex()
print(out)
