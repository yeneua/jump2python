# 프롬프트에서 명령어 사용 -> 인수를 전달해줌(함수처럼!!)

import sys

args = sys.argv[1:]
for i in args:
    # print(i)
    print(i.upper(), end=' ')