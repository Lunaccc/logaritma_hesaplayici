def log_calculator():
    print("İşlem yapmak istediğiniz iki logaritmayı girin:")
    base1 = float(input("1. logaritmanın tabanını girin: "))
    num1 = float(input("1. logaritmanın sayısını girin: "))
    base2 = float(input("2. logaritmanın tabanını girin: "))
    num2 = float(input("2. logaritmanın sayısını girin: "))

    print("Yapmak istediğiniz işlemi seçin:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")

    choice = int(input("Seçiminiz (1/2/3/4): "))

    if choice == 1:
        result = num1/num2 + (base1/base2)
        print("Sonuç: ", result)

    elif choice == 2:
        result = num1/num2 - (base1/base2)
        print("Sonuç: ", result)

    elif choice == 3:
        result = num1*num2**(base1/base2)
        print("Sonuç: ", result)

    elif choice == 4:
        result = num1/num2**(base1/base2)
        print("Sonuç: ", result)

    else:
        print("Geçersiz seçim.")
    
    print("\nProgramı tekrar başlatmak için 'E' tuşuna basın.")
    repeat = input()
    if repeat.upper() == "E":
        log_calculator()

log_calculator()

