#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# 第一天，学习使用 pytorch

import torch
import numpy as np

t1 = torch.tensor([1, 2, 3])
array1 = np.arange(12).reshape(3, 4)
c = torch.rand([3,4])

print(t1, '\n', array1, c)
