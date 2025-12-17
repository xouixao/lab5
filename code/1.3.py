#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    school = {"1A": 25, "1B": 23, "2A": 27, "2B": 26}
    school["1A"] = 26
    school["3A"] = 20
    del school["2B"]
    print(sum(school.values()))
    