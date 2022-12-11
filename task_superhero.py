import requests
URL = "https://akabab.github.io/superhero-api/api/all.json"

def superhero_requests(url):
    responce = requests.get(url)
    data = responce.json()
    return data
def parser_hero(name_hero: list):
    superhero_intellect = {}
    for i in superhero_requests(URL):
        if i['name'] in name_hero:
            superhero_intellect[i['name']] = int(i['powerstats']['intelligence'])
    win_hero = [key for (key, value) in superhero_intellect.items() if value == max(superhero_intellect.values())][0]

    print(f"Самый интелектуальный супергерой {win_hero}, его интелект составляет: {superhero_intellect[win_hero]}")

if __name__ == '__main__':
    parser_hero(['Hulk', 'Captain America', 'Thanos'])
