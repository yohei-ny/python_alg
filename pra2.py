bool =True
while bool ==True:
  recive_price =int(input("金額を入力してください"))
  sum_price =int(input("商品金額を入力してください"))
  rm_charge =recive_price - sum_price
  if recive_price <0 or sum_price<0 or rm_charge<0:
    print("再度入力してください")
    continue
  charge =rm_charge
  bool =False
lists =[]

price =[5000,1000,500,100,50,10,5,1]

for i ,x in enumerate(price):
  lists.append(rm_charge//x)
  rm_charge =(rm_charge%x)
  print(x,"の枚数が",lists[i])
print("お釣りは{}".format(charge))
