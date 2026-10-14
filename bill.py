def electronics_gst(a,b):
    amount=a+b
    gst=amount*18/100
    return amount+gst

def food_gst(e):
    gst=e*7/100
    return e+gst

def fashion_gst(a,b):
    amount=a+b
    gst=amount*13/100
    return amount+gst

def total_bill(a,b,c,d,e):
    electronics=electronics_gst(a,b)
    fashion=fashion_gst(c,d)
    food=food_gst(e)

    return electronics+fashion+food

def calculate_discount(a,b,c,d,e):
    total=total_bill(a,b,c,d,e)
    discount=total*20/100
    return total-discount

a=100
b=100
c=100
d=100
e=100
total=total_bill(a,b,c,d,e)
discount=total*20/100
final=calculate_discount(a,b,c,d,e)

print("Total after GST:",total)
print("Discount:",discount)
print("Final Bill:",final)