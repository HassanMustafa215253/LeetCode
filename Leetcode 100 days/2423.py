def doesValidArrayExist(derived: list[int]) -> bool:
    xored=derived.copy()
    for i in range(len(derived)-1):
        xored[i]=xored[i]^xored[i+1]
    xored[-1]=xored[-1]^xored[0]

    x22=[]
    for i in range(len(xored)-1):
        x22.append((xored[i]^xored[i+1])^1)
    x22.append((xored[-1]^xored[0])^1)

    print("derived: ",derived)
    print("xored: ",xored)
    # print("xored^1: ",[i^1 for i in xored])
    print("x22: ",x22)



    if x22==derived:
        return 1
    else:
        return 0
print(doesValidArrayExist([1,1,0]),end="\n\n")
# print(doesValidArrayExist([1,1]),end="\n\n")
print(doesValidArrayExist([0,1,1]),end="\n\n")