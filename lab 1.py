def parallel(list):
    sum=0
    Re=0
    for element in list:
        sum = sum + 1/element

    Re=1/sum 
    print (Re, "ohm")
parallel([330, 1000, 2000])

#question2
def potential_divider(x,list):
    res=0
    for elem in list:
        res=x*(x/sum(list))
        print(a,"volt")

