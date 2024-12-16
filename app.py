from flask import Flask, request, render_template, jsonify
import time, traceback, asyncio
from threading import Thread
from requests import get


app = Flask(__name__)
__version__ = 3.4

class base:
    status = 'Stopped'
    allow_run = False

class avaitor_bot(base): pass
class mines_bot(base): pass
class luckyjet_bot(base): pass


@app.route('/', methods=['GET', 'POST', 'PATCH'])
def index():
    if request.method == 'PATCH': return jsonify(dict(avaitor=avaitor_bot.status, mines=mines_bot.status, luckyjet=luckyjet_bot.status))
    if request.method == 'POST':
        bname = request.form.get('bot')
        run = request.form.get('run', 0, int)
        eval(bname + '_bot').allow_run = bool(run)
        return jsonify(dict(success=True, msg='Success! But it may take some time to complete the operation'))
    return render_template('index.html', version=__version__)

def keep_alive():
    while 1:
        time.sleep(5 * 60) # Every 5 mins
        print('[+] Keep Alive', flush=True)
        try: get('https://avaitor-bot.onrender.com')
        except: print(traceback.format_exc(), flush=True)


if __name__ == '__main__':
    Thread(target=lambda: app.run('0.0.0.0')).start()
    Thread(target=keep_alive).start()
    import avaitor_bot, luckyjet_bot, mines_bot  #, ads
    async def run_bots():
        for task in asyncio.as_completed([avaitor_bot.bot_main(), luckyjet_bot.bot_main(), mines_bot.bot_main()]):
            await task
    asyncio.run(run_bots())
    


