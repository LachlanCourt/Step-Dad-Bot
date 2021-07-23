import discord, sys, random

count = 0
targetLow = 40#50
targetHigh = 50#100
target = random.randint(targetLow, targetHigh)

client = discord.Client()

messages = [
['I saw one of those things from your computer legos the other day', 'creeper.png'],
['I\'m proud of you son', ''],
['You\'re doing great!', ''],
['How about we go out and play catch some time?', ''],
['If you\'re good maybe we can get some icecream after soccer practice', ''],
['I need some help setting up my email', ''],
['What is that eye-pad you keep talking about', ''],
['What does IDK mean?', ''],
['Your mother and I are getting a divorce but I want you to know that we love you very much', ''],

['This is what I call a pro gamer move', ''],
['That\'s pretty pog', ''],
['Are you winning son?', ''],
['Daaaaamn Daniel!', ''],
['Wow that\'s over 9000!', ''],
['Is this loss?', 'spiderman.jpg'],
['Haha like that silly dog, what\'s it called, doog? Haha much wow right?', ''],
['RIP Vine am I right?', ''],
['You know what they say these days, YEET!', ''],
['That\'s lit', ''],
['LOL out loud!', ''],
['What does IDK mean?', ''],

['Haha it\'s a yikes from me', '']
    ]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.author) == "Latch#7069" and str(message.content) == 'shutdown1234':
        await message.channel.send('Goodbye!')
        await client.close()
        return

    global count
    global target
    
    count += 1
    if count == target:
        count = 0
        
        target = target = random.randint(targetLow, targetHigh)
        text, image = getMessage()
        if image == '':
            await message.channel.send(text)
        else:
            await message.channel.send(content=text, tts=False, embed=None, file=discord.File(image, filename=None, spoiler=False), files=None, delete_after=None, nonce=None, allowed_mentions=None)
        

def getMessage():
    temp = messages[random.randint(0, len(messages) - 1)]
    return temp[0], temp[1]

client.run('OAuth Goes Here')
print('Closed')
