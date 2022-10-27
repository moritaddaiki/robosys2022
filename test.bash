#!/bin/bash
#SPDX-FileCopyrightText: 2022 Daiki Morita
#SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo NG at Line $1

	res=1

}

res=0

### I/0 test ###

out=$(seq 5 | ./plus.py)

[ "${out}" = 14 ] || ng ${LINENO}

[ "$res" = 0 ] && echo OK

exit $res
