#!/usr/bin/python3
#SPDX-FileCopyrightText: 2022 Daiki Morita
#SPDX-License-Identifier: BSD-3-Clause

import sys

ans = 0
ans1=0

def totum(s):

            try:
                return int(s)

            except:
                return float(s)
                                                    
            ans = 0
            ans1= 0
            count=0
print('この計算では税率は10%固定とします。')

for line in sys.argv[1:]:
                                                                            ans += totum(line)
                                                                            ans1 += totum(line) * 0.1
                                                                            print('現在の値段は（', ans,'円)', end='')
                                                                            print('その内税金は->(' ,ans1, '円)')
else:
    print('//////////////////////////////////////////')

    print('合計金額は', ans, '円', '(内税金', ans1, '円)')



