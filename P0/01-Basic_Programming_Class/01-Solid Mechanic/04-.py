def soilclass():


    import math


    r = input('classifications name(USCS/AASHTO): ')
    a = float(input('F200: '))
    b = float()
    if a<50:
        b = float(input('F4: '))

    PL = float()
    LL = float()
    PI = float()
    PIA = float()

    LL = float(input('LL(%) = '))
    PI= float(input('PI(%) = '))
    PIA = 0.73 * (LL - 20)
    if PI > PIA:
        print(f'On A-Line, PI = 0.73(LL-20) = {PIA}%, '
              f'Hence with PI of {PI}% soil lies above the A-line')
    elif PI < PIA:
        print(f'On A-Line, PI = 0.73(LL-20) = {PIA}%, '
              f' Hence with PI of {PI}% soil lies below the A-line')

    if r.upper() == "USCS":
        print('----------------')
        print('USCS Classification: '
              '----------')
        D10 = float(input('D10(mm)= '))
        D60 = float(input('D60(mm) = '))
        D30 = float(input('D30(mm) = '))
        Cu = D60 / D10
        Cc = (D30) ** 2 / (D10 * D60)
        print(f'''Cu = D60/D10 = {Cu},  Cc = (D30)^2/(D10*D60) = {Cc}''')

        if a < 50:
            print(f'As less than 50% of total soil, i.e. {a}%, is passing through #200 sieve, '
                  f'it is a Coarse grained soil')
            if b < 50:
                if a < 5:
                    if Cu >= 4 and 1 <= Cc <= 3:
                        print(f'As Cu>=4 and 1<=Cc<=3, '
                              f'soil class is GW (Well Graded Gravel)')
                    else:
                        print(f'As either Cu<4 or Cc<1 or Cc>3, '
                              f'soil class is GP (Poorly Graded Gravel)')
                elif a > 12:
                    if PIA < PI and LL < 50:
                        print(f'With PI above A-line and LL<50, fines are clay with Low Compressibility(CH)',
                              f'so soil can be classified as GC - Clayey Gravel')
                    elif PIA < PI and LL > 50:
                        print(f'With PI above A-line and LL>50, fines are Clay with High Compressibility(CH)',
                              f'so soil can be classified as GC - Clayey Gravel')
                    elif PIA > PI and LL < 50:
                        print(f'With PI below A-line and LL<50,fines are Silt with Low Compressibility(ML)',
                              f'so soil can be classified as GM - Silty Gravel')
                    elif PIA > PI and LL > 50:
                        print(f'With PI below A-line and LL>50, fines are Silt with High Compressibility(MH)',
                              f'so soil can be classified as GC - Clayey Gravel')
                    exit()


            elif b >= 50:
                if a < 5:
                    if Cu >= 4 and 1 <= Cc <= 3:
                        print(f'As Cu>=4 and 1<=Cc<=3, '
                              f'soil class is SW (Well Graded Sand)')
                    else:
                        print(f'As either Cu<4 or Cc<1 or Cc>3, '
                              f'soil class is SP (Poorly Graded Sand)')

                elif a > 12:
                    if PIA < PI and LL < 50:
                        print(f'With PI above A-line and LL<50, fines are clay with Low Compressibility(CH)',
                              f'so soil can be classified as SC (Clayey Sand)')
                    elif PIA < PI and LL > 50:
                        print(f'With PI above A-line and LL>50, fines are Clay with High Compressibility(CH)',
                              f'so soil can be classified as SC (Clayey Sand)')
                    elif PIA > PI and LL < 50:
                        print(f'With PI below A-line and LL<50, fines are Silt with Low Compressibility(ML)',
                              f'so soil can be classified as SM (Silty Sand)')
                    elif PIA > PI and LL > 50:
                        print(f'With PI below A-line and LL>50, fines are Silt with High Compressibility(MH)',
                              f'so soil can be classified as SC (Clayey Sand)')


        elif a >= 50:
            print(f'More than or equal to 50%, i.e. {a}%, is passing through #200 sieve')
            if LL < 50:
                if PIA < PI and PI > 7:
                    print(f'With PI above A-line and LL<50, '
                          f'fines are clay with Low Compressibility(CL)')
                elif PIA > PI and PI < 4:
                    print(f'With PI below A-line, LL<50, and PI<4, '
                          f'fines are Silt with Low Compressibility(ML)')
            elif LL > 50:

                if PIA < PI:
                    print(f'With PI above A-line and LL>50, fines are Clay with High Compressibility(CH)')

                elif PIA > PI:
                    print(f'With PI below A-line and LL>50, fines are Silt with High Compressibility(MH)', "n")

    if r.upper() == "AASHTO":
        print('---------------------- ')
        print('AASHTO Soil Classification:')
        c = float(input('% finer than 2.00 mm (#10):  '))
        d = float(input('% finer than 0.425 mm (#40): '))

        if c <= 50 and d <= 30 and a <= 15 and PI <= 6:
            print(f'As % finer than 2.0mm (#200) <=50, %finer than 0.425 mm (#40)<=30'
                  f'% finer than 0.075mm (#200) <=15%, and PI<=6, '
                  f'hence the soil fits the criteria of soil class A-1-a (Stone Fragments,gravels and sand)')

        elif c >= 51 and d <= 50 and a <= 25 and PI <= 6:
            print(f'As %finer than 0.425 mm (#40)<=50'
                  f'% finer than 0.075mm (#200) <=25%, and PI<=6, '
                  f'hence the soil fits the criteria of soil class A-1-b (Stone Fragments,gravels and sand)')

        elif c >= 51 and d >= 51 and a <= 10 and v.lower() == "n":
            print(f'with %finer than 0.425 mm (#40) >=51, '
                  f'and % finer than 0.075mm (#200) <=10%, '
                  f'the soil is fine sand of class A-3')

        elif c > 50 and d >=51 and a <= 35 and LL <= 40 and PI <= 10:
            print(f'with LL<=40 and PI<=10, '
                  f'soil fits the criteria of "Silty or clayey Gravel" A-2-4')

        elif c > 50 and d > 50 and a <= 35 and LL >= 41 and PI <= 10:
            print(f'with LL>=41 and PI<=10, '
                  f'soil fits the criteria of "Silty or clayey Gravel" A-2-5')

        elif c > 50 and d > 50 and a <= 35 and LL <= 40 and PI >= 11:
            print(f'with LL<=40 and PI<=10, '
                  f'soil fits the criteria of "Silty or clayey Gravel" A-2-6')

        elif c > 50 and d > 50 and a <= 35 and LL >= 41 and PI >= 11:
            print(f'with LL>=41 and PI>=11, '
                  f'soil fits the criteria of "Silty or clayey Gravel" A-2-7')

        elif c > 50 and d > 50 and a >= 36 and LL <= 40 and PI <= 10:
            print(f'with LL<=40 and PI<=10, '
                  f'soil fits the criteria of "Silty Soils" A-4')

        elif c > 50 and d > 50 and a >= 36 and LL >= 41 and PI <= 10:
            print(f'with LL<=40 and PI<=10, '
                  f'soil fits the criteria of "Silty Soils" A-5')

        elif c > 50 and d > 50 and a >= 36 and LL <= 40 and PI >= 11:
            print(f'with LL<=40 and PI>=11, '
                  f'soil fits the criteria of "Silty Soils" A-6')

        elif c > 50 and d > 50 and a >= 36 and LL >= 41 and PI >= 11:
            if PI <= LL - 30:
                print(f'with LL>=41 and PI>=11, and PI < LL-30 '
                      f'soil fits the criteria of "Silty Soils" A-7-5')
            elif PI > (LL - 30):
                print(f'with LL>=41 and PI>=11, and PI > LL-30 '
                      f'soil fits the criteria of "Silty Soils" A-7-5')


soilclass()

a = input('Exit? stress/n: ')
while a.lower() == "n":
    soilclass()
    a = input('Exit? stress/n: ')
else:
    exit()