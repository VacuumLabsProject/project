import matplotlib.pyplot as plt


def show_plot(x_vals, y_vals):
    plt.plot(x_vals, y_vals)
    plt.ylabel("P, Па")
    plt.xlabel("t, с")
    plt.yscale('log')
    plt.show()
