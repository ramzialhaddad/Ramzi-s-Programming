# https://discordapp.com/oauth2/authorize?client_id=670763933447094337&scope=bot&permissions=19990528

import discord
from gtts import gTTS
import os

token = open("token.txt", "r").read()

client = discord.Client()

@client.event
async def on_ready():
	print("We are logged into the matrix")

@client.event
async def on_message(message):
	alfredServerGuild = client.get_guild(670748850851676241)
	generalVoiceChannel = client.get_channel(670748850851676245)

	print("In {} the person {} said {}".format(message.channel, message.author, message.content))

	if "alfred go home" in message.content.lower():
		await client.close()

	elif "hello alfred" in message.content.lower():
		await message.channel.send("Hello!")

	elif "alf say" in message.content.lower()[:7]:
		await message.channel.send(message.content[8:])

	elif "alf tts" in message.content.lower()[:7]:
		text = message.content[8:]
		try:
			os.remove("tts.wav")
		except:
			pass
		tts = gTTS(text)
		tts.save('tts.wav')

		vc = alfredServerGuild.voice_client
		try:
			if vc.is_playing():
				vc.stop()
		except:
			pass
		try:
			await generalVoiceChannel.connect()
		except:
			await alfredServerGuild.get_member(670763933447094337).move_to(generalVoiceChannel)
		vc = alfredServerGuild.voice_client
		vc.play(discord.FFmpegPCMAudio("tts.wav"))
		vc.volume = 70

client.run(token)