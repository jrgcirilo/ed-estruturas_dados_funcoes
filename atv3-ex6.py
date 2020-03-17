def tem_33(arg):
    test = False
    for i in arg:
        if i == 3:
            if test is True:
                return True
            else:
                test = True
        else:
            test = False
    else:
        return False
res=tem_33([1,2,3,0,0,7,5])
res2=tem_33([1,0,2,4,0,5,7])
res3=tem_33([1,7,2,4,0,3,3])
print(res)
print(res2)
print(res3)