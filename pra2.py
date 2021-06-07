recive_price =int(input("金額を入力してください"))
sum_price =int(input("商品金額を入力してください"))
charge =recive_price - sum_price
rm_charge =recive_price - sum_price
lists=[]
# if rm_charge>5:
lists.append(charge//5000)
rm_charge =(charge%5000)

lists.append(rm_charge//1000)
rm_charge=(rm_charge%1000)
# sm5=(charge//5000)
lists.append(rm_charge//500)
rm_charge=(rm_charge%500)

lists.append(rm_charge//100)
rm_charge=(rm_charge%100)

lists.append(rm_charge//50)
rm_charge=(rm_charge%50)

lists.append(rm_charge//10)
rm_charge=(rm_charge%10)

lists.append(rm_charge//5)
rm_charge=(rm_charge%5)

lists.append(rm_charge)
# print("お釣りは{}円です,枚数は{},残りは{}です".format(charge,sm5,rm_charge))
# for i in len(lists):
print("5000:",lists[0])
print("1000:",lists[1])
print("500:",lists[2])
print("100:",lists[3])
print("50:",lists[4])
print("10:",lists[5])
print("5:",lists[6])
print("1:",lists[7])
