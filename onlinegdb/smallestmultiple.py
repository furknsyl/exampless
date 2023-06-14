##smallest multiple
num = 1
while True:
    stn = True
    for i in range(1, 21):
        if num % i != 0:
            stn = False
            break
    if stn:
        print(num)
        break
    num += 1