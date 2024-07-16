import requests

def shorter_link(full, link_n):
    API_KEY = '2141d1a732e7b0beee169982ac4cda58d417e'
    BASE_URL = 'https://cutt.ly/api/api.php'

    pay = {'key': API_KEY, 'short': full, 'name': link_n}
    response = requests.get(BASE_URL, params=pay)
    data = response.json()

    try:
        title = data['url']['title']
        shorter_link = data['url']['shortLink']

        print('Title : ', title)
        print('Link : ', shorter_link)
    except KeyError:
        status = data['url']['status']
        print('Error Status:', status)

link = input('Enter a Link: ')
name = input('Give your link a name: ')

shorter_link(link, name)
