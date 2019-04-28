import json, urllib.request
import pandas as pd

stock = 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json'
data = urllib.request.urlopen(stock).read()

output = json.loads(data)

messages = []
for message in output['messages']:
    id = message['id']
    body = message['body']
    date = message['created_at']

    result = {'id': id, 'body': body, 'date': date}
    messages.append(result)

df = pd.DataFrame(messages, columns=['id', 'body', 'date'])
df.to_csv('test.csv', encoding='utf-8', index=False)
