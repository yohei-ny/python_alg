def linear_serach(data,value):
  for i in range(len(data)):
    if data[i] == value:
      return i
  return -1

data =[50,30,90,10,20,70,60,40,80]
print(linear_serach(data,40))
          