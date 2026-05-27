import numpy as np

class GoldenSection:
    def __init__(self, loss_function, a, b, epsilon=1e-8, max_iteration=100):
        self.loss_function = loss_function
        self.interval = [a, b]
        self.r = 0.618
        self.epsilon = epsilon
        self.max_iteration = max_iteration

    def step(self, log=False):
        left = (self.interval[1] - self.interval[0]) * (1 - self.r) + self.interval[0]
        right = (self.interval[1] - self.interval[0]) * (self.r) + self.interval[0]
        for i in range(1, self.max_iteration+1):
            z_l = self.loss_function(left)
            z_r = self.loss_function(right)
            if z_l <= z_r:
                self.interval[1] = right
                if self._criteria():
                    x = (self.interval[0] + self.interval[1])/2
                    if log:
                        print(f"[Success] Converged at step={i}")
                    return x, self.loss_function(x)
                else:
                    right = left
                    left = (self.interval[1] - self.interval[0]) * (1 - self.r) + self.interval[0]
            else:
                self.interval[0] = left
                if self._criteria():
                    x = (self.interval[0] + self.interval[1])/2
                    if log:
                        print(f"[Success] Converged at step={i}")
                    return x, self.loss_function(x)
                else:
                    left = right
                    right = (self.interval[1] - self.interval[0]) * (self.r) + self.interval[0]

    def _criteria(self):
        if abs(self.interval[1] - self.interval[0]) < 2 * self.epsilon:
            return True  
        else:
            return False  
        
class BiSection:
    def __init__(self, loss_function, a, b, epsilon=1e-8, max_iteration=100):
        self.loss_function = loss_function
        self.interval = [a, b]
        self.epsilon = epsilon
        self.max_iteration = max_iteration

    def step(self, epsilon=1e-2, log=False, K=0):
        for i in range(self.max_iteration):
            x = (self.interval[1] + self.interval[0])/2
            derivative = (self.loss_function(float(x)+epsilon) - self.loss_function(float(x)-epsilon)) / (2*epsilon)
            if derivative <= K:
                self.interval[0] = x
            else:
                self.interval[1] = x
            
            if self._criteria():
                x = (self.interval[0] + self.interval[1])/2
                if log:
                    print(f"[Success] Converged at step={i}")
                return x, self.loss_function(x)                

    def _criteria(self):
        if abs(self.interval[1] - self.interval[0]) < 2 * self.epsilon:
            return True  
        else:
            return False
        
class GradientDescent:
    def __init__(self, loss_function, x_initial, epsilon=1e-6, max_iteration=100):
        self.loss_function = loss_function
        self.x = np.array(x_initial)
        self.epsilon = epsilon
        self.max_iteration = max_iteration
        self.out = False
        
    def _get_gradient(self, x:np.ndarray):
        g = np.zeros_like(x)
        for i in range(len(x)):
            x1 = x.copy()
            x2 = x.copy()
            x1[i] += self.epsilon
            x2[i] -= self.epsilon
            g[i] = (self.loss_function(x1) - self.loss_function(x2)) / (2 * self.epsilon)
            if all(x1 == x) and all(x2 == x):
                print(f"[ERROR] epsilon has no effect on x. \n{x1}\n{x2}")
                raise ValueError("[ERROR] You should pick a larger epsilon.")
                self.out = True
        return g
    
    def _create_loss_function(self):
        def loss_function(alpha):
            input_vector = self.x - alpha * (self.gx)
            return self.loss_function(input_vector)
        return loss_function
    
    def step(self, criteria=1e-4, log=False, D=None):
        old_z = self.loss_function(self.x)
        for i in range(self.max_iteration):
            fx = self._create_loss_function()
            self.gx = self._get_gradient(self.x)
            optim = GoldenSection(fx, 0, 1, epsilon=self.epsilon)
            alpha, min_z = optim.step()            
            self.x = self.x - alpha * (self.gx)
            new_z = self.loss_function(self.x)
            if abs(new_z - old_z) < criteria:
                if log:
                    print(f"[Success] Converged at step={i}")
                return self.x, self.loss_function(self.x)
            if self.out:
                print("##NOT CONVERGED##")
                return self.x, self.loss_function(self.x)
            old_z = new_z.copy()
        if log:
            print(f"[ERROR] Reach to max iteration -> {self.max_iteration}")
        return self.x, self.loss_function(self.x)
            