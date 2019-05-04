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

        elif message.content.startswith(PREFIX + "secret"):
            print("Secret called. " + message.author.display_name + " is curious")
            await message.channel.send(random.choice([":wink:", "Shhhh", ":thinking:"]))
        
        #Fallback unrecognised commands
        else:
            print("Unrecognised input detected:", message.content)
            await message.channel.send("Error: Command not recognised. Try " + PREFIX + "help")

    # If message from a specific person, 1/500 chance of reacting "very cool"
    if message.author == "109139923247841280":
        if random.randrange(1, 500) == 1:
            await message.add_reaction("🇻")
            await message.add_reaction("🇪")
            await message.add_reaction("🇷")
            await message.add_reaction("🇾")
            await message.add_reaction("🇨")
            await message.add_reaction("🇴")
            await message.add_reaction("🅾")
            await message.add_reaction("🇱")
            print("Reacted 'very cool' to Gordon's message of", message.content)


client.run("I'm not giving you my token >:P")
