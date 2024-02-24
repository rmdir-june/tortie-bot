import requests
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
import time
import os


#worker: python3 main.py


try:
    def tortie_requests():
        headers = {
            'User-Agent': 'windows:Id6gOqcg_2e53LwFfznNDQ:v.1.0.0: (by u/Achilles-Foot'
        }
        try:
            tortiesjson = requests.get("https://www.reddit.com/r/torties/top.json", headers=headers).json()
            toppost_imagelink = tortiesjson['data']['children'][0]['data']['url_overridden_by_dest']
            toppost_title = tortiesjson['data']['children'][0]['data']['title']
            return toppost_title, toppost_imagelink
        except KeyError:
            time.sleep(1)
            return tortie_requests()


    def tortie_parse(toppost_title, toppost_imagelink):
        print(toppost_imagelink)
        alt = f'r/torties - {toppost_title}'
        r = requests.get(toppost_imagelink)
        soup = BeautifulSoup(r.content)
        img = soup.find(alt=alt)
        print(img['src'])

        with open("test.jpg", "wb") as f:
            f.write(requests.get(img['src']).content)


    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    while True:
        title, imagelink = tortie_requests()


        @client.event
        async def on_ready():
            print(f'We have logged in as {client.user}')
            tortie_requests()
            tortie_parse(title, imagelink)
            channel = client.get_channel(1163200431103684639)
            with open('test.jpg', 'rb') as f:
                picture = discord.File(f)
                await channel.send(file=picture)


        print(os.environ.get('TORTIE_TOKEN'))
        client.run(os.environ.get('TORTIE_TOKEN'))
        time.sleep(20)
except TypeError:
    pass
