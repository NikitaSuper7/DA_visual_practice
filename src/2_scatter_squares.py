import matplotlib.pyplot as plt

if __name__ == '__main__':
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()

    x_val = [1, 2, 3, 4, 5]
    y_val = [1, 4, 9, 16, 25]

    ax.scatter(x_val, y_val, s=200)

    # Назначение заголовка диаграммы и меток.
    ax.set_title('Square Numbers', fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Values", fontsize=14)

    # Назначение размера шрифта и делений на осях.
    ax.tick_params(axis='both', which='major', labelsize=14)

    plt.show()
