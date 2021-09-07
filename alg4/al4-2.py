# def linear_serach(data,value):
#   for i in range(len(data)):
#     if data[i] == value:
#       return i
#   return -1

# data =[50,30,90,10,20,70,60,40,80]
# print(linear_serach(data,40))
          

## 

import math
def is_prime(num):
 if num <=1:
   return False
 for i in range(2,int(math.sqrt(num)+1)):
    if num % i ==0:
      return False
 return True
for i in range(200):
  if is_prime(i):
    print(i)

from pandas import Series,DataFrame
import pandas as pd
attri_detail ={"ID":["1","2","3","4","5"],
              "Sex":["F","F","M","M","F"],
              "Money":[1000,2000,500,300,700],
              "Name":["Saito","Horie","Kondo","Kawada","Matsubara"]}
attri_detail_frame =DataFrame(attri_detail)
print(attri_detail)