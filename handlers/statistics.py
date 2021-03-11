import numpy as np
import calplot
import matplotlib.pyplot as plt


class Graphics:
    @staticmethod
    def build_histogram_math(data, count_1):
        component_histogram = Histogram(data, count_1)
        component_histogram.run()

    @staticmethod
    def calendar_heat_map(data):
        component_calendar = CalendarHeatMap(data)
        component_calendar.run()


class Histogram:
    def __init__(self, data, count_1):
        self._data = data
        self._count_1 = count_1
        self._n_bins = len(self._data)
        self.fig, self.ax = plt.subplots()

        self.main_set_up()

    def __prepare_data(self) -> tuple:
        x = np.array([])
        y = np.array([])
        for i in self._data.items():
            x = np.append(x, i[0])
            y = np.append(y, i[1])
        return x.astype(str), y.astype(int)

    def __prepare_color(self):
        self.count_color = np.random.rand(self._n_bins, 3)
        return self.count_color

    def _create(self, x, y, color_group):
        self.ax.bar(x, y, color=color_group, align='edge', width=0.5)
        for index, count in enumerate(y):
            self.ax.text(index, count, int(count), horizontalalignment='center', verticalalignment='bottom',
                         fontdict={'fontweight': 500, 'size': 12})

    def _generate_appreciate(self):
        self.fig.set_figwidth(16)
        self.fig.set_figheight(8)
        self.fig.set_facecolor('floralwhite')
        plt.title("Количество сообщений в телеграмме", fontsize=22)
        plt.ylabel('# Количество сообщений')
        plt.ylim(0, self._count_1 + 500)
        self.ax.set_facecolor('seashell')

    def main_set_up(self):
        x, y = self.__prepare_data()
        color_group = self.__prepare_color()
        self._create(x, y, color_group)
        self._generate_appreciate()

    @staticmethod
    def run():
        plt.show()

    def __str__(self):
        return 'Создание гистограммы'


class CalendarHeatMap:
    def __init__(self, data):
        self.data = data
        self._create()

    def _create(self):
        calplot.calplot(self.data, edgecolor=None, cmap='YlGn')
        #calmap.calendarplot(self.data, fig_kws={'figsize': (16, 10)},
                            #yearlabel_kws={'color': 'black', 'fontsize': 14}, subplot_kws={
                                                                                    #'title': 'Date of correspondence'})


    @staticmethod
    def run():
        plt.show()

