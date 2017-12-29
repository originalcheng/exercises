def dec2hex(num):
    lookup = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    res = []
    while num !=0:
        remainder = num%16
        res= [lookup[remainder]]+res
        num = int(num/16)
    return res


if __name__ == "__main__":
    res = dec2hex(254)
    print(res)