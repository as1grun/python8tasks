import requests
import random
import json
from character import Character
from episode import Episode

character_id = random.randint(1, 826)

url = f'https://rickandmortyapi.com/api/character/{character_id}'
response = requests.get(url)

if response.status_code == 200:
    character_data = response.json()
    print(character_data)
else:
    print(f"Error: {response.status_code}")


print(character_data)
print("Keys:", character_data.keys())


file_name = f'info_character_{character_id}.json'
with open(file_name, 'w') as file:
    json.dump(character_data, file)

episode_urls = character_data.get("episode", [])

file_name_episodes = f'all_episodes_with_character_{character_id}.txt'
with open(file_name_episodes, 'a') as file:
    for episode_url in episode_urls:
        file.write(episode_url + '\n')

episode_response = requests.get('https://rickandmortyapi.com/api/episode/1')
episode_data = episode_response.json()
print(" ", episode_data.keys())
episode_objects = []
for episode_url in episode_urls:
    episode_response = requests.get(episode_url)
    if episode_response.status_code == 200:
        episode_data = episode_response.json()
        episode_objects.append(Episode(**episode_data))
    else:
        print(f"Error retrieving episode data: {episode_response.status_code}")
