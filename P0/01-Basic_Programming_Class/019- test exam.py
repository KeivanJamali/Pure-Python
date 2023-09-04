b = '12ab3'
i = 0
while i< 4:
    try:
        a = int(b[i])
    except:
        try:
            a = a//i
        except:
            i = 0
    finally:
        i+=1