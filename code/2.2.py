#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    r = []
    while True:
        comand = input().lower()
        if comand == "exit":
            break
        if comand == "add":
            to = input("To where? ")
            n = input("Flight id? ")
            t = input("Type of plain? ")
            rn = {
                "to": to,
                "n": n,
                "t": t
            }
            r.append(rn)
            if len(r) > 0:
                r.sort(key=lambda item: item.get("to"))
        if comand == "list":
            t1 = input("Type of plain? ")
            d = 0
            for rn in r:
                if rn.get("t") == t1:
                    print("Going to " + rn.get("to") + " With flight id " + rn.get("n"))
                    d += 1
            if d == 0:
                print("Not a type of plain or that type dosn`t servicing a flight")
