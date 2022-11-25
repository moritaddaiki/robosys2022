#!/usr/bin/python3
#SPDX-FileCopyrightText: 2022 Daiki Morita
#SPDX-License-Identifier: BSD-3-Clause

import sys

ans = 0

def totum(s):

        try:      
            return int(s)

        except:
            return float(s)


            
        ans = 0


        for line in sys.stdin:        
            ans += totum(line)


print(ans)
