print("now we will calculate your marketing: \n................ \nTomato=3 NIS\nCucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS\n")
tomatos=int(input("Enter how many tomatos?"))
Cucumbers=int(input("Enter how many Cucumbers?"))
Colas=int(input("Enter how many Colas?"))
Chickens=int(input("Enter how many Checkens?"))


print("\nsummary of your order:\n-------------------- \ntomatos: " + str(tomatos) + "\ncucumbers: " + str(Cucumbers) + "\nColas: " + str(Colas) + "\nChickens: " + str(Chickens))

summary=(tomatos*3)+(Cucumbers*2)+(Colas*5)+(Chickens*20)
print("\nyou have to pay: " + str(summary) + " NIS without tax")
print("\nyou have to pay: " + str("%.2f" %(summary*1.17)) + " NIS with tax")