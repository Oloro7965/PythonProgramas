import torch,sklearn,matplotlib
import numpy as np
lista=[[1,2,3]
       ,[4,5,6],
       [7,8,9]]
tns=torch.FloatTensor(lista)
print(tns)
print(tns.shape)
# print(type(tns))