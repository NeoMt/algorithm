# !/usr/bin/env python 
# -*- coding:utf-8 -*- 
# Author: NeoMT<matengneo@gmail.com>
#
# 未知长度序列等概率采样
# 某时间节点下，采样序列长度为n，需采样结果数为m
# 按以下策略采样，能够保证元素采样概率相等，且为m/n
#   1. 若m >= n, 则将当前元素保存到结果序列；
#   2. 若m < n, 则以m/n的概率选择是否保留当前元素，
#      若采样当前元素，且随机从结果序列中选取一个元素进行替换

import random

# 输入sequence长度未知，m为需要采样的数据个数
def random_pick(m, sequence):
  result = []
  i = 0
  while True:
    try:
      current_num = sequence[i]
      if i < m:
        result.append(current_num)
      else:
        j = random.randint(0, i)
        if j < m:
          result[j] = current_num
      i = i + 1
    except IndexError:
      print "End of Sequence, Sequence num:", i
      return result

if __name__ == '__main__':
  sequence = [x for x in range(0, 11)]
  print random_pick(10, sequence)