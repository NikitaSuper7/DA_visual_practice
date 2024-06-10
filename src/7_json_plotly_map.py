# import pandas as pd
from matplotlib import pyplot as plt
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

if __name__ == "__main__":
    filename = r'D:\SkyPro_Dev\Django\data_visualization\data\ehmatthes-pcc_2e-078318e\chapter_16\mapping_global_data_sets\data\eq_data_30_day_m1.json'

    with open(filename, 'r') as file:
        all_eq_data = json.load(file)

    all_eq_dicts = all_eq_data['features']

    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mag = eq_dict['properties']['mag']
        lon = eq_dict['geometry']['coordinates'][0]
        lat = eq_dict['geometry']['coordinates'][1]
        title = eq_dict['properties']['title']
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        hover_texts.append(title)

    # нанесение данных на диаграмму.
    data = [{
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'text': hover_texts, # Текст при наведении на маркер
        'marker': {
            'size': [5 * mag for mag in mags],
            'color': mags,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar': {'title': 'Magnitude'},
        }
    }]
    my_layout = Layout(title='Global Earthquakes')

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='global_earthquakes.html')
