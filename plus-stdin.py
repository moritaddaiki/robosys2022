#!/usr/bin/python3
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
