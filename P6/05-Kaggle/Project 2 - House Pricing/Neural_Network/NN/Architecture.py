import torch
import torch.nn as nn

class NN(nn.Module):
    def __init__(self, features_n, output_n, hidden_n1, hidden_n2):
        super().__init__()
        self.l_0 = nn.Linear(in_features=features_n, out_features=hidden_n1)
        self.l_1 = nn.Linear(in_features=hidden_n1, out_features=hidden_n1)
        self.l_2 = nn.Linear(in_features=hidden_n1, out_features=hidden_n1)
        self.l_3 = nn.Linear(in_features=hidden_n1, out_features=hidden_n1)
        self.l_00 = nn.Linear(in_features=hidden_n1, out_features=output_n)
        self.relu = nn.ReLU()

    def forward(self, x):
        output = self.relu(self.l_0(x))
        output = self.relu(self.l_1(output))
        output = self.relu(self.l_2(output))
        output = self.relu(self.l_3(output))
        output = self.relu(self.l_00(output))
        return output