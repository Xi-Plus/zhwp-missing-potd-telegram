cfg = {
    'url_local': 'https://zh.wikipedia.org/wiki/Wikipedia:每日图片/{0}年{1}月{2}日',
    'url_commons': 'https://commons.wikimedia.org/wiki/Template:Potd/{0:02d}-{1:02d}-{2:02d}_(en)',
    'telegram': {
        'token': '',
        'chats': {
            # 0 year
            # 1 month
            # 2 date
            # 3 day
            # 4 url_local
            # 5 url_commons
            -123456: {
                'message': '#首頁 {3}天後<a href="{4}">{1}/{2}的特色圖片</a>目前缺少，可參考<a href="{5}">共享資源的特色圖片</a>添加',
                'day_start': 1,
                'day_end': 3,
            },
        },
    },
}
