cards = '6', '7', '8', '9', '1', 'J', 'Q', 'K', 'A'
mast = 'C', 'D', 'H', 'S'

inp1, inp2 = input().split()
kozir = str(input())
z1, z2 = inp1[0], inp2[0]
m1, m2 = inp1[-1], inp2[-1]

if z1 in cards and z2 in cards and m1 in mast and m2 in mast:
    a, b = cards.index(z1), cards.index(z2)
    if m1 == m2:
            print('First' if a > b else 'Second' if a < b else 'Error')
    else:
        print('First' if m1 == kozir else 'Second' if m2 == kozir else 'Error')
else:
    print('Error')


