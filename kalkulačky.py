opakovat = "ano"
while opakovat == "ano":
    čísloJedna = int(input("Zadejte číslo: "))
    znamínko = input("Zadejte znamínko: ")
    čísloDva = int(input("Zadejte druhé číslo: "))
    if znamínko == "+":
        print(čísloJedna + čísloDva)
    elif znamínko == "-":
        print(čísloJedna - čísloDva)
    elif znamínko == "*":
        print(čísloJedna * čísloDva)
    elif znamínko == "/":
        print(čísloJedna / čísloDva)
    else:
        print("neplatné znamínko")
    opakovat = input("chcete z opakovat: ")