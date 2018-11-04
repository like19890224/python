import pickle
# shop_data = ['apple','eggs','banana',]
# with open('/tmp/mylist','wb') as fobj:
#     pickle.dump(shop_data,fobj)
#
with open('/tmp/mylist','rb') as fobj:
    mylist = pickle.load(fobj)
print(mylist[0],mylist[1],mylist[2])
