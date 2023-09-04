from random import Random

while True:
    lozi = Random().randrange(0, 10)
    setare = Random().randrange(0, 10)
    daere = Random().randrange(0, 10)
    mosalas = Random().randrange(0, 10)
    morab = 6

    m_lozi_setare = lozi + setare
    if m_lozi_setare % 10 != 5:
        continue
    m_daere_setare = daere + setare + m_lozi_setare // 10

    if m_daere_setare % 10 != lozi:
        continue
    m_morab_morab = morab * 2 + m_daere_setare // 10
    m_mosalas_morab = mosalas + m_morab_morab // 10
    if m_mosalas_morab % 10 != daere:
        continue
    fir_num = mosalas * 1000 + morab * 100 + daere * 10 + lozi
    sec_num = morab * 100 + setare * 10 + setare
    ans = fir_num + sec_num
    if len(str(ans)) != 5:
        continue
    break

print(fir_num, sec_num, ans)
