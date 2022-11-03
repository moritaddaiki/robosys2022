#!/bin/bash -xv 
#SPDX-FileCopyrightText: 2022 Daiki Morita
#iSPDX-License-Identifier: BSD-3-Clause

ng () {
	echo NG at Line $1
        res=1
}

res=0
+ res=0

### I/0 test ###
out=$(seq 5 | ./plus.py)
++ seq 5
++ ./plus.py
+ out=15
[ "${out}" = 15 ] || ng ${LINENO}
+ '[' 15 = 15 ']'

[ "$res" = 0 ] && echo OK
+ '[' 0 = 0 ']'
  + echo OK
    OK
      exit $res
        + exit 0
exit $res
