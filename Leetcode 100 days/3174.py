def clearDigits(s: str) -> str:
    a=len(s)
    i=0
    s=list(s)
    while i!=a:
        if s[i].isdigit():
            s.pop(i)
            a-=1
            if i!=0:
                s.pop(i-1)
                a-=1
                i-=1
        else:
            i+=1
    s="".join(s)
    print(s)
clearDigits("65weafaiofjaoergjeroigjoerg46521")
