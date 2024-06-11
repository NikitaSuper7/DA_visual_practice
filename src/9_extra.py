import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

if __name__ == '__main__':
    df = pd.read_csv(
        r"""D:\SkyPro_Dev\Django\data_visualization\data\ehmatthes-pcc_2e-078318e\chapter_16\the_csv_file_format\data\sitka_weather_2018_full.csv""",
        encoding='utf-8'
    )
    df['DATE'] = pd.to_datetime(df['DATE'])
    print(df.head())

    # Нанесение данных на диаграмму.
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(2, 2, figsize=(16, 10))

    # Graph_1
    sns.lineplot(x=df['DATE'], y=df['TMAX'], color='red', ax=ax[0, 0])
    sns.lineplot(x=df['DATE'], y=df['TMIN'], color='blue', ax=ax[0, 0])

    # Graph_2
    sns.lineplot(x=df.DATE, y=df.TMAX, color='green', ax=ax[0, 1])
    sns.lineplot(x=df.DATE, y=df.TMIN, color='black', ax=ax[0, 1], legend='brief')

    # Graph_3
    sns.scatterplot(x=df.DATE, y=df.TMAX, color='blue', ax=ax[1, 0], legend='auto')

    # Graph_4
    sns.scatterplot(x=df.DATE, y=df.TMIN, color='pink', ax=ax[1, 1], legend='auto')

    # Выделить цветом диапазон между графикками (Graph_1)
    ax[0, 0].fill_between(df.DATE, df.TMAX, df.TMIN, facecolor='green', alpha=0.2)

    # Форматирование диаграммы.
    plt.title("daily high and low temperatures, july 2018", fontsize=16)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()  # выводит метки дат по диагонали.
    plt.ylabel("Temperature (f)", fontdict={'size': 10})
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()
