from telethon import TelegramClient
from tqdm import tqdm

#need to sign in once for a session
#can't share api_id and api_hash
api_id = 'your_api_id'
api_hash = 'your_api_hash'

client = TelegramClient('anon', api_id, api_hash)

async def downloadFiles():
	print('retrieving messages...')
	#channel link is test_python_123 which contains 3 media files
	messages = await client.get_messages('test_python_123', None)
	print(len(messages))
	for msg in tqdm(messages):
		if msg.media is not None:
			print('downloading...')
			await client.download_media(msg)

with client:
	print('signing in...')
	client.loop.run_until_complete(downloadFiles())
