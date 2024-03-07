import pandas as pd


class Load_file:
    def __init__(self, file):
        self.file = file
        self.low_band = 55
        self.high_band = 127
        self.data = self._to_dataframe()

    def _to_dataframe(self):
        value = []
        for row_num in range(3, 1078):
            d = self._cell_to_frame(self.file.iloc[row_num, :])
            value.append(d)

        result = pd.DataFrame(value, columns=range(len(value[0])), index=range(len(value)))
        return result

    def _cell_to_frame(self, cell):
        row = []
        cell = str(cell)[self.low_band:self.high_band]
        for number in cell.split(" "):
            if number == "":
                continue
            else:
                row.append(float(number))
        return row

