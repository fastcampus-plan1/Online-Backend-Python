import discord
from scraper import Scraper

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def build_message(item):
    embed = discord.Embed(type="rich", title=item["name"])
    embed.description = item["brand"]
    embed.set_thumbnail(url=item["image"])
    embed.url = item["url"]
    embed.add_field(name="원래 가격", value=item["original_price"], inline=True)
    embed.add_field(name="할인 가격", value=item["sale_price"], inline=True)
    return embed

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith("!타임세일"):
        # 무신사 타임세일 결과를 출력한다.
        scraper = Scraper()
        results = scraper.do()

        embeds = []
        for item in results:
            embeds.append(build_message(item))
        
        await message.channel.send(embeds=embeds)


client.run('PUT YOUR BOT TOKEN')
