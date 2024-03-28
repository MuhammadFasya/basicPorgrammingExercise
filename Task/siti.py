#Toko Siti
while True:
    try:
#Input your price 
        goods = str(input("Input the cosmetic you want to sell:"))
        price = float(input("Input the price you bought the cosmetic:"))
        finalPrice= price*(10/100)
        print(f"The price is: {finalPrice:,}")
        break
    except ValueError:
        print("Input Invalid")