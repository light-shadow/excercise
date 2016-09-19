def reverse(aString):
    a = len(aString)
    bString = ''
    while(a>0):
        bString += aString[a-1]
        a = a-1
    if aString == bString:
        print True
    else:
        print False
        
reverse('aba')
reverse('abab')
