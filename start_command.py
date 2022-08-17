@bot.on_message(filters.command("start", ["!", "/"]))
def connect(chat, m):
	try:
		userID = m.chat.id
		bot.send_message(userID, 'Привет! Я умею скачивать видео из YouTube. Отправь мне ссылку — а я отправлю тебе скачанное видео')
	except Exception as e:
		print(e)