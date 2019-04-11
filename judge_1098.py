"""
I=0 J=1 
I=0 J=2 
I=0 J=3 

I=0.2 J=1.2 
I=0.2 J=2.2 
I=0.2 J=3.2 

I=0.4 J=1.4 
I=0.4 J=2.4 
I=0.4 J=3.4 

I=0.6 J=1.6 
I=0.6 J=2.6 
I=0.6 J=3.6 

I=0.8 J=1.8 
I=0.8 J=2.8 
I=0.8 J=3.8 

I=1.0 J=2.0 
I=1.0 J=3.0 
I=1.0 J=4.0 

I=1.2 J=2.2 
I=1.2 J=3.2 
I=1.2 J=4.2 

I=1.4 J=2.4 
I=1.4 J=3.4 
I=1.4 J=4.4 

I=1.6 J=2.6 
I=1.6 J=3.6 
I=1.6 J=4.6 

I=1.8 J=2.8 
I=1.8 J=3.8 
I=1.8 J=4.8 

I=2.0 J=3.0 
I=2.0 J=4.0 
I=2.0 J=5.0
"""
i = 0
j = 1
a = 0.2
n = 0
while i <= 2:
    for c in range(1, 4):
        if i > 2.19:
            print('I={:.0f} J={:.0f}'.format(2, j))
        if i == 1.0 or i == 0.0 or i > 1.8:
            print('I={:.0f} J={:.0f}'.format(i, j))
        elif i < 2:
            print('I={:.1f} J={:.1f}'.format(i, j))
        j = j + 1
    i = i + a
    j = 1 + i




