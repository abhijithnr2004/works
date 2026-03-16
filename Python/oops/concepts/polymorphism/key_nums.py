def operation(*args,**Kwargs) :

    if Kwargs.get("key") == "max" :

        print("Max :",max(args))

    else :

        print("Min :",min(args))

operation(10,20,40,30,key="max")

operation(10,20,40,30,key="min")