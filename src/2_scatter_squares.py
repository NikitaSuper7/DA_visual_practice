import matplotlib.pyplot as plt

if __name__ == '__main__':
    while True:
        print(f"""
        1 - 5 scatters on plot
        2 - automaticly range scatters
        """)
        diagram = int(input("Please enter num of diagram: "))
        if diagram == 1:
            # 1 - 5 scatters on plot
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
        elif diagram == 2:
            x_val = list(range(1, 1001))
            y_val = list(map(lambda x: x**2, x_val))

            plt.style.use('seaborn-v0_8')
            fig, ax = plt.subplots()
            ax.scatter(x=x_val, y=y_val, s=10, c=y_val, cmap=plt.cm.Blues)

            # Назначение заголовка диаграмм и меток.
            ax.set_title('Square Numbers', fontsize=24)
            ax.set_xlabel('Value', fontsize=14)
            ax.set_ylabel('Square of values', fontsize=14)

            # Назначение размера шрифта и делений на осях.
            ax.tick_params(axis='both', which='major', labelsize=10)

            # Назначение диапазона для каждой оси.
            ax.axis([0, max(x_val)+100, 0, max(y_val)+100])
            plt.savefig(r'C:\Users\nike7\OneDrive\Pictures\ex_1.png', bbox_inches='tight')
            plt.show()


        again = input("Do you want to continue (y/n)? ").lower()
        if again != 'y':
            print("Thank you")
            break