from config import BOT, single_button, send_session_start, send_session_close
import asyncio, random, traceback, sys

# ✅ PRIVATE CHANNEL ID
ID = -1003890199038  

status = 'Stopped'
allow_run = False


async def send_signal():
    try:
        await BOT.sendMessage(ID, '🚨 Checking new signal...')
        
        await asyncio.sleep(random.randint(110, 130))

        multiplier = round(random.randint(130, 250) / 100, 2)

        M2 = await BOT.sendPhoto(
            ID,
            'static/plane_pic.jpg',
            f'🎯 <b>Entry Confirmed</b> 🎯\n\n'
            f'📱 Site: 👉 <a href="https://1wrjmw.com/casino/list?open=register&p=mth6">Click Here To Play</a> 👈\n\n'
            f'💰 Exit at: <b>{multiplier}x</b>\n\n'
            f'USE PROMO: <code>REDHAT69</code> and get 500% Bonus',
            parse_mode='HTML',
            reply_markup=single_button(
                'Play Here',
                'https://1wrjmw.com/casino/list?open=register&p=mth6'
            )
        )

        await asyncio.sleep(random.randint(50, 70))

        isWIN = bool(random.choice([0] * 20 + [1] * 80))

        await BOT.sendMessage(
            ID,
            '✅ <b>WIN</b> ✅' if isWIN else '❌ <b>LOSS</b> ❌',
            reply_to_message_id=M2.message_id,
            parse_mode='HTML'
        )

        if isWIN:
            await BOT.sendSticker(ID, 'static/grumpy_tiger_money.tgs')

        await asyncio.sleep(random.randint(5, 15))

        print('[+] Signal Sent', flush=True)

    except Exception as e:
        print("Signal Error:", e, flush=True)


async def send_promo():
    try:
        await BOT.sendPhoto(
            ID,
            'static/promo_pic.jpg',
            'Create an Account on <a href="https://1wrjmw.com/casino/list?open=register&p=mth6">1WIN</a>\n\n'
            'Use my promo code - <code>REDHAT69</code>\n'
            'Get 500% Bonus 💪🔥\n\n'
            'After creating your account, send your UID to @ReDHaT4O4\n\n'
            '⚠️ Don\'t forget to use promo: <code>REDHAT69</code>',
            parse_mode='HTML',
            reply_markup=single_button(
                'Create Account',
                'https://1wrjmw.com/casino/list?open=register&p=mth6'
            )
        )
    except Exception as e:
        print("Promo Error:", e, flush=True)


async def bot_main():
    global status
    while True:
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

        except KeyboardInterrupt:
            sys.exit(1)

        except Exception:
            print(traceback.format_exc(), flush=True)
            await asyncio.sleep(5)


def run():
    asyncio.run(bot_main())


if __name__ == '__main__':
    allow_run = True
    run()
