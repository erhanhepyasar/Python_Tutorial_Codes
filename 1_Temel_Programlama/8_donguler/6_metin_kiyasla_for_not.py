#ilk_metin adlı degisken içinde bulunan, ancak ikinci_metin adlı degisken içinde
# bulunmayan karakterleri listelemek

ilk_metin = "asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh"
ikinci_metin = "sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf"
for s in ilk_metin:
    if not s in ikinci_metin:
        print(s)