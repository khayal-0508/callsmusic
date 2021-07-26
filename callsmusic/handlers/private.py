from pyrogram import Client
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import Message

from ..helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f'<b>👋🏻 Salam {message.from_user.mention()}!</b>\n\n'
        'Mən @tag1y3v tərəfindən yaradılan "Khan Music Bot"-am, '
        'Mən sizin səsli söhbətinizdə musiqi dinləməyinizə kömək edə bilərəm.'
        '\n\nHazırda istifadə edəcəyiniz əmrlərim bunlardır:\n\n'
        '/play - Yanıt verdiyiniz və ya adını yazdığınız musiqini oxutmaq\n'
        '/pause - Oxunan musiqiyə pauza vermək\n'
        '/resume - Musiqi axınını davam etdirmək\n'
        '/skip - Oxunan musiqini dəyişdirmək\n'
        '/mute - Assistantı səssizə almaq\n'
        '/unmute - Assistantın səsini açmaq\n'
        '/stop - Musiqi axınını sonlandırmaq',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        '🔈 Kanal', url='https://t.me/KhanVlog',
                    ),
                    InlineKeyboardButton(
                        'Qrup 💬', url='https://t.me/KhanChat',
                    ),
                ],
            ],
        ),
    )
