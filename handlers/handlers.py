from aiogram import F, Router, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, ContentType
import keyboards as kb
router = Router()

t = '''Привет, вот правила игры в Wordle:

1. Цель игры: Отгадать загаданное слово за определенное количество попыток.

2. Игровое поле: Игровое поле состоит из семи строк, в каждой из которых показано, были ли угаданные буквы на своем месте (зеленый цвет), присутствуют ли угаданные буквы, но на другом месте (желтый цвет), или вообще нет угаданных букв (серый цвет).

3. Количество попыток: У игрока есть семь попыток, чтобы угадать слово.

4. Угадывание слова: Игрок вводит слово, которое, по его мнению, является загаданным. После каждой попытки система сообщает, какие буквы правильно угаданы и находятся на своем месте(Подсвечены зеленым цветом), какие буквы присутствуют в загаданном слове, но стоят на другом месте(Подсвечены желтым цветом), и каких букв в загаданном слове нет вовсе(Подсвечены серым цветом).

5. Конец игры: Игра заканчивается, когда игрок угадывает слово или когда он исчерпывает все семь попыток.

6. Стратегия: Игрок должен использовать информацию от предыдущих попыток, чтобы лучше выбирать следующие буквы и угадать слово за минимальное количество ходов.

Это основные правила игры в Wordle!'''

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'{t}',reply_markup=kb.main)

@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer(t)

# @router.message(F.photo)
# async def send_photo_file_id(message: Message):
#     photo_data = message.photo[-1]
#     await message.answer(f'{photo_data}')
  
@router.message(lambda msg: msg.text == 'Играть')
async def send_photo(message: types.Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAOYZh1aBxYpBmh4kC_SF0XwctPvxmEAAvzdMRtNyfBI6OB8VbzWBgEBAAMCAAN4AAM0BA')

@router.message(lambda msg: msg.text == 'Правила')
async def pravila(message: types.Message):
    await message.answer(t)

        
