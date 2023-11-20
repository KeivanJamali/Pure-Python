import pandas as pd
from tqdm.auto import tqdm
from collections import OrderedDict


class Dataloader:
    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data
        self.dict = self._make_dict()

    def _make_dict(self):
        data_dict = OrderedDict()
        for index, value in tqdm(self.data.iterrows()):
            if value.FromNodeId in data_dict.keys():
                data_dict[value.FromNodeId].update({value.ToNodeId: value.TravelTime})
            else:
                data_dict[value.FromNodeId] = {value.ToNodeId: value.TravelTime}
        return OrderedDict(sorted(data_dict.items(), key=lambda x: x[0]))
