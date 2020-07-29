import discord

kadaidesu_list = []
client = discord.Client()



async def kadai(message):
    string = 'コマンドリストhere!\n'
    for command in Commands: 
        string += 'ﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜ\n'
        string += '{}: {}\n'.format('!' + command, Commands[command]['info'])
        string += '    使い方：{}\n'.format(Commands[command]['usecommand'])
        string += '    省略形：{}\n'.format(Commands[command]['unti'])
        string += 'ﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜﾖﾜ\n'

    await message.channel.send(string)

async def newkadai(message):
    msg = message.content.split(' ')
    try:
        title, deadline, memo = msg[1:]

        kadaidesu_list.append({
            'title': title,
            'deadline': deadline,
            'memo': memo
        })

        await message.channel.send('課題を追加しましたお＾＾')
    except:
        await message.channel.send('入力形式が間違っています。wwwwww')


async def kadaikesu(message):
    msg = message.content.split(' ')
    for i in range(len(kadaidesu_list)):
        if kadaidesu_list[i]['title'] == msg[1]:
            kadaidesu_list.pop(i)
            await message.channel.send('課題を削除したお＾＾')


async def kadailist(message):
    string = '課題一覧だお^^\n'
    for i, assignment in enumerate(kadaidesu_list):
        string += '------------------------\n'
        string += '{}. {}\n'.format(i + 1, assignment['title'])
        string += '締切: {}\n'.format(assignment['deadline'])
        string += '備考: {}\n'.format(assignment['memo'])
        string += '------------------------\n'

    string += '現在、{}個の課題が出されているお^^'.format(len(kadaidesu_list))
    await message.channel.send(string)


TOKEN = 'NzM3ODIyMDEzNTQ4MjY1NTMz.XyC8TA.DgdrvEFH8u5LpBvP7Fe-NMw9Oj0'


Commands = {
    'commandlist':{
        'info':'この説明をだすよ＾＾',
        'usecommand':'!commandlist',
        'unti':'!clist',
        'func': kadai
    },
    'newkadai': {
        'description': '新しい課題を追加します。',
        'usecommand': r'!newkadai \{タイトル\} \{締切\} \{備考\}',
        'unti': '!nk',
        'func': newkadai
    },
    'kadaikesu':{
        'info':'課題消すよ。こんな感じで処理できるといいね＾＾',
        'usecommand':r'kadaikesu\{課題名\}',
        'unti':'!kkesu',
        'func': kadaikesu
    },
    'kadailist':{
        'info':'登録されている課題一覧を表示するよ',
        'usecommand':'!kadailist',
        'unti':'!klist',
        'func': kadailist
    },
}
    
@client.event
async def on_ready():
     print('課題ちゃん参上')


@client.event
async def on_message(message):
  msg = message.content.split(' ')

  if message.author.bot:
      return
  for command in Commands:
      if msg[0] in ['!' + command, Commands[command]['unti']]:
          await Commands[command]['func'](message)

client.run('NzM3ODIyMDEzNTQ4MjY1NTMz.XyC8TA.DgdrvEFH8u5LpBvP7Fe-NMw9Oj0')
          
