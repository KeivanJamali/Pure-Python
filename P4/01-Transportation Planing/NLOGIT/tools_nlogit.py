import pandas as pd
import numpy as np
import math
from pathlib import Path

class Tools:
    def __init__(self, data_wide):
        # self.data_long_path = Path(data_long_path)
        # self.data_wide_path = Path(data_wide_path)
        # self.data_wide = pd.read_csv(self.data_wide_path)
        # self.data_long = pd.read_csv(self.data_long_path)
        self.data_wide = data_wide
        # self.data_long = data_long
        self.data = self.data_wide.copy()
        self.confusion_matrix = None
        self.c1, self.c2 = None, None
        self.a = None
        self.l = None

    def fit(self, c1, c2, model="logit", b1=None, b2=None, a=None, l=5):
        self.c1, self.c2 = c1, c2
        self.b1, self.b2 = b1, b2
        self.a = a
        self.l = l
        self._update_data(model=model)
        self._confusion_matrix_function()

    def _function_utility_1(self, ic, oc, cons=0):
        u = self.c1 * ic + self.c2 * oc + cons
        return u
    

    def _function_nested_logit(self, IC1, OC1, IC2, OC2, IC3, OC3, IC4, OC4, IC5, OC5):
        IC = [IC1, IC2, IC3, IC4, IC5]
        OC = [OC1, OC2, OC3, OC4, OC5]
        down = 0
        for i in range(len(IC)):
            down += math.exp(self.b1 * IC[i] + self.b2 * OC[i])
        step_1 = []
        for i in range(len(IC)):
            up = math.exp(self.b1 * IC[i] + self.b2 * OC[i])
            step_1.append(up/down)

        down = 0
        for i in range(len(IC)):
            down += math.exp(self.c1 * IC[i] + self.c2 * OC[i])
        step_2 = []
        for i in range(len(IC)):
            up = math.exp(self.c1 * IC[i] + self.c2 * OC[i])
            step_2.append(up/down)

        result = []
        for i in range(len(IC)):
            result.append(step_1[i]/step_2[i])

        return result
        
    
    def _function_logit(self, IC1, OC1, IC2, OC2, IC3, OC3, IC4, OC4, IC5, OC5):
        IC = [IC1, IC2, IC3, IC4, IC5]
        OC = [OC1, OC2, OC3, OC4, OC5]
        down = 0
        for i in range(len(IC)):
            temp = self.a[i] if self.a else 0
            down += math.exp(self._function_utility_1(IC[i], OC[i], temp))
        result = []
        for i in range(len(IC)):
            temp = self.a[i] if self.a else 0
            up = math.exp(self._function_utility_1(IC[i], OC[i], temp))
            result.append(up/down)
        return result
    
    def _function_softmax(self, p1, p2, p3, p4, p5):
        res_list = [p1, p2, p3, p4, p5]
        res = res_list.index(max(res_list))
        return res + 1
    
    def _update_data(self, model):
        if model == "logit":
            self.data[["p1", "p2", "p3", "p4", "p5"]] = self.data.apply(lambda x: self._function_logit(x["ic1"], x["oc1"], x["ic2"], x["oc2"], x["ic3"], x["oc3"], x["ic4"], x["oc4"], x["ic5"], x["oc5"]), 
                                                                        axis=1,
                                                                        result_type="expand")
        elif model == "nested_logit":
            self.data[["p1", "p2", "p3", "p4", "p5"]] = self.data.apply(lambda x: self._function_nested_logit(x["ic1"], x["oc1"], x["ic2"], x["oc2"], x["ic3"], x["oc3"], x["ic4"], x["oc4"], x["ic5"], x["oc5"]), 
                                                                        axis=1,
                                                                        result_type="expand")
        self.data["p_choice"] = self.data.apply(lambda x: self._function_softmax(x["p1"], x["p2"], x["p3"], x["p4"], x["p5"]), 
                                                axis=1)
        
    def _confusion_matrix_function(self):
        confusion_matrix = np.zeros(shape=(self.l, self.l))
        for i in range(len(self.data.index)):
            confusion_matrix[self.data.iloc[i, 1]-1][self.data.iloc[i, -1]-1] += 1

        self.confusion_matrix = confusion_matrix

    def rate_score(self):
        r2_list = []
        for i in range(self.l):
            r2 = self.confusion_matrix[i, i] / self.confusion_matrix[i].sum()
            r2_list.append(float(r2))
        return r2_list
