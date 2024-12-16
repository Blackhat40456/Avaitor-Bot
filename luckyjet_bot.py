from config import BOT, single_button, send_session_start, send_session_close
import asyncio, random, time, traceback, sys


ID = '@AvaitorGreenSignalsbyReDHaT'

status = 'Stopped'
allow_run = False


async def send_signal():
    M1 = await BOT.sendMessage(ID, '\U0001F6A8 Checking new signal...')
    await asyncio.sleep(random.randint(110, 130)) # 120
    M2 = await BOT.sendPhoto(ID, 'static/jet_pic.jpg', f'\U0001F3AF Enter confirmed \U0001F3AF\n\U0001F4F1 Site: \U0001F449 <a href="https://1wnurc.com/casino/list?open=register#mth6">Click Here To Play</a> \U0001F448\n\n\U0001F4B0 Exit at {random.randint(130, 250) / 100}x\n\nUSE PROMO: <code>ReDHaT</code> and get 500% Bonus', parse_mode='HTML', reply_markup=single_button('Play Here', 'http://1wdpnk.life/v3/reg-form-aviator#mth6'))
    await asyncio.sleep(random.randint(50, 70)) # 60
    isWIN = bool(random.choice([0] * 20 + [1] * 80))
    M3 = await BOT.sendMessage(ID, '\u2705 <b>WIN</b> \u2705' if isWIN else '\U0000274C <b>LOSS</b> \U0000274C', reply_to_message_id=M2.message_id, parse_mode='HTML')
    if isWIN: await BOT.sendSticker(ID, 'static/grumpy_tiger_money.tgs')
    await asyncio.sleep(random.randint(5, 15)) # 10
    print('[+] Signal Sent', flush=True)


async def send_promo():
    await BOT.sendPhoto(ID, 'static/promo_pic.jpg', 'Create an Account on <a href="https://1wnurc.com/casino/list?open=register#mth6">1WIN</a> & use my promo code - <code>ReDHaT</code> and get 500% bonus\U0001F44D\U0001F4AA\n\nAfter creating your account, send your UID number to <a href="https://t.me/ReDHaT4O4">@ReDHaT4O4</a>\n\n\u26A0\ufe0fDon\'t forget to use my promo code: <code>ReDHaT</code>\n500% Bonus Link: https://1wnurc.com/casino/list?open=register#mth6', parse_mode='HTML', reply_markup=single_button('Create Account', 'https://1wnurc.com/casino/list?open=register#mth6'))


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
