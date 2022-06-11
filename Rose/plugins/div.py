from Rose import app
from Rose.utils.commands import *

@app.on_message(command("test"))
async def plug(_, message):
    szteambots = await message.reply_text(text="Hello I am rose"
    )
    supun = """
I'm a group management bot with some useful features.
@divmas    
    """
    await szteambots.edit_text(supun)

__MODULE__ = "div"
__HELP__ = """  
/div - test cmd here
"""
