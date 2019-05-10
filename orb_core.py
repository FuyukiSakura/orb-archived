"""
Use the following link to add the bot:
https://discordapp.com/oauth2/authorize?client_id=569758271930368010&scope=bot&permissions=64
"""

# Imports libraries needed
import discord
import random
print("Libraries successfully loaded")

# Sets prefix and client
client = discord.Client()
PREFIX = 'orb.'
COMMANDS = [
    ("help", "Displays help blurb", "None"), 
    ("commands", "Lists all commands", "None"), 
    ("ping", "Pings the bot, with various responses", "None")
]
MESSAGE = discord.Game("with orbs. Try orb.help")

# Displays boot complete message
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=MESSAGE)
    print('Bot startup successful. Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Ignores self
    if message.author == client.user:
        return

    # Checks for command prefix
    if message.content.startswith(PREFIX):
        # Bot status ping
        if message.content.startswith(PREFIX + "ping"):
            print("Ping received from", message.author.display_name)
            await message.channel.send(random.choice(["Hello!", "Ping!", "Ping received", "Pong!"]))

        # Orb bot help text
        elif message.content.startswith(PREFIX + "help"):
            print("Help request received from", message.author.display_name)
            await message.channel.send("""Orb bot is a bot that does things, for example:
            - Reacts to every message containing the words 'very cool'
            - Responds to pings
            For a list of commands see " + PREFIX + "commands. Developed by xiii™#0013""")
        
        # Lists all commands from the COMMANDS list
        elif message.content.startswith(PREFIX + "commands"):
            output = ""
            print("Commands list requested from", message.author.display_name)
            for command in COMMANDS:
                output += "```Command: " + PREFIX + command[0] + "\n"
                output += "Function: " + command[1] + "\n"
                output += "Arguments: " + command[2] + "```"
            await message.channel.send(output)

        # Secreto
        elif message.content.startswith(PREFIX + "secret"):
            print("Secret called. " + message.author.display_name + " is curious")
            await message.channel.send(random.choice([":wink:", "Shhhh", ":thinking:"]))

        # Meme ban
        elif message.content.startswith(PREFIX + "ban"):
            target = message.content.split(PREFIX + "ban")[1]
            print("Ban on", target, "called for by", message.author.display_name)
            if "ORB" in target.upper() or "<@569758271930368010>" in target:
                await message.channel.send("Pls no ban am good bot")
            elif message.content == (PREFIX + "ban") or message.content == (PREFIX + "ban "):
                await message.channel.send(random.choice(["I can't ban nothing", "Specifiy a person please", "This command doesn't work like that"]))
            else:
                await message.channel.send("Banning " + target)
                await message.channel.send("...")
                await message.channel.send("Shit it didn't work")

        # Bully time
        elif message.content.startswith(PREFIX + "bully") or message.content.startswith(PREFIX + "bulli"):
            print("Bully called for by", message.author.display_name)
            try:
                target = message.content.split(PREFIX + "bully")[1]
            except:
                target = message.content.split(PREFIX + "bulli")[1]
            if "ORB" in target.upper() or "<@569758271930368010>" in target:
                await message.channel.send("You cannot kill me :superiorsmuggie:")
            elif message.content == PREFIX + "bully" or message.content == PREFIX + "bully " or message.content == PREFIX + "bulli" or message.content == PREFIX + "bulli ":
                await message.channel.send(random.choice(["I can't kill nothing", "Sic me on them, boss", "That's not how this works", "Who?"]))
            else:
                await message.channel.send(random.choice([("Bullying " + target), (target + " is a meanie!"), (target + " please stop speaking")]))

        # Ranking
        elif message.content.startswith(PREFIX + "rank"):
            target = message.content.split(PREFIX + "rank")[1]
            print("Ranking", target, "for", message.author.display_name)
            if "ORB" in target.upper() or "<@569758271930368010>" in target:
                await message.channel.send("I'd give me a 10/10")
            else:
                await message.channel.send("I'd give " + target + " a " + str(random.randint(0, 10)) + " out of 10")

        # Illya
        elif message.content.startswith(PREFIX + "illya"):
            print("Illya called by", message.author.display_name)
            if random.randint(1, 50) == 2:
                await message.channel.trigger_typing()
                await message.channel.send(file=discord.File(fp="images/lolice.gif"))
            else:
                await message.channel.trigger_typing()
                await message.channel.send(file=discord.File(fp="images/illya_" + str(random.randint(1, 11)) + ".png"))

        # BDE
        elif message.content.startswith(PREFIX + "bde"):
            print("BDE called by", message.author.display_name)
            await message.channel.send("Isn't that Todd's job?")

        # Fallback unrecognised commands
        else:
            print("Unrecognised input detected:", message.content)
            await message.channel.send("Error: Command not recognised. Try " + PREFIX + "help. Remember, all commands are lowercase!")

    # If message contains very cool, or otherwise a 1/2000 chance of reacting "very cool"
    if "VERY COOL" in message.content.upper() or random.randint(1, 2000) == 1:
        await message.add_reaction("🇻")
        await message.add_reaction("🇪")
        await message.add_reaction("🇷")
        await message.add_reaction("🇾")
        await message.add_reaction("🇨")
        await message.add_reaction("🇴")
        await message.add_reaction("🅾")
        await message.add_reaction("🇱")
        print("Reacted 'very cool' to message", "'" + message.content + "'", "from user", message.author.display_name)
    
    # Girls aren't real
    elif "GIRLS AREN'T REAL" in message.content.upper() or "GIRLS ARENT REAL" in message.content.upper():
        rand_int = random.randint(1, 10)
        if rand_int <= 3:
            await message.add_reaction("🇹")
            await message.add_reaction("🇷")
            await message.add_reaction("🇺")
            await message.add_reaction("🇪")
            print("Reacted 'true' to the message", "'" + message.content + "'", "from user", message.author.display_name)
        elif rand_int > 3 and rand_int <= 5:
            print("Ignored", "'" + message.content + "'", "from user", message.author.display_name)
            pass
        else:
            await message.add_reaction("🇫")
            await message.add_reaction("🇦")
            await message.add_reaction("🇨")
            await message.add_reaction("🇹")
            print("Reacted 'fact' to the message", "'" + message.content + "'", "from user", message.author.display_name)

    # Epic reaction time
    elif "EPIC" in message.content.upper():
        if random.randint(1, 20) == 2:
            await message.add_reaction("🇪")
            await message.add_reaction("🅱")
            await message.add_reaction("🇮")
            await message.add_reaction("🇨")
            print("Reacted 'ebic' to the message", "'" + message.content + "'", "from user", message.author.display_name)
        else:
            await message.add_reaction("🇪")
            await message.add_reaction("🇵")
            await message.add_reaction("🇮")
            await message.add_reaction("🇨")
            print("Reacted 'epic' to the message", "'" + message.content + "'", "from user", message.author.display_name)
    
    # Memory meme
    elif random.randint(1, 2000) == 1:
        print("I remember", message.content)
        await message.channel.send("[Orb will remember that]")

client.run("No steal >:)")
