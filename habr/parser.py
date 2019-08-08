import requests
from bs4 import BeautifulSoup


def get_html(url):
    result = requests.get(url)
    return result.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    h1 = soup.find('h1', {'class': 'page-header__info-title'})
    a = soup.find('a', {'href': 'https://habr.com/ru/post/461939/'})
    navbar = soup.find('ul', {'id': 'navbar-links'})
    li = navbar.find('li').find('a').text
    print(li)


def main():
    html = get_html('https://habr.com/ru/hub/python/')
    get_data(html)


if __name__ == '__main__':
    main()
