from modular.optimization_algorithms import GradientDescent
import numpy as np
import hashlib
import student_info

def solve_p4(student_id):
    seed = int(hashlib.sha256(student_id.encode()).hexdigest(), 16) % 1e8

    D = 10000 + int(seed) % 10000
    C = 1000
    T = []
    B = []
    number = 4
    for i in range(number):
        T.append(float((5+(2*i)) + int(seed)%(5+2*i)))
        B.append(0.1 * (i+1) + (int(seed)%10)/100)
    
    initial_point = np.random.random(number)
    # initial_point = np.array([3000, 2500, 2000, 1500])
        
    def travel_time(x, t, b):
        return t * (1 + b * (x/C)**4)
    
    tries = [100 * i for i in range(2, 15)]
    tries = [100000]

    results = [[], []]
    for t in tries:
        result = []
        def loss_fn(x: np.ndarray):
            cost = 0
            cost_cons = -D
            lambda_cons = t
            for i in range(len(T)):
                travel_time_val = travel_time(x[i], T[i], B[i])
                cost += x[i] * travel_time_val
                cost_cons += x[i]
            return cost + lambda_cons * cost_cons**2

        optim = GradientDescent(loss_fn,
                                initial_point,
                                max_iteration=1000,
                                epsilon=1e-6)
        x, y = optim.step(criteria=1e-3, log=False, D=D)

        for i in range(len(T)):
            val = travel_time(x[i], T[i], B[i])
            result.append(float(round(val, 2)))
        results[0].append(result)
        results[1].append(tuple([int(i/10) for i in x]))
    return results, D
    
if __name__ == "__main__":
    for k, v in student_info.students.items():
        res, D = solve_p4(student_id=v)
        print(f"\n############### {k} ##############")
        im_number = np.zeros(len(res[0]))
        for r in range(len(res[0])):
            im_number[r] = hash(tuple(res[1][r]))%100000
            # print(f"T={res[0][r]}, F(D={D} [?] {(sum(res[1][r]))*10}) = {res[1][r]} ##->## {hash(tuple(res[1][r]))%100000}")
        value, count = np.unique(im_number, return_counts=True)
        print(f"Important Number is : {int(value[np.argmax(count)])}")
        print(f"----------------------------------\n")
    
    # res, D = solve_p4(student_id="403206113")
    # for r in range(len(res[0])):
    #         print(f"T={res[0][r]}, F(D={D} [?] {sum(res[1][r])}) = {res[1][r]} ##->## {hash(tuple(res[1][r]))%100000}")

        