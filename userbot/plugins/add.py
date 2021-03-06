"""Invitea gli utenti nel seguente Gruppo   
Comando: .invita <Utenti>"""

from telethon import functions

from userbot.utils import admin_cmd

"""Invita gli utenti nel seguente gruppo
Comando: .invita <Utente/i>"""

from telethon import functions

from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd


@borg.on(admin_cmd(pattern="invita ?(.*)"))
@borg.on(sudo_cmd(pattern="invita ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_or_reply(
            event, "`.invita` nel gruppo, non in Privata!"
        )
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Invitati con Successo!")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Invitati con Successo!")
