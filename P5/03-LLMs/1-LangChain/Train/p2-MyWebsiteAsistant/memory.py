from pathlib import Path
from datetime import datetime
import pandas as pd

class Memory:
    def __init__(self, user_id:str, log_folder_path:str):
        self.user_id = user_id
        self.log_folder_path = Path(log_folder_path)

    def update_memory(self, query:str, response:str) -> None:
        print("[INFO] Updating memory...")
        date = datetime.now().strftime("%Y-%m-%d")
        filename = self.log_folder_path / f"{date}.csv"
        data = pd.read_csv(filename) if filename.exists() else pd.DataFrame(columns=["time", "user_id", "query", "response"])

        time = datetime.now().strftime("%H:%M:%S")
        data.loc[len(data)] = {"time": time, "user_id": self.user_id, "query": query, "response": response}
        data.to_csv(filename, index=False)
        print("[INFO] Memory updated successfully.")

    def get_relevant_history(self, limit:int=5) -> list:
        print(f"[INFO] finding history for {self.user_id}...")
        date = datetime.now().strftime("%Y-%m-%d")
        filename = self.log_folder_path / f"{date}.csv"
        if not filename.exists():
            return [], ""

        data = pd.read_csv(filename)
        relevant_history = []
        relevant_doc = ""
        for i in range(len(data)):
            if (data["user_id"][i]) == self.user_id:
                relevant_history.append(("human", data["query"][i]))
                relevant_history.append(("ai", data["response"][i]))
                relevant_doc += data["query"][i] + "\n" + data["response"][i] + "\n\n"

        if len(relevant_history) > 2 * limit:
            relevant_history = relevant_history[-(2 * limit):]
            relevant_doc = relevant_doc[-500:]
        print(f"[INFO] Found {len(relevant_history)} relevant history entries.")
        return relevant_history, relevant_doc
        