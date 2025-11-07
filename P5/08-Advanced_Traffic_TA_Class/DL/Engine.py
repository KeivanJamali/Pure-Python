from tqdm.auto import tqdm
import torch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from IPython.display import clear_output

class Model:
    def __init__(self,
                 model: torch.nn.Module,
                 random_seed: int = 42):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.seed = random_seed
        self.model = model.to(self.device)
        self.results = None
        self.train_true_predict_list, self.val_true_predict_list = [], []
        
    def train_step(self, 
                   loss_fn: torch.nn.Module, 
                   optimizer: torch.optim.Optimizer,
                   train_dataloader: torch.utils.data.DataLoader,
                   metrics: list[str] = ["MAE", "MSE", "R2"],
                   plot_resolution: int = 0,
                   if_tqdm: bool = True):
        self.model.train()
        self.train_metrics = {metric: 0 for metric in metrics} if metrics else {}
        self.true_predicted_list = {"true": [], "predicted": []}

        for batch, (x, targets) in enumerate(tqdm(train_dataloader, desc="Batch Training", disable=not if_tqdm)):
            x = x.to(self.device)
            targets = targets.to(self.device).squeeze()
            optimizer.zero_grad()
            outputs = self.model(x).squeeze()
            loss = loss_fn(outputs, targets)
            loss.backward()
            optimizer.step()
            
            self.true_predicted_list["true"].extend(targets.detach().cpu().numpy())
            self.true_predicted_list["predicted"].extend(outputs.detach().cpu().numpy())

            if plot_resolution and batch % plot_resolution == 0:
                self.plot_true_vs_predicted()

        for metric in self.train_metrics:
            if metric == "MAE":
                self.train_metrics[metric] = round(mean_absolute_error(self.true_predicted_list["true"], self.true_predicted_list["predicted"]), 4)
            elif metric == "MSE":
                self.train_metrics[metric] = round(mean_squared_error(self.true_predicted_list["true"], self.true_predicted_list["predicted"]), 4)
            elif metric == "R2":
                self.train_metrics[metric] = round(r2_score(self.true_predicted_list["true"], self.true_predicted_list["predicted"]), 2)

        return self.train_metrics, self.true_predicted_list
    
    def validation_step(self,
                        val_dataloader: torch.utils.data.DataLoader,
                        metrics: list[str] = ["MAE", "MSE", "R2"],
                        plot_resolution: int = 0,
                        if_tqdm: bool = False):
        self.model.eval()
        self.val_metrics = {metric: 0 for metric in metrics} if metrics else {}
        self.true_predicted_list = {"true": [], "predicted": []}

        with torch.inference_mode():
            for batch, (x, targets) in enumerate(tqdm(val_dataloader, desc="Batch Validation", disable=not if_tqdm)):
                x, targets = x.to(self.device), targets.to(self.device).squeeze()
                outputs = self.model(x).squeeze()

                self.true_predicted_list["true"].extend(targets.detach().cpu().numpy())
                self.true_predicted_list["predicted"].extend(outputs.detach().cpu().numpy())

                if plot_resolution and batch % plot_resolution == 0:
                    self.plot_true_vs_predicted()

        for metric in self.val_metrics:
            if metric == "MAE":
                self.val_metrics[metric] = round(mean_absolute_error(self.true_predicted_list["true"], self.true_predicted_list["predicted"]), 4)
            elif metric == "MSE":
                self.val_metrics[metric] = round(mean_squared_error(self.true_predicted_list["true"], self.true_predicted_list["predicted"]), 4)
            elif metric == "R2":
                self.val_metrics[metric] = round(r2_score(self.true_predicted_list["true"], self.true_predicted_list["predicted"]), 2)

        return self.val_metrics, self.true_predicted_list
    
    def plot_true_vs_predicted(self):
        true = self.true_predicted_list["true"]
        predicted = self.true_predicted_list["predicted"]
        sample_number = len(true)
        clear_output(wait=True)
        plt.figure(figsize=(10, 6))
        plt.scatter(range(sample_number), true[:sample_number], label="True", color="blue", marker=".")
        plt.scatter(range(sample_number), predicted[:sample_number], label="Predicted", color="orange", marker=".")
        plt.xlabel("Sample Index")
        plt.ylabel("Value")
        plt.title("True vs Predicted Values")
        plt.legend()
        plt.grid()
        plt.show()
        

class Engine:
    def __init__(self,
                 model: Model,
                 train_dataloader: torch.utils.data.DataLoader,
                 val_dataloader: torch.utils.data.DataLoader,
                 random_seed: int = 42,):
        self.model = model
        self.train_dataloader = train_dataloader
        self.val_dataloader = val_dataloader
        self.seed = random_seed
        
    def train(self,
              loss_fn: torch.nn.Module,
              optimizer: torch.optim.Optimizer,
              epochs: int,
              metrics: list[str] = ["MAE", "MSE", "R2"],
              plot_resolution: int = 0):
        self.train_true_predicted_list = {"true": [], "predicted": []}
        self.val_true_predicted_list = {"true": [], "predicted": []}
        self.metrics_history = {"train": {metric: [] for metric in metrics}, "val": {metric: [] for metric in metrics}}
        
        for epoch in tqdm(range(epochs), desc="Epoch Training"):
            self.train_metrics, train_data = self.model.train_step(loss_fn, optimizer, self.train_dataloader, metrics, if_tqdm=False)
            self.val_metrics, val_data = self.model.validation_step(self.val_dataloader, metrics, if_tqdm=False)
            
            # Store complete epoch data
            self.train_true_predicted_list["true"] = train_data["true"]
            self.train_true_predicted_list["predicted"] = train_data["predicted"]
            self.val_true_predicted_list["true"] = val_data["true"]
            self.val_true_predicted_list["predicted"] = val_data["predicted"]
            
            # Store metrics history
            for metric in metrics:
                self.metrics_history["train"][metric].append(self.train_metrics[metric])
                self.metrics_history["val"][metric].append(self.val_metrics[metric])

            if plot_resolution and epoch % plot_resolution == 0:
                self.plot_true_vs_predicted()
            elif not plot_resolution and epoch % 10 == 0:
                print(f"EPOCH {epoch+1:02d} | train loss: {self.train_metrics} | val loss: {self.val_metrics}")
                

        self.model.results = {"train": self.train_metrics, "val": self.val_metrics}
        return self.model.results
    
    def plot_true_vs_predicted(self):
        clear_output(wait=True)
        fig, axes = plt.subplots(2, 1, figsize=(15, 10))
        
        # Plot Training Data
        train_true = self.train_true_predicted_list["true"]
        train_pred = self.train_true_predicted_list["predicted"]
        axes[0].plot(range(len(train_true)), train_true, label="True", color="blue", linewidth=2)
        axes[0].plot(range(len(train_pred)), train_pred, label="Predicted", color="orange", linewidth=2)
        axes[0].set_xlabel("Sample Index")
        axes[0].set_ylabel("Value")
        axes[0].set_title("Training: True vs Predicted Values")
        axes[0].legend()
        axes[0].grid()
        
        # Plot Validation Data
        val_true = self.val_true_predicted_list["true"]
        val_pred = self.val_true_predicted_list["predicted"]
        axes[1].plot(range(len(val_true)), val_true, label="True", color="blue", linewidth=2)
        axes[1].plot(range(len(val_pred)), val_pred, label="Predicted", color="orange", linewidth=2)
        axes[1].set_xlabel("Sample Index")
        axes[1].set_ylabel("Value")
        axes[1].set_title("Validation: True vs Predicted Values")
        axes[1].legend()
        axes[1].grid()
        
        plt.tight_layout()
        plt.show()
    
    def plot_metrics(self):
        """Plot training and validation metrics over epochs."""
        metrics = list(self.metrics_history["train"].keys())
        num_metrics = len(metrics)
        
        fig, axes = plt.subplots(1, num_metrics, figsize=(6 * num_metrics, 5))
        
        # Handle case where there's only one metric
        if num_metrics == 1:
            axes = [axes]
        
        for idx, metric in enumerate(metrics):
            train_history = self.metrics_history["train"][metric]
            val_history = self.metrics_history["val"][metric]
            epochs = range(1, len(train_history) + 1)
            
            axes[idx].plot(epochs, train_history, marker='.', label=f"Train {metric}", linewidth=2)
            axes[idx].plot(epochs, val_history, marker='.', label=f"Val {metric}", linewidth=2)
            axes[idx].set_xlabel("Epoch")
            axes[idx].set_ylabel(metric)
            axes[idx].set_title(f"{metric} over Epochs")
            axes[idx].legend()
            axes[idx].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        