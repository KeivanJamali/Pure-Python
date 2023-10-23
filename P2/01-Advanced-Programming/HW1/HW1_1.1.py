def can_transport_all(C, M, D, H):
    # Base case: If there are no cats, chickens, or seeds, we have successfully transported all of them
    if C == 0 and M == 0 and D == 0:
        return True

    # Check if it's possible to transport the cats
    if C > 0:
        # Check if the cats can be transported without chickens present
        if C <= H and M == 0:
            return True

    # Check if it's possible to transport the chickens
    if M > 0:
        # Check if the chickens can be transported without seeds present and without cats eating them
        if M <= H and D == 0 and C == 0:
            return True

    # Check if it's possible to transport the seeds
    if D > 0:
        # Check if the seeds can be transported without chickens eating them
        if D <= H and M == 0:
            return True

    # If no combination is successful, it's not possible to transport all the cats, chickens, and seeds
    return False


# while True:
#     try:
#         data = input().split(" ")
#         data = [int(i) for i in data]
#         if can_transport_all(data[0],data[1],data[2],data[3]):
#             print("YES")
#         else:
#             print("NO")
#     except:
#         break

print(can_transport_all(1,1,1,3))