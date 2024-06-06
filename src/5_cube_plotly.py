from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import  offline

class Die:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        """Взвращает случайное число от 1 до числа граней."""

        return randint(1, self.num_sides)


if __name__ == '__main__':
    die_1 = Die(6)
    die_2 = Die(6)
    results = []

    for rull_num in range(1000):
        result = die_1.roll() + die_2.roll()
        results.append(result)

    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides
    for value in range(2, max_result+1):
        frequenciy = results.count(value)
        frequencies.append(frequenciy)

    # Визуализация результатов
    x_val = list(range(2, max_result+1))
    data = [Bar(x=x_val, y=frequencies)]

    x_axis_config = {'title': 'Result', 'dtick': 1}
    y_axis_config = {'title': 'Frequency of Result'}

    # Класс Layout() возвращает объект, который задает макет и конфигурацию диаграммы в целом.
    my_layout = Layout(title= "Result of rolling two D6 1000 times",
                       xaxis=x_axis_config, yaxis=y_axis_config)
    # Строит Диаграмму.
    offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
