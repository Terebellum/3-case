#!/usr/bin/env python3
# -*- encoding: utf-8
if __name__ == "__main__":
    p = int(input())
    d = True
    for i in range(2, int(p**0.5)+1):
        if (p % i == 0):
            d = False
    print(int(d))
