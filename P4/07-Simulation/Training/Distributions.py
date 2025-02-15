from IPython.display import display, Math
from math import factorial
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class DU:
    def __init__(self, i:int, j:int, size:int=100, print_:bool=False):
        self.print_ = print_
        self.sample = Distribution_Sample_Maker.discrete_uniform(i=i, j=j, size=size)
        self.i = i
        self.j = j
        self.size = size
        self.mean = self._mean()
        self.var = self._var()

    def _mean(self):
        temp = (self.i+self.j)/2
        if self.print_:
            display(Math(r"\text{Mean of the Discrete Uniform is } \frac{i+j}{2} = " + f"{temp:.2f}"))
        return temp
    
    def _var(self):
        temp = ((self.j-self.i+1)**2 - 1) / 12
        if self.print_:
            display(Math(r"\text{Variance of the Discrete Uniform is } \frac{(j-i+1)^2 - 1}{12} = " + f"{temp:.2f}"))
        return temp
    
    def mass_function(self, x):
        if self.i <= x <= self.j:
            return (self.j-self.i+1)**(-1)
        else:
            return 0
        
    def distribution_function(self, x):
        if x < self.i:
            return 0
        elif x > self.j:
            return 1
        else:
            return (int(x)-self.i+1)/(self.j-self.i+1)
        

class Bernoulli:
    def __init__(self, p:float, size:int=100, print_:bool=False):
        self.print_= print_
        self.sample = Distribution_Sample_Maker.bernoulli(p=p, size=size)
        self.p = p
        self.mean = self._mean()
        self.var = self._var()
        self.mode = self._mode()

    def _mean(self):
        temp = self.p
        if self.print_:
            display(Math(r"\text{Mean of the Bernoulli is } p = " + f"{temp:.2f}"))
        return temp
    
    def _var(self):
        temp = self.p*(1-self.p)
        if self.print_:
            display(Math(r"\text{Variance of the Bernoulli is } p\times(1-p) = " + f"{temp:.2f}"))
        return temp
    
    def _mode(self):
        if self.p < 0.5:
            temp = 0
        elif self.p == 0.5:
            temp = [0, 1]
        else:
            temp = 1
        if self.print_:
            display(Math(r"\text{Mode of the Bernoulli is } " + f"{temp}"))
        return temp
    
    def mass_function(self, x):
        if x==1:
            return self.p
        elif x==0:
            return 1-self.p
        else:
            return 0
        
    def distribution_function(self, x):
        if x < 0:
            return 0
        elif 0 <= x < 1:
            return 1-self.p
        else:
            return 1

class Bin:
    def __init__(self, t:int, p:float, size:int=100, print_:bool=False):
        self.print_= print_
        self.sample = Distribution_Sample_Maker.binomial(t=t, p=p, size=size)
        self.t = t
        self.p = p
        self.mean = self._mean()
        self.var = self._var()
        self.mode = self._mode()

    def _mean(self):
        temp = self.t * self.p
        if self.print_:
            display(Math(r"\text{Mean of the Binomial is } np = " + f"{temp:.2f}"))
        return temp
    
    def _var(self):
        temp = self.t * self.p*(1-self.p)
        if self.print_:
            display(Math(r"\text{Variance of the Binomial is } n \times p \times (1-p) = " + f"{temp:.2f}"))
        return temp
    
    def _mode(self):
        if (self.p*(self.t+1)) % 1 < 0.00001:
            temp = [self.p*(self.t+1) - 1, self.p*(self.t+1)]
        else:
            temp = int(self.p*(self.t+1))
        if self.print_:
            display(Math(r"\text{Mode of the Binomial is } " + f"{temp}"))
        return temp
    
    def mass_function(self, x):
        if x in range(0, self.t+1):
            coef = factorial(self.t)/(factorial(x)*factorial(self.t-x))
            return coef * self.p**(x) * (1-self.p)**(self.t-x)
        else:
            return 0
        
    def distribution_function(self, x):
        if x < 0:
            return 0
        elif 0 <= x <= self.t:
            temp = sum([self.mass_function(i) for i in range(0, int(x))])
            return temp
        else:
            return 1

class Poisson:
    def __init__(self, lamb:int, size:int=100, print_:bool=False):
        self.print_= print_
        self.sample = Distribution_Sample_Maker.poisson(lamb=lamb, size=size)
        self.lamb = lamb
        self.mean = self._mean()
        self.var = self._var()
        self.mode = self._mode()

    def _mean(self):
        temp = self.lamb
        if self.print_:
            display(Math(r"\text{Mean of the Poisson is } \lambda = " + f"{temp:.2f}"))
        return temp
    
    def _var(self):
        temp = self.lamb
        if self.print_:
            display(Math(r"\text{Variance of the Poisson is } \lambda = " + f"{temp:.2f}"))
        return temp
    
    def _mode(self):
        if self.lamb % 1 < 0.00001:
            temp = [self.lamb-1, self.lamb]
        else:
            temp = int(self.lamb)
        if self.print_:
            display(Math(r"\text{Mode of the Poisson is } " + f"{temp}"))
        return temp
    
    def mass_function(self, x):
        if x >= 0 and x%1 < 0.0001:
            temp = (np.e**(-self.lamb) * self.lamb**x) / factorial(x)
            return temp
        else:
            return 0
        
    def distribution_function(self, x):
        if x < 0:
            return 0
        elif 0 <= x:
            temp = np.e**(-self.lamb) * sum((self.lamb**i)/factorial(i) for i in range(0, int(x)))
            return temp
        
class Geom:
    def __init__(self, p:float, size:int=100, print_:bool=False):
        self.print_= print_
        self.sample = Distribution_Sample_Maker.geometry(p=p, size=size)
        self.p = p
        self.mean = self._mean()
        self.var = self._var()
        self.mode = self._mode()

    def _mean(self):
        temp = (1-self.p)/self.p
        if self.print_:
            display(Math(r"\text{Mean of the Geometry is } \lambda = " + f"{temp:.2f}"))
        return temp
    
    def _var(self):
        temp = (1-self.p)/self.p**2
        if self.print_:
            display(Math(r"\text{Variance of the Geometry is } \lambda = " + f"{temp:.2f}"))
        return temp
    
    def _mode(self):
        temp = 0
        if self.print_:
            display(Math(r"\text{Mode of the Geometry is } " + f"{temp}"))
        return temp
    
    def mass_function(self, x):
        if x >= 0 and x%1 < 0.0001:
            temp = self.p*(1-self.p)**x
            return temp
        else:
            return 0
        
    def distribution_function(self, x):
        if 0 <= x:
            temp = 1 - (1-self.p)**(1+int(x))
        else:
            temp = 0
        return temp
    
class Negbin:
    def __init__(self, s:int, p:float, size:int=100, print_:bool=False):
        self.print_= print_
        self.sample = Distribution_Sample_Maker.negetivebinomial(s=s, p=p, size=size)
        self.p = p
        self.s = s
        self.mean = self._mean()
        self.var = self._var()
        self.mode = self._mode()

    def _mean(self):
        temp = self.s * ((1-self.p)/self.p)
        if self.print_:
            display(Math(r"\text{Mean of the Negative Binomial is } \lambda = " + f"{temp:.2f}"))
        return temp
    
    def _var(self):
        temp = self.s * ((1-self.p)/self.p**2)
        if self.print_:
            display(Math(r"\text{Variance of the Negative Binomial is } \lambda = " + f"{temp:.2f}"))
        return temp
    
    def _mode(self):
        temp = (self.s * (1-self.p) - 1)/self.p
        if temp % 1 < 0.0001:
            temp = [temp, temp + 1]
        else:
            temp = int(temp)
        if self.print_:
            display(Math(r"\text{Mode of the Negative Binomial is } " + f"{temp}"))
        return temp
    
    def mass_function(self, x):
        if x >= 0 and x%1 < 0.0001:
            coef = factorial(int(self.s+x-1)) / factorial(x) * factorial(self.s-1)
            temp = coef * self.p**self.s * (1-self.p)**x
            return temp
        else:
            return 0
        
    def distribution_function(self, x):
        if 0 <= x:
            temp = sum(self.mass_function(i) for i in range(0, int(x)+1))
        else:
            temp = 0
        return temp




class Distribution_Sample_Maker:
    @staticmethod
    def discrete_uniform(i:int, j:int, size:int) -> np.array:
        sample = np.random.randint(i, j+1, size=size)
        return sample
    
    @staticmethod
    def bernoulli(p:float, size:int):
        sample = np.random.choice([0, 1], size=size, p=[1 - p, p])
        return sample
    
    @staticmethod
    def binomial(t:int, p:float, size:int):
        sample = np.random.binomial(n=t, p=p, size=size)
        return sample
    
    @staticmethod
    def poisson(lamb:int, size:int):
        sample = np.random.poisson(lam=lamb, size=size)
        return sample

    @staticmethod
    def geometry(p:float, size:int):
        """The result shows the number of failure before success. Not the total trial which is n+1"""
        uniform_random = np.random.uniform(0, 1, size=size)
        sample = np.ceil(np.log(uniform_random) / np.log(1-p)) - 1
        return sample.astype(int)
    


class Sample_Calculation:
    def __init__(self, sample):
        self.sample = sample
        self.mean = self._mean()
        self.var = self._var()
        self.data, self.distribution = self._make_data()
        self.max = self._max()
        self.n = len(sample)

    def plot_data(self) -> None:
        plt.bar(self.data.keys(), self.data.values(), width=0.3, alpha=0.7, edgecolor="red")
        plt.xticks(list(self.data.keys()))
        plt.xlabel("X")
        plt.ylabel("Repeate")
        plt.title("Function Plot")
        plt.show()

    def plot_distribution(self) -> None:
        plt.plot(self.distribution.keys(), self.distribution.values())
        plt.xticks(list(self.data.keys()))
        plt.xlabel("X")
        plt.ylabel("Cumulative probability")
        plt.title("Distribution Plot")
        plt.show()

    def _make_data(self):
        data = {}
        distribution = {0:0}
        sorted_sample = sorted(self.sample)
        for i in sorted_sample:
            i = int(i)
            if i in data.keys():
                data[i] += 1
                distribution[i] += 1
            else:
                data[i] = 1
                distribution[i] = max(distribution.values()) + 1
        return data, distribution

    def _mean(self):
        # m = sum(self.sample) / len(self.sample)
        m = np.mean(self.sample)
        return float(m)

    def _var(self, ddof=0):
        # var = sum((x - self.mean(print_=False)) ** 2 for x in self.sample) / (len(self.sample) - 1)
        var = np.var(self.sample, ddof=ddof)
        return float(var)
    
    def _max(self):
        return max(self.sample)

    def MLE(self, type_:str):
        if type_ == "discrete_uniform":
            print(f"We have a ''Discrete Uniform'' distribution\nfor the maximum Likelihood Estimator we have \nthese parameters: i={min(self.sample)} and j={max(self.sample)} with size of {len(self.sample)}")

        elif type_ == "bernoulli":
            temp = sum(self.sample)/len(self.sample)
            print(f"We have a ''Bernoulli'' distribution\nfor the maximum Likelihood Estimator we have \nthese parameters: p={temp} with size of {len(self.sample)}")

        elif "binomial" in type_:
            par = type_.split("_")
            if len(par) == 2:
                temp = sum(self.sample) / len(self.sample)
                temp = temp / int(par[1])
                print(f"We have a ''Binomial'' distribution with known parameters of t={par[1]}\nfor the maximum Likelihood Estimator we have \nthese parameters: p={temp:.2f} with size of {len(self.sample)}")
            elif len(par) == 1:
                f_k = np.array([np.sum(self.sample >= k) for k in range(1, self.max + 1)])
                def g(t, p):
                    term1 = np.sum(f_k * np.log(t - np.arange(1, len(f_k) + 1) + 1))
                    term2 = self.n * t * np.log(1 - p)
                    term3 = self.n * self.mean * np.log(p / (1-p))
                    return term1 + term2 + term3                
                
                t_values = np.arange(self.max, int((self.mean * (self.max-1)) / (1 - self.var / self.mean) + 1))
                best_t = 0
                best_p = 0
                max_likelihood = -np.inf

                for t in t_values:
                    p = self.mean / t
                    if 0 < p < 1:
                        likelihood = g(t, p)
                        if likelihood > max_likelihood:
                            max_likelihood = likelihood
                            best_t = t
                            best_p = p
                print(f"We have a ''Binomial'' distribution without known parameters\nfor the maximum Likelihood Estimator we have \nthese parameters: t={best_t} and p={best_p:.2f} with size of {len(self.sample)}")

        elif type_ == "poisson":
            temp = sum(self.sample)/len(self.sample)
            print(f"We have a ''Poisson'' distribution \nfor the maximum Likelihood Estimator we have \nthese parameters: lambda={temp:.2f} with size of {len(self.sample)}")

        elif type_ == "geometry":
            temp = 1/(sum(self.sample)/len(self.sample)+1)
            print(f"We have a ''Geometry'' distribution \nfor the maximum Likelihood Estimator we have \nthese parameters: lambda={temp:.2f} with size of {len(self.sample)}")


        elif type_ == "negative_binomial":
            temp = 1/(sum(self.sample)/len(self.sample)+1)
            print(f"We have a ''Negative Binomial'' distribution \nfor the maximum Likelihood Estimator we have \nthese parameters: lambda={temp:.2f} with size of {len(self.sample)}")


        
