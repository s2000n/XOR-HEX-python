def bi(x):
    hex_v1 = {'0':'0000', '1':'0001','2':'0010','3':'0011',
              '4':'0100','5':'0101','6':'0110','7':'0111',
              '8':'1000','9':'1001','a':'1010','b':'1011',
              'c':'1100','d':'1101','e':'1110','f':'1111'}
    msg_len = len(x)
    final = ''
    for i in range(0, msg_len):
        final = final + hex_v1[x[i]]
    return final

def xor(ar1,ar2):
    out=[None]*len(ar1)
    for i in range(len(ar1)):
        if ar1[i]==ar2[i]:
            out[i]=0
        elif ar1[i]!=ar2[i]:
            out[i]=1
    return out

def main():
    print('messages must same number of digits')
    msg1=input('\nwrite message (HEX): ')
    msg1_bi=list(bi(msg1))
    print('in binary: ',*msg1_bi)
    msg2=input('\nwrite key (HEX):')
    msg2_bi=list(bi(msg2))
    print('in binary: ',*msg2_bi)
    out=xor(msg1_bi,msg2_bi)
    print('\nxor is: ',*out)

main()