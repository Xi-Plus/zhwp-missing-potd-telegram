import argparse
import datetime
import functools
import time

import requests
import telegram
from config import cfg

parser = argparse.ArgumentParser()
parser.add_argument('--dry-run', action='store_true')
args = parser.parse_args()
print(args)
dry_run = args.dry_run


@functools.lru_cache()
def check_exist(year, month, date):
    try:
        url = cfg['url_local'].format(year, month, date)
        req = requests.get(url)
        return req.status_code == requests.codes.ok
    except Exception as e:
        print(e)
        return False


bot = telegram.Bot(cfg['telegram']['token'])

for chat_id in cfg['telegram']['chats']:
    setting = cfg['telegram']['chats'][chat_id]
    print(chat_id, setting)
    for day_diff in range(setting['day_start'], setting['day_end'] + 1):
        the_day = datetime.datetime.now() + datetime.timedelta(days=day_diff)
        year = the_day.year
        month = the_day.month
        date = the_day.day
        if not check_exist(year, month, date):
            message = setting['message'].format(
                year,
                month,
                date,
                day_diff,
                cfg['url_local'].format(year, month, date),
                cfg['url_commons'].format(year, month, date),
            )
            print(message)
            if not dry_run:
                for i in range(5):
                    try:
                        print('send to {}'.format(chat_id))
                        sent_message = bot.send_message(
                            chat_id=chat_id,
                            text=message,
                            parse_mode=telegram.ParseMode.HTML,
                            disable_web_page_preview=True)
                        break
                    except telegram.error.TimedOut as e:
                        print('send to {} failed: TimedOut: {}'.format(chat_id, e))
                        time.sleep(1)
                    except telegram.error.BadRequest as e:
                        print('send to {} failed: BadRequest: {}'.format(chat_id, e))
                        break
                    except Exception as e:
                        print('send to {} failed: {}'.format(chat_id, e))
