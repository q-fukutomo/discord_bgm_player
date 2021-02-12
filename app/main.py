import os
import re
import discord
import secret

dirname = os.path.dirname(__file__)
libdir = os.path.join(dirname, 'audio')

client = discord.Client()

@client.event
async def on_ready():
    print('ログイン')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == '!join-bg':
        if message.author.voice is None:
            await message.channel.send(message.author.name + 'は音声チャンネルに接続していません。')
            return

        await message.author.voice.channel.connect()
        await message.channel.send('音声チャンネル`' + message.author.voice.channel.name + '`に接続しました。')
        return
    
    if message.content == '!quit-bg':
        if message.guild.voice_client is None:
            await message.channel.send('音声チャンネルに接続していません。')
            return

        channel = message.guild.voice_client.channel.name
        await message.guild.voice_client.disconnect()
        await message.channel.send('音声チャンネル`' + channel + '`から切断しました。')
        return 

    if re.match('!play-bg.*', message.content):
        if message.guild.voice_client is None:
            await message.channel.send('音声チャンネルに接続していません。')
            return

        result = re.match('!play-bg\s+(.+)', message.content)
        if result:
            audiofile= result.group(1)
            await message.channel.send(audiofile)

            audiofilePath= os.path.join(libdir, audiofile)
            if os.path.isfile(audiofilePath):
                source = discord.FFmpegPCMAudio( audiofilePath, before_options = '-stream_loop -1' ) # -1指定で無限ループ
                message.guild.voice_client.play( source )
                return

            await message.channel.send('音声ファイルが見つかりませんでした。')
            return

        await message.channel.send('音声ファイルを指定してください。')
        return

    if message.content == '!stop-bg':
        if message.guild.voice_client is None:
            await message.channel.send('音声チャンネルに接続していません。')
            return

        message.guild.voice_client.stop()
        return

    if message.content == '!list-bg':
        files = '```\n'
        for file in os.listdir(libdir):
            if file != '.gitkeep':
                files += file + '\n'
        files += '```'
        await message.channel.send(files)
        return


    #オウム返し
    # await message.channel.send(message.content)

# on_messageの定義ここまで

client.run(secret.TOKEN)