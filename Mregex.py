import re


def regex():
    '''
    Misol uchun matndan 3 xonali sonlarni ajratib olib listga saqlovchi funksiya
    '''
    misol = 'Namunaviy sonlar 1, 12, 13, va 345 muhim 456'
    natija = re.findall(r'\d\d\d', misol)
    print(natija)

regex()

print(regex.__doc__)        # Bu bilan istalgan funksiya, klasslarning ichidagi izohlarni olish mumkin