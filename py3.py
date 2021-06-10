import math

def get_num(not_value):
  if not_value <=1:
    return False
  for i in range(2,int(math.sqrt(not_value))+1):
    if not_value % i ==0:
      return False
  return True

for i in range(200):
  if get_num(i):
    print(i)