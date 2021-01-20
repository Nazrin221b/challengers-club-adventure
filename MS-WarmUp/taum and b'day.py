def taumBday(b, w, bc, wc, z):
    return b*min(bc, wc+z) + w*min(wc,bc+z)



b=int(input('black gifts:' ))
w=int(input('white gifts:' ))
bc=int(input('cost of black gift: '))
wc=int(input('cost of white gift: '))
z=int(input('cost for convertion: '))
print(taumBday(b,w,bc,wc, z))