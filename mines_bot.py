from config import BOT, single_button, send_session_start, send_session_close
import asyncio, random, time, traceback, sys


ID = '@MinesvipsignalsbyReDHaT'

status = 'Stopped'
allow_run = False


def get_box(stars : int = 4):
    bxi = ['\U0001F7E6' for _ in range(25)]
    for k in random.sample(list(range(len(bxi))), stars): bxi[k] = '\u2B50\uFE0F'
    for t in range(5): bxi.insert(5 * (t + 1) + t, '\n')
    return ''.join(bxi)[:-1]


async def send_signal():
    M1 = await BOT.sendMessage(ID, '\U0001F6A8 Checking new signal...')
    await asyncio.sleep(random.randint(110, 130)) # 120
    M2 = await BOT.sendMessage(ID, '\u2705 CONFIRMED ENTRY!\n\nAttempts: 4\n\n\U0001F449 <a href="https://1wzlcz.life/casino/play/1play_1play_mines">Play Here!</a>\n\n' + get_box() + '\n\n\u2705 Tutorial\n\U0001F451 <a href="https://1wnurc.com/casino/list?open=register#mth6">Mines VIP</a>\nPromoCode: <code>ReDHaT</code> use this promo code and get 500% bonus', parse_mode='HTML', reply_markup=single_button('Play Here', 'https://1wzlcz.life/casino/play/1play_1play_mines'), disable_web_page_preview=True)
    await asyncio.sleep(random.randint(50, 70)) # 60
    isWIN = bool(random.choice([0] * 20 + [1] * 80))
    M3 = await BOT.sendMessage(ID, '\u2705 <b>GREEENNNNN</b> \u2705' if isWIN else '\U0000274C <b>LOSS</b> \U0000274C', reply_to_message_id=M2.message_id, parse_mode='HTML')
    if isWIN: await BOT.sendSticker(ID, 'static/grumpy_tiger_money.tgs')
    await asyncio.sleep(random.randint(5, 15)) # 10
    print('[+] Signal Sent', flush=True)


async def send_promo():
    await BOT.sendPhoto(ID, 'static/mines_promo_pic.jpg', 'Create an Account on <a href="https://1wnurc.com/casino/list?open=register#mth6">1WIN</a> & use my promo code - <code>ReDHaT</code> and get 500% bonus\U0001F44D\U0001F4AA\n\nAfter creating your account, send your UID number to <a href="https://t.me/ReDHaT4O4">@ReDHaT4O4</a>\n\n\u26A0\ufe0fDon\'t forget to use my promo code: <code>ReDHaT</code>\n500% Bonus Link: https://1wnurc.com/casino/list?open=register#mth6', parse_mode='HTML', reply_markup=single_button('Create Account', 'https://1wnurc.com/casino/list?open=register#mth6'))


async def bot_main():
    global status
    while 2 + 2 != 5:
        try:
            await asyncio.sleep(5)
            if allow_run:
                status = 'Running'
                await send_session_start(ID)
                while allow_run:
                    await send_signal()
                await send_session_close(ID)
                await send_promo()
                status = 'Stopped'
        except KeyboardInterrupt: sys.exit(1)
        except: 
            await asyncio.sleep(5)
            print(traceback.format_exc(), flush=True)


run = lambda: asyncio.run(bot_main())

if __name__ == '__main__':
    allow_run = True
    run()
