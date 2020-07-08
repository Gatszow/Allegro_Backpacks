import requests
from bs4 import BeautifulSoup


def showlist(_list, _keys):
    iteration = 1
    change_title(_list)
    for element in _list:
        print('{}.'.format(iteration), ' \n'.join(str(element[key]) for key in keys))
        print('')
        iteration += 1


def change_title(_list):
    for i in range(len(_list)):
        _list[i]['title'] = _list[i]['title'].lower().capitalize()
    return _list


result = requests.get('https://allegro.pl/listing?string=plecak&bmatch=baseline-product-'
                      'eyesa2-engag-dict45-fas-1-5-0605')
src = result.content


soup, keys, list_of_backpacks, temporary_list, duplication_list = \
    BeautifulSoup(src, 'lxml'), ['title', 'link'], list(), [], []

for h2 in soup.find_all('h2', {'class': '_9c44d_LUA1k'}):
    for a in h2.find_all('a'):
        title, link = a.text, a['href']
        if title not in duplication_list:
            temporary_list.append(title)
            temporary_list.append(link)
            list_of_backpacks.append(dict(zip(keys, temporary_list)))
            temporary_list.clear()
        duplication_list.append(title)

showlist(list_of_backpacks, keys)
