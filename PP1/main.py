from xmlrpc.client import boolean


def add(string=""):
    a=0
    temp=""
    string=string.replace(" ", "")
    string=string.replace("\n", ",")
    if(string.find(",,")!=-1): raise ValueError
    if(string==""): return 0
    if(string==","): return 0

    for i in string:
        if (i != "," and i != " "):
            temp+=i
        else:
            if(i==","):
                a+=int(temp)
                temp=""
    a+=int(string[-1])

    return a

print(add("1,1,1"))

