while True:
    parola = input("parola belirleyin: ")
    if not parola:
        pass
    elif len(parola) in range(3, 9): #eğer parolanın uzunluğu 3 ile 8 karakter
        #aralığında ise...
        print("Yeni parolanız", parola)
        break
    else:
        print("parola en az 3, en fazla 8 karakter olmalı")