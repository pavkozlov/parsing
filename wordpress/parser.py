import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    section = soup.findAll('section', {'class': 'plugin-section'})[1]
    plugins = section.findAll('article')
    for plugin in plugins:
        h2 = plugin.find('h2')
        rating = plugin.find('span', {'class': 'rating-count'})
        print(h2.text, rating.text)


def main():
    html = get_html('https://ru.wordpress.org/plugins/')
    data = get_data(html)


if __name__ == '__main__':
    main()
