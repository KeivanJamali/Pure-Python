class HW1_5:
    def __init__(self, colors) -> None:
        self.saving_list = []
        self.colors = colors
        self.leftover = None

    def cash(self, save_obj, name) -> None:
        self.saving_list.append([save_obj, name])

    def leftover_adjust(self, leftover) -> None:
        self.leftover = leftover

    def dynamic(self, leftover, color_prices):
        last_prices = []
        for color in color_prices:
            leftover_new = leftover - color
            if leftover_new < 0:
                leftover_new += color
                last_prices.append(leftover_new)
            color_prices_new = color_prices.copy().remove(color)
            self.dynamic(leftover_new, color_prices_new)

