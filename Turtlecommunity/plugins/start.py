import requests
import os
from TurtleCommunity import Turtle
from PIL import Image
from telethon import events

myimage = "https://telegra.ph/file/e74be9e4a2ffca7699dff.jpg"
startmessage = "Hey!! Thanks For Using This As Base For Your Bot\nVisit @turtlecommunitytg For Any Help"

@Turtle.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    r = requests.get(myimage, allow_redirects=True)
    open('alive.jpg', 'wb').write(r.content)

    await Turtle.send_file(event.chat_id, 'alive.jpg', caption=startmessage, link_preview=False)