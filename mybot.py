import telebot
from telebot import types

bot = telebot.TeleBot('6917419316:AAHqULWU_oi_yK1NIZYShV5Ro4HfcPolLlI')

user_messages = {}

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Приветствие')
    btn2 = types.KeyboardButton('Запрос')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Нажмите на кнопку", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == 'Приветствие':
        bot.send_message(message.chat.id, text='Добро пожаловать, этот Бот поможет вам узнать о ценах на продукты из сети магазина Народный ')
    elif message.text == 'Запрос':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn3 = types.KeyboardButton('Кто написал тебя')
        btn1 = types.KeyboardButton('Что ты можешь?')
        btn4 = types.KeyboardButton('Выйти в меню')
        btn2 = types.KeyboardButton('Посетить сайт')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Выберите категорию услуг", reply_markup=markup)

    elif message.text == 'Посетить сайт':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Чтобы перейти на сайт', url='https://www.market.kg/ru'))
        bot.send_message(message.chat.id, 'Нажмите на кнопку', reply_markup=markup)
    elif message.text == 'Кто написал тебя':
        bot.send_message(message.chat.id, "Меня написал\nИмя: Идирис\ntelegram: @Idiris13")
    elif message.text == 'Что ты можешь?':
        bot.send_message(message.chat.id, 'Я могу предоставить список продуктов и об их цене')
        markup_inline = types.InlineKeyboardMarkup()
        item_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
        item_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        markup_inline.row(item_yes, item_no)
        bot.send_message(message.chat.id, text='Вам показать список продуктов?', reply_markup=markup_inline)
    elif message.text == 'Выйти в меню':
        mark = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton('Приветствие')
        bt2 = types.KeyboardButton('Запрос')
        mark.add(bt1, bt2)
        bot.send_message(message.chat.id, text="Вы в меню", reply_markup=mark)
    else:
        bot.send_message(message.chat.id, text='Пожалуйста работайте с кнопками ')

products_prices = {
    '🍅🥕🥔': {
        'Помидоры 1кг': (135, 'https://img.freepik.com/free-photo/tomato-isolated_2829-17580.jpg?size=626&ext=jpg'),
        'Огурцы Караж 1кг': (100, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSr9UDNUHvJjLHWdVTOUNRfmXl4qirzpT7WlvQyIgwcg&s'),
        'Картофель фасованный 1кг': (39, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcdVyb9qratvPsDv8TiNMb8-vdUhcZ5oJU_IAMAmumXg&s'),
        'Свекла 1кг': (83, 'https://aif-s3.aif.ru/images/003/305/6c9b6fe8d41537b85c741d54121bfb29.jpg')
    },
    '🍋🍌🍎': {
        'Яблоки Превосходные 1кг': (150, 'https://buyer.prosoft.kg/images/product/51/1502629227.jpg'),
        'Бананы в/с 1кг': (155, 'https://img.belta.by/images/storage/news/with_archive/2022/000467_1643035210_480984_big.jpg'),
        'Апельсины': (170, 'https://img.belta.by/images/storage/news/with_archive/2022/000467_1646837834_489198_big.jpg'),
        'Мандарины 1кг': (180, 'https://ss.sport-express.ru/userfiles/materials/173/1739263/full.jpg'),
        'Яблоки Голден 1кг': (165, 'https://ksp-sw.ru/wp-content/uploads/2018/03/yabloko-grusha-golden-delishes2.jpg')
    },
    '🥖🍞': {
        'Хлеб Солдатский 380г': (20, 'https://cdn-img.perekrestok.ru/i/800x800-fit/xdelivery/files/75/00/2f46b8b8e300473e3383e907117c.jpg'),
        'Черный хлеб': (25, 'https://static.mk.ru/upload/entities/2019/11/27/13/articles/detailPicture/43/e9/87/ba/5deb8043023989c928fee132f7f1748e.jpg'),
        'Лепешки': (20, 'https://tehnokeramica.ru/upload/forstati/492(8).jpg')
    },
    '🥛🍶': {
        'Молоко ВМ 3,2% 900г': (104, 'https://globus-online.kg/upload/iblock/34c/34cd095cc1f5caac3fa7a52036f0609c.png'),
        'Сливки ДВД 10% 480г': (183, 'https://cdn-img.perekrestok.ru/i/800x800-fit/xdelivery/files/c2/00/3d13f0bf2535b7d355ddccc7bd42.jpg'),
        'Кактель Чудо молоч ягоды/мороженое 2.0%': (70, 'https://prodmarket.kz/wp-content/uploads/bezymyannyj-1-263.jpg'),
        'Сметана': (100, 'https://marr.ru/upload/resize_cache/webp/upload/iblock/5ae/l38gs9qyun5kj2fvpi5ep27npeaza18o.webp'),
        'Кефир': (83, 'https://www.globalfoods.ru/upload/iblock/c75/zrylbknkpdcf3v1qa7wpy406b3vfcsq7.jpg'),
        'Сливки': (139, 'https://globus-online.kg/upload/iblock/a4c/a4cb8d1985e0700065bb5d70dc66dd15.png'),
        'Жети батыр: Сметана 30% 300г': (87, 'https://globus-online.kg/upload/iblock/35d/35d05615cca477f98474ec6be12d8e18.png'),
        'Творожок': (86, 'https://globus-online.kg/upload/iblock/5ea/5ea1950b217cfa68d0b308b828c8fa26.png'),
        'Село зеленое, молоко': (111, 'https://taumart.ru/upload/resize_cache/webp/upload/iblock/62d/ip1ap7dy1nio50v4gorr8czvbzcft8en.webp'),
        'КЕФИР': (89, 'https://images.coolclever.ru/img/1000/20230323152510-0000000034020072-19260-17.jpg'),
        'ДАННИСИМО': (112, 'https://produktoff.com/static/upload/goods/38/18138_original.jpg'),
    },
    '🐔': {
        'Окорочка куриные заморож ТУ вес': (239, 'https://swlife.ru/image/cache/catalog/product/cc/64/cc64cbf27bae482d210d0ea33ca2ef83-0x0.webp'),
        'Голень цыпленка бройлера замороженная вес': (319, 'https://cdn.metro-cc.ru/ru/ru_pim_296713001001_01.png'),
        'Филе куриное заморож 1кг': (439, 'https://static.insales-cdn.com/images/products/1/599/712852055/large_75ebd73da0ff0157797941540b8f5329.jpg')
    },
    '🍖🥩': {
        'АЛ-ХАЛАЛ, ЮЖНАЯ': (262, 'https://al-halal.kg/wp-content/uploads/2018/09/6-%D0%AE%D0%B6%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D0%BF%D0%B8%D1%8F-600x399.jpg'),
        'РИХА, ЛЮБИТЕЛЬСКАЯ': (62, 'https://riha.kg/wp-content/uploads/2021/02/Lyubitelskaya-Krasnaya-tsena--297x188.jpg'),
        'ОСТАНКИНО, СОЛЯМИ ИТАЛЬЯНСКАЯ': (537, 'https://ompk.ru/images/cache/66-121-ital-salami-s-726x340.jpg'),
        'САЛИХ, ХАНСКАЯ': (199, 'https://globus-online.kg/upload/iblock/bd1/bd18cf5993fc49a88f4d8646daf05a92.png'),
        'АБРОЙ': (39, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdeASjQIOkVs3DTdz4XjkAwQ85Ly_7ogO0E32VXc2Rmg&s'),
        'ТУРАН СОЛЯМИ': (32, 'https://globus-online.kg/upload/iblock/02b/on8dwjcu8zxxeu786hhkyvgwymi4u4ia/23d8eb87-0b3d-11ee-80c9-005056845eda.png'),
        'ПАПА МОЖЕТ, СЕРВЕЛАТ ОХОТНИЧИЙ': (346, 'https://globus-online.kg/upload/iblock/7dc/7dcc8df64942f19ea013084ed47e2e1f.png')
    },
    '🥠🍫': {
        'Батончик Babyfox молочный 45г': (35, 'https://may24.ru/upload/iblock/25c/_25c7f3d948ac4276b8a46b33b27e951f.jpg'),
        'Батончик Snickers super 80 г': (91, 'https://globus-online.kg/upload/iblock/13e/13e286f301f5a6bb58a64b53d5a8a864.png'),
        'Батончик BonTime hyra/пломбир 20г KDV': (9, 'https://delovoy.by/upload/Sh/imageCache/8ee/f72/c8a6ef5433c4e7ab8a9d4d5f4c26c2bb.jpg'),
        'Батончик Ulker Albeni XXL 70г': (76, 'https://avatars.mds.yandex.net/get-mpic/4407413/img_id2294973640269502842.png/9hq'),
        'Батончик Ulker Albeni 40г': (46, 'https://main-cdn.sbermegamarket.ru/big1/hlr-system/686/116/006/122/722/17/100030116387b0.jpeg'),
        'Конфеты Рахат Батончик мол-вал 1кг': (471, 'https://hatber.kz/upload/iblock/b93/b93ce2dc92efb6090eaa7ada062e11f1.jpg'),
        'Батончик Twix 55г': (57, 'https://cc.kz/upload/iblock/cb6/cb613f9237987011e39792b5c0e63599.jpg')
    },
    '☕️': {
        'Пиала 250г': (254, 'https://cc.kz/upload/iblock/b0c/zjji4t98kde2nhoi3ai4rjknqm3cjnku.jpg'),
        'JACOBS': (390, 'https://s0.rbk.ru/v6_top_pics/media/img/1/44/346910418045441.jpeg'),
        'TESS PLEASURE': (301, 'https://ananas.kg/image/cache/catalog/10971-700x770.jpg'),
        'MACCOFFE': (19, 'https://double.kg/wp-content/uploads/74d037ed73c011eea41300155d56a302_74d037ee73c011eea41300155d56a302.jpg')
    },
    '🧃🥤': {
        'Pepsi 1,5л': (137, 'https://cc.kz/upload/iblock/727/z4ev3ycpcj1vgux25usaeqlrnna0bzky.jpg'),
        'ЕССЕНТУКИ 1,5': (148, 'https://produktoff.kz/pictures/product/big/6795_big.jpg'),
        'BORJOMI 0,33': (106, 'https://voda095.ru/upload/iblock/323/323a4eefe3739f234d1abff969e2dcbb.png'),
        'ШОРО BAYTIK 1,5': (45, 'https://www.shoro.kg/wp-content/uploads/2021/04/baytik-kopiya-1.png'),
        'COCA COLA 1,5': (99, 'https://www.abcfoodservice.it/5189-large_default/coca-cola-beverage-lt-15-x-6.jpg'),
        'SPRITE': (99, 'https://images.uzum.uz/ceimfdivtie1lhbfcrt0/original.jpg'),
        'FANTA 1,5': (99, 'https://elitalco.kz/upload/images/10310_114139_09.jpeg'),
        'ШОРО АРАЛАШ BIO 1л': (97, 'https://ashlyanfu-msk.ru/wa-data/public/shop/products/27/00/27/images/15/15.970.png'),
        'Любимый 0,95': (109, 'https://vodovoz.ru/upload/iblock/a64/a6481d5e2dd2d6552a5ef01b2927110a.jpeg'),
        'GOLDEN SUN 5л': (164, 'https://storage.yandexcloud.net/frunze/product/73408/600x600.webp')

    }
}

@bot.callback_query_handler(func=lambda call: True)
def cal_inline(call):
    chat_id = call.message.chat.id
    if chat_id in user_messages:
        for message_id in user_messages[chat_id]:
            bot.delete_message(chat_id, message_id)
        user_messages[chat_id] = []

    if call.data == 'yes':
        bot.send_message(chat_id, 'Выберите категорию продуктов')
        markup_inline = types.InlineKeyboardMarkup()
        vegetables = types.InlineKeyboardButton(f'🍅🥕🥔', callback_data='vegetables')
        fruits = types.InlineKeyboardButton(f'🍋🍌🍎', callback_data='fruits')
        bread = types.InlineKeyboardButton(f'🥖🍞', callback_data='bread')
        milk = types.InlineKeyboardButton(f'🥛🍶', callback_data='milk')
        meat = types.InlineKeyboardButton(f'🐔', callback_data='meat')
        sausage = types.InlineKeyboardButton(f'🍖🥩', callback_data='Sausage')
        confectionery = types.InlineKeyboardButton(f'🥠🍫', callback_data='confectionery')
        tea_and_coffee = types.InlineKeyboardButton(f'☕️', callback_data='tea_and_coffee')
        Beverages = types.InlineKeyboardButton(f'🧃🥤', callback_data='Beverages')
        markup_inline.add(vegetables, fruits, bread, milk, meat, sausage, confectionery, tea_and_coffee, Beverages)
        bot.send_message(chat_id, 'Выберите категорию продуктов', reply_markup=markup_inline)
    elif call.data == 'no':
        bot.send_message(chat_id, 'Хорошо, если вам понадобится помощь, обращайтесь!')
    elif call.data in ['vegetables', 'fruits', 'bread', 'milk', 'meat', 'Sausage', 'confectionery', 'tea_and_coffee', 'Beverages']:
        category = {
            'vegetables': '🍅🥕🥔',
            'fruits': '🍋🍌🍎',
            'bread': '🥖🍞',
            'milk': '🥛🍶',
            'meat': '🐔',
            'Sausage': '🍖🥩',
            'confectionery': '🥠🍫',
            'tea_and_coffee': '☕️',
            'Beverages': '🧃🥤',
        }[call.data]

        msg = bot.send_message(chat_id, f'Вот список {category.lower()} и их цены:')
        user_messages.setdefault(chat_id, []).append(msg.message_id)
        for product, (price, photo_url) in products_prices[category].items():
            try:
                msg = bot.send_photo(chat_id, photo=photo_url, caption=f'{product}: {price} сом.')
                user_messages[chat_id].append(msg.message_id)
            except telebot.apihelper.ApiTelegramException as е:
                bot.send_message(chat_id, f"Ошибка {product}")



bot.polling(none_stop=True)
