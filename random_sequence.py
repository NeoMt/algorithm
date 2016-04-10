# !/usr/bin/env python 
# -*- coding:utf-8 -*- 
# Author: NeoMT<matengneo@gmail.com>
#
# 非重复随机序列生成算法
# 给定整数N，求一整型序列，该序列包含N个整数(0到N-1)，呈随机分布状态，且不重复。
#
# 解法：

import random

def random_sequence(N):
  sequence = [x for x in range(0, N)]  # origin sequence
  for i in range(0, N):
    r = random.randint(i, N - 1)
    a = sequence[i]
    sequence[i] = sequence[r]
    sequence[r] = a
  return sequence

if __name__ == '__main__':
  print random_sequence(10)