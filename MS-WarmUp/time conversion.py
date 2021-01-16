def timeConversion(s):
    main=int(s[:2])
    tip=s[-2:]
    if main!=12:
        if tip=='PM':
            main+=12
            s=str(main)+s[2:8]
        else:
            s=s[0:8]
    else:
        if tip=='PM':
            s=s[0:8]
        else:
            s='00'+s[2:8]
    return s


s='07:05:45PM'
print(timeConversion(s))