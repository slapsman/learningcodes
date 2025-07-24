
print("roller coaster`a hoş geldiniz")
boy=int(input("boyunuz kaç"))
if boy>=180 :
    print("roller coaster`a binebilirsiniz")
    yas=int(input("yaşiniz kaç"))
    if yas <=12 :
        print("roller coaster`a binmek için 5tl ödemen gerekli")
    elif yas<=18 :
        print("roller coaster`a binmek için 7tl ödemen gerekli")
    else :
        print("roller coaster`a binmek için 25tl ödemen lazım")
else :
    print("roller coaster`a binemessin")


