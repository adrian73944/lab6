import keyword
slowa=["for","print","break","done","bad"]
for i in slowa:
    kluczowe=keyword.iskeyword(i)
    if kluczowe==True:
        print(i,"jest kluczowe")
    else:
        print(i,"nie jest kluczowe")
