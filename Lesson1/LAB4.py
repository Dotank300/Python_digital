#lists

my_list=["Dotan koren", 29, "dotank300@gmail.com", "0526666666",]
print(my_list)
print("\n\nfull name: " + (my_list[0]) + "\nMy Age: " + str(my_list[1]) + "\nmy mail: " + (my_list[2]) + "\nmy Number is: " + (my_list[3]))

my_list2=['192.168.1.1', '192.168.1.2']
print(my_list2)

my_list2.append("192.168.1.3")
my_list2.append("192.168.1.4")
my_list2.append("192.168.1.5")
print(my_list2)

my_list2.pop(2)
print(my_list2)

print("my length is: " + str(len(my_list2)) + "\nAnd the ip lis: " + str(my_list2))


