import requests


payload = {
   'content' : "@everyone spamされています!!"
}

header = {
   'authorization' : 'Tokenをここに'
}

for i in range (10000) :
    r = requests.post('https://discord.com/api/v9/channels/チャンネルID/messages', data=payload, headers=header)