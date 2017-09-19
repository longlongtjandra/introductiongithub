x=1
y=10

(x <= y)

for i in range (1,y+1):
    if (i <= 5):
        print(" "* (y-i), "*" * (i*2-1))

    else:
        print (" "* i, "*" *( (y-i )*2-1))

x+=1
