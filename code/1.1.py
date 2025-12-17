#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    s = input().lower()
    v = set('аеёиоуыэюя')
    print(sum(c in v for c in s))
