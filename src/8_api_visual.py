import requests
from plotly.graph_objs import Bar
from plotly import offline

if __name__ == '__main__':
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}

    request = requests.get(url, headers=headers)

    # Сохранение ответа API в переменной^
    response_dict = request.json()
    repo_dicts = response_dict['items']
    stars, labels, repo_links = [], [], []
    for repo_dict in repo_dicts:
        # repo_names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])

        # Для подсказки при наведении на столбец:
        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner} <br />{description}"
        labels.append(label)

        # Ссылка:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

    # построение визуализации.
    data = [
        {
            'type': 'bar',
            'x': repo_links,
            'y': stars,
            'hovertext': labels,
            'marker': {
                'color': 'rgb(60, 100, 150)',
                'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
            },
            'opacity': 0.6,
        }
    ]

    my_layout = {
        'title': 'Most-Stared Python Projects on github',
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
                  },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14}
                },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')
