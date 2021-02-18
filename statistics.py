import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt


def create_histogram_mat(data):
    # [(1, 'a'), (2, 'b')]
    # Prepare data
    x, y = prepare_data_for_histogram(data)
    fig, ax = plt.subplots()
    n_bins = len(data)
    count_color = np.random.rand(1, n_bins)

    # Make histogram
    ax.bar(x, y, color=count_color, align='edge', width=0.5)
    for index, count in enumerate(y):
        ax.text(index, count, int(count), horizontalalignment='center', verticalalignment='bottom',
                fontdict={'fontweight': 500, 'size': 12})

    # Decoration
    fig.set_figwidth(16)
    fig.set_figheight(8)
    fig.set_facecolor('floralwhite')
    plt.title("Количество сообщений в телеграмме", fontsize=22)
    plt.ylabel('# Количество сообщений')
    plt.ylim(0, data[n_bins-1][1])
    ax.set_facecolor('seashell')

    plt.show()


def create_histogram_dash():
    pass


def prepare_data_for_histogram(data):
    x = np.array([])
    y = np.array([])
    for i in data:
        x = np.append(x, i[0])
        y = np.append(y, i[1])
    return x.astype(int), y.astype(int)
