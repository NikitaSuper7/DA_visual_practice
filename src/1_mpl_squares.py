import matplotlib.pyplot as plt

if __name__ == '__main__':
    squares = [1, 4, 9, 16, 25]
    input_val = [1, 2, 3, 4, 5]
    # for sty in plt.style.available:
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()
    ax.plot(input_val, squares, linewidth=3)
    # Назначение заголовка диаграммы и меток осей
    ax.set_title(f"Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=16)

    # Назначение шрифта и делений на осях.
    ax.tick_params(axis='both', labelsize=10)

    plt.show()
