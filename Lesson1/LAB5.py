#Dictionary

my_dict={"dotan":"10","roni":"20","lian":"30","idan":"40","ben":"50"}
print(my_dict)
summary=my_dict["dotan"]+my_dict["ben"]
print("The Summary is: " + str(summary))
#my_dict["yuval"]=summary
#print(my_dict)
my_dict.update({"yoel":summary})
print(my_dict)
print("Number of entries: " + str(len(my_dict)))
print("idan" in my_dict)