import requests

def shorter_link(full, link_n):
    API = '2141d1a732e7b0beee169982ac4cda58d417e'
    BASE = 'https://cutt.ly/api/api.php'

    pay = {'key': API, 'short': full, 'name': link_n}
    response = requests.get(BASE, params=pay)
    data = response.json()

    try:
        title = data['url']['title']
        shorter_link = data['url']['shortLink']

        print('Title : ', title)
        print('Link : ', shorter_link)
    except KeyError:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter your link : ')
name = input('Name your link : ')

shorter_link(link, name)
