import random
s1=''''''
s2=''''''
def story(n,name):
    global e
    global f
    global s2
    a={1:'''Today, every student has a computer small enough to fit in to his 1.He can solve any math problem by simply pushing the computers little
    2.Computers can add, multiply,divide and 3.They can also 4 better than human.Some computers are 5. Others have a/an 6 screen that shows all kinds of
    7 and even 8 figures.''',
   2:''''''}
    global s1
    if name==e:
        s1=a[n]
    else:
        s2=a[n]
    inp(n,name)
def inp(n,name):
    global s1
    global e
    global f
    global s2
    if n==1:
        n1=input("enter a noun")
        np1=input("enter a plural noun")
        v1=input("enter an verb-present tense")
        v2=input("enter an verb")
        c1=input("enter a colour")
        ad1=input("enter an adjective")
        np2=input("enter a plural noun")
        ad2=input("enter an adjective")
        li=[n1,np1,v1,v2,c1,ad1,np2,ad2]
        b=1
        if name==e:
            for i in li:
                s1=s1.replace(str(b),i)
                b+=1
            print(s1)
        else:
            for i in li:
                s2=s2.replace(str(b),i)
                b+=1
            print(s2)

while 1:
    e=input("enter the name of player 1")
    f=input("enter the name of player 2")
    h=[e,f]
    print(e+" enter which level you want to play")
    k=int(input())
    story(k,e)
    print(f + " enter which level you want to play")
    k = int(input())
    story(k, f)
    print(s1+"\n\n"+s2)
    print("the winner is "+h[random.randrange(0,2)])
    break








