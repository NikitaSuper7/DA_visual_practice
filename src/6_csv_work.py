import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    df = pd.read_csv(
        r"""D:\SkyPro_Dev\Django\data_visualization\data\ehmatthes-pcc_2e-078318e\chapter_16\the_csv_file_format\data\sitka_weather_2018_full.csv""",
        encoding='utf-8'
    )
    df['DATE'] = pd.to_datetime(df['DATE'])
    print(df.head())

    # Нанесение данных на диаграмму.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots()

    ax.plot(df.DATE, df.TMAX, c='red')
    ax.plot(df.DATE, df.TMIN, c='blue')

    # Выделить цветом диапазон между графикками
    plt.fill_between(df.DATE, df.TMAX, df.TMIN, facecolor='green', alpha=0.2)

    # Форматирование диаграммы.
    plt.title("daily high and low temperatures, july 2018", fontsize=16)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate() # выводит метки дат по диагонали.
    plt.ylabel("Temperature (f)", fontdict={'size': 10})
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()
