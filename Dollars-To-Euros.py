Continue = "yes"
while Continue == "yes":
    dollar = float(input("How many dollars do you want to convert to Euros? "))
    euro = dollar * .94540
    print(str("$") , dollar, (str("is")),euro,str("Euros") )
    Continue = str.lower(input("Would you Like to convert again? "))
