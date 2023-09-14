import matplotlib.pyplot as plt
from IPython import display
import time


plt.ion()
start_time = time.time()


def plot_graph(scores, mean_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training....')
    plt.xlabel(f'Number of Games, Time lapsed = {time.time() - start_time}')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores) - 1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) - 1, mean_scores[-1], str(mean_scores[-1]))