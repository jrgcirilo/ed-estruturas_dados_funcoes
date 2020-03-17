def espiao(arg):
    id1 = False
    id2 = False
    id3 = False
    for i in arg:
        if i == 0:
            if id3 is False:
                if id1 is False and id2 is False:
                    id1 = True
                elif id1 is True and id2 is False:
                    id2 = True
                else:
                    return False
            else:
                return False
        elif i == 7:
            if id1 is True and id2 is True:
                return True
            else:
                return False
res=espiao([1,2,4,0,0,7,5])
res2=espiao([1,0,2,4,0,5,7])
res3=espiao([1,7,2,4,0,5,0])
print(res)
print(res2)
print(res3)