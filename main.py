from telethon import TelegramClient, events
import asyncio

from dotenv import load_dotenv
import os
from icecream import ic
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
ALOW_IDS_str = os.getenv("ALOW_IDS")
if ALOW_IDS_str:
    id_list = ALOW_IDS_str.split(",")
    ALOW_IDS = [int(id.strip()) for id in id_list]
else:
    ALOW_IDS = []


client = TelegramClient('user_session.session', api_id, api_hash, device_model='Custom Device', system_version='Custom OS')






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

presentation_text = '''
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
            event_text = event.text.lower().strip()
            event_text_splited = event_text.split()
            presentation_text_formated = presentation_text.format(link=get_link())
            if keyword in event_text:
                await event.reply(presentation_text_formated)
            elif event_text_splited[0] == "/replace_link":
                if len(event_text_splited) != 2:
                    await event.reply("Ведите ссылку в формате '/replace_link ссылка'")
                else:
                    link = event_text_splited[1]
                    write_link(link)
                    await event.reply(f"Записала {link}")
                return 
            elif event_text_splited[0] == "/get_link":
                link = get_link()
                await event.reply(link)
                return  
        except Exception as e:
            await event.reply(main_text)
            await event.reply(presentation_text_formated)
            raise e
            
            
def write_link(link: str):
    with open("link", "w", encoding="utf-8") as file:
        file.write(link)
        
def get_link(path="link"):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as file:
            data = file.read().strip()
            return data
    else:
        return "link_not_defined"
            
async def main():
    print("Запускаем клиент. Авторизуйтесь, если потребуется.")
    await client.start()
    print("Клиент запущен. Ожидаем сообщения...")
    await client.run_until_disconnected()

asyncio.run(main())
