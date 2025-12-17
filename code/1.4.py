#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    d = {1: "one", 2: "two", 3: "three"}
    d_rev = {v: k for k, v in d.items()}
    print(d_rev)
