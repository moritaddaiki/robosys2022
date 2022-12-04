#!/usr/bin/python3
#SPDX-FileCopyrightText: 2022 Daiki Morita
#SPDX-License-Identifier: BSD-3-Clause


import sys

def totum(s):
    try:
        return int(s)
    except:
        return float(s)


    
ans = 0
for line in sys.stdin:
    line = line .rstrip()
    ans += totum(line)

print(ans)
