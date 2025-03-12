from telethon import TelegramClient, events
import asyncio

from dotenv import load_dotenv
import os
from icecream import ic
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")


client = TelegramClient('user_session.session', api_id, api_hash, device_model='Custom Device', system_version='Custom OS')

link = "https://docs.google.com/presentation/d/131zIIWNSkh6XKrf15oc40yfSPbNc1SiSkqck7eQLEYk/edit?pli=1#slide=id.g33f141938f8_3_115"

main_text = '''
                HI! 🌞
Я r2d2, гибридный интеллект Leo (Ивана Аркадьевича). 🚀

Я - его премодерируемый (not real-time) AI/HI-чатбот, поэтому со мной можно общаться как будто я и есть он. Все сообщения он тоже видит через API и, если сочтет нужным, ответит сам [как, собственно, при обычном личном общении, у вас, у homo sapience, принято насколько я знаю 🙂]

Я могу делать разные штуки. Например, помочь организовать созвон/встречу. 📅

Для этого укажи, пожалуйста, какие у тебя (Вас? как удобнее?) есть опции по времени. ⏰
Лучше если укажешь не точечно, а возможные диапазоны. Например, когда "зеленые" зоны (максимально удобно) или когда "красные" (занято 100%). 🚦

Отвечать можно в аудио, если нет времени писать буквами 🎤
#VoiceFriendlyInterface

————
This is semi-automatically generated message.
You've got it because @OrangeRedLeo/@reallyAI give me access to you telegram ID via HI-prompt (Hybrid Intelligence prompt).
I'll try to do my best to help your communication 😊
'''

presentation_text = f'''
                ✨ Также хотела сообщить, что прямо сейчас мой пользователь выступает на конференции со своей чудо-презентацией! 🎤📊

🔗 Вот ссылка: {link}

Можете ознакомиться и оценить! 🚀😊


//Ягодка r2d2🌞 (Leo's HI assistant)
'''
keyword = "през"

@client.on(events.NewMessage)
async def handler(event):
    ic(event)
    if event.is_private and not event.out:
        try:
            user = await client.get_entity(event.sender_id)
            ic(user)
            event_text = event.text.lower().strip()
            if keyword in event_text:
                await event.reply(presentation_text)
        except Exception as e:
            await event.reply(main_text)
            await event.reply(presentation_text)
            
            
async def main():
    print("Запускаем клиент. Авторизуйтесь, если потребуется.")
    await client.start()
    print("Клиент запущен. Ожидаем сообщения...")
    await client.run_until_disconnected()

asyncio.run(main())
