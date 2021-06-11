# import math

# def get_num(not_value):
#   if not_value <=1:
#     return False
#   for i in range(2,int(math.sqrt(not_value))+1):
#     if not_value % i ==0:
#       return False
#   return True

# for i in range(200):
#   if get_num(i):
#     print(i)

import math

def get_num(value):
  if value <0:
    return []
  prime=[2]
  limit =int(math.sqrt(value))


  ## 奇数の作成を行なっていく
  data =[i +1 for i in range(2,value,2)]
  print(data)
  while limit >data[0]:
    prime.append(data[0])
    # データの入れ替えを行う
    data =[j for j in data if j %data[0]!=0]
  return prime + data

print(get_num(200))
