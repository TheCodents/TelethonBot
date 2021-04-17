from .. import app
from telethon import events, Button

@app.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/TheCodents")],
                        [Button.inline("Inline Button",data="example")]
                    ])

@app.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    await event.edit("You clicked a button!")