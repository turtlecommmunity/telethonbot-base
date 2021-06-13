from .. import Turtle
from telethon import events, Button

@Turtle.on(events.NewMessage(incoming=True, pattern="/help"))
async def help(event):
    thebuttonn = [[Button.url("🐢Support Channel🐢",url="https://t.me/turtlecommunitytg")],[Button.url("🐢Github🐢", url="https://github.com/turtlecommunity")]]
    helptext = f"Hey <b>{event.sender.first_name}</b>\nYou can Join Our Support Channel From Below."
    await  Turtle.send_message(event.chat_id,helptext, buttons=thebuttonn,parse_mode="HTML")
