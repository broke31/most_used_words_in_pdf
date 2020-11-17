from textwrap import wrap
import matplotlib.pyplot as plt

from manupulate_text import split_freq


def plot_and_save_graphic(freq_to_plot, name_file):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    title = ax.set_title("\n".join(wrap(name_file, 60)))
    fig.tight_layout()
    title.set_y(1.05)
    fig.subplots_adjust(top=0.8)
    plt.xticks(range(len(freq_to_plot)), [val[0] for val in freq_to_plot])
    plt.xticks(rotation=90)
    plt.tight_layout()
    labels, values = split_freq(freq_to_plot)
    plt.bar(labels, values, color='blue')

    for i in range(len(values)):
        plt.annotate(str(values[i]), xy=(labels[i], values[i]), ha='center', va='bottom')
    plt.savefig("figures/" + name_file + ".png", bbox_inches="tight")
    plt.show()