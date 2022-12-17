import requests


def get_most_intelligent_superhero(*superhero):
    superhero_unit = 0
    intelligence_list = []
    response = requests.get("https://akabab.github.io/superhero-api/api/all.json").json()
    superhero_list = [*superhero]
    for superhero in superhero_list:
        for superhero_unit in range(len(response)):
            if superhero == response[superhero_unit]['name']:
                intelligence_list.append(response[superhero_unit]['powerstats']['intelligence'])
            superhero_unit += 1
        name_and_intelligence = list(zip(intelligence_list, superhero_list))
    return max(name_and_intelligence)[1]


print(f"Самый умный супергерой: {get_most_intelligent_superhero('Hulk', 'Captain America', 'Thanos')}")
