def check(A200, A4, Cc, Cu, LL, PI, oven_LL):
    """finding Soil_Kind"""
    A = A_line(LL)
    if A200 < 50:
        if A4 < (100 - A200) / 2:  # Gravel
            if A200 < 5:
                if Cu >= 4 and Cc <= 3 and Cc >= 1:  # Well Graded Gravel
                    # print("GW")
                    return "GW"
                else:  # Poor Graded Gravel
                    # print("GP")
                    return "GP"
            elif A200 > 12:
                if PI < 4 or PI < A:  # Silty Gravel
                    # print("GM")
                    return "GM"
                elif PI > 7 and PI >= A:  # Clayey Gravel
                    # print("GC")
                    return "GC"
            else:
                if Cu >= 6 and Cc <= 3 and Cc >= 1:  # Well Graded gravel

                    if PI < 4 or PI < A:  # Silty Sand
                        # print("GW-GM")
                        return "GW-GM"
                    elif PI > 7 and PI >= A:  # Clayey Sand
                        # print("GW-GC")
                        return "GW-GC"
                else:  # Poor Graded Sand
                    if PI < 4 or PI < A:  # Silty Sand
                        # print("GP-GM")
                        return "GP-GM"
                    elif PI > 7 and PI >= A:  # Clayey Sand
                        # print("GP-GC")
                        return "GP-GC"

        else:  # Sand
            if A200 < 5:
                if Cu >= 6 and Cc <= 3 and Cc >= 1:  # Well Graded Sand
                    # print("SW")
                    return "SW"
                else:  # Poor Graded Sand
                    # print("SP")
                    return "SP"
            elif A200 > 12:
                if PI < 4 or PI < A:  # Silty Sand
                    # print("SM")
                    return "SM"
                elif PI > 7 and PI >= A:  # Clayey Sand
                    # print("SC")
                    return "SC"
            else:
                if Cu >= 6 and Cc <= 3 and Cc >= 1:  # Well Graded Sand
                    if PI < 4 or PI < A:  # Silty Sand
                        # print("SW-SM")
                        return "SW-SM"
                    elif PI > 7 and PI >= A:  # Clayey Sand
                        # print("SW-SC")
                        return "SW-SC"
                else:  # Poor Graded Sand
                    if PI > 7 and PI >= A:  # Clayey Sand
                        # print("SP-SC")
                        return "SP-SC"
                    elif PI < 4 or PI < A:  # Silty Sand
                        # print("SP-SM")
                        return "SP-SM"
                    elif PI < 7 and LL < 25 and LL > 12:
                        return "SC-SM"
    elif A200 > 50:
        if LL < 50:
            if oven_LL / LL < 0.75:  # Organic Low Plasticity
                # print("OL")
                return "OL"
            elif PI > 7 and PI >= A:  # Clay Low Plasticity
                # print("CL")
                return "CL"
            elif PI < 4 or PI < A:  # Silt Low Plasticity
                # print("ML")
                return "ML"
            elif PI < 7 and LL < 25 and LL > 12:
                return "CL-ML"
        else:
            if oven_LL / LL < 0.75:  # Organic High Plasticity
                # print("OH")
                return "OH"
            elif PI >= A:  # Clay High Plasticity

                # print("CH")
                return "CH"
            elif PI < A:  # Silt High Plasticity
                # print("MH")
                return "MH"
    else:
        return "GM-ML"
    return "Nothing match!"


def A_line(LL):
    """A_line Function"""
    return 0.73 * (LL - 20)
print(A_line(55))
print(check(8, 70, 2, 5, 55, 20, 55))

