def check_right_angle(a, b, c):
    if abs(a**2 + b**2 - c**2) < 0.01:
        return True
    else:
        return False
p_list = []
    
for p in range(3, 1001):
    p_counter = 0
    for a in range(1, p):
        for b in range(a, p):
            c = p - a - b
            if c < b:
                break
                
            if check_right_angle(a, b, c):
                p_counter += 1
    p_list.append(p_counter)

print(p_list.index(max(p_list))+3)