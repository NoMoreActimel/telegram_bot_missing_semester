import telebot
from os import environ
import random

upper_underwear_images = [
    "https://cs5.pikabu.ru/post_img/2014/09/09/9/1410269428_757869691.jpg",
    "https://shop.effectum.info/wp-content/uploads/2019/10/gavajskaja-rubashka-iz-filma-odnazhdy-v-gollivude-1.jpg",
    "https://winnersports-wear.com/upload/iblock/af6/af69f7ec1237d541efdf34679db359ad.png",
    "https://storage.vsemayki.ru/images/0/1/1978/1978153/previews/people_7_manshort_front_white_500.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnKWkjjtwOv2FgPV7Acquppn4cxLc9TWMgPg&usqp=CAU"
]
bottom_underwear_images = [
    "https://cs5.livemaster.ru/storage/b1/6f/71f354bae8d015abbfdeab7268av--muzhskaya-odezhda-trusy-muzhskie-semejnye.jpg",
    "https://st.tsum.com/btrx/i/10/67/92/95//01_434.jpg?u=1636494750",
    "https://cf-product.clouty.ru/link_aHR0cHM6Ly9hLmxtY2RuLnJ1L3BpL2ltZzYwMHg4NjYvTS9QL01QMDAyWE0xSzgzRV8xMTAyNTkyOF8xX3YxLmpwZw==",
    "https://www.maxxximoda.ru/upload/iblock/3d5/3d592ec6323fe3f75a5607b5e3028faf.jpg",
    "https://66.img.avito.st/640x480/8563840166.jpg"
]
upper_outerwear_images = [
    "https://cdn.shopify.com/s/files/1/0016/9095/9972/products/2560px-Pornhub-logo_mockup_Front_On-Hanger_Black_1024x1024_2x_af1c46a8-6ef0-4015-954a-16a66d7bbd57_300x300.jpg?v=1622275334",
    "https://images11.esquire.ru/upload/custom/101/1015ebf18acb4b3e4085602802b0810f.jpg",
    "https://www.melijoe.com/images/179184/image_gallery_large.jpg",
    "https://www.fc-moto.de/WebRoot/FCMotoDB/Shops/10207048/5C86/5F9B/CC37/B3F5/8810/AC1E/1407/0270/19SBLUL02191-005322_659_ml.jpg",
    "https://cdn3.justbutik.ru/styles/product_catalog_211x281/openstack/externals/43/22/43228f112ebc92ba40f30309a52aa876.jpg?itok=148DJpyk"
]
bottom_outerwear_images = [
    "https://images.quiddi.ru/item/images/dir761/59e3b79f429c2bf70a351574c31480e59b5ac8bb.jpg",
    "https://shopsycdn.com/i/p/4b/35/4b35d25fe29d7b3cdca0371ed81eba64_medium.jpg",
    "https://machete-market.ru/image/cache/data-armejskoe-shmotka-shtany-jungle-python-380x380.jpg",
    "https://usdenim.ru/wp-content/uploads/2017/08/klassicheskie-muzhskie-dzhinsy-02.jpg",
    "https://sartoreale.ru/upload/iblock/339/vvyo4tdl0s9y0zhcunuwvibsro5a0zsn.jpg"
]

token_file = open("token.txt", 'r')

token = environ.get('API')
bot = telebot.TeleBot(token_file.readline())


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "hello there!")
    bot.send_message(message.chat.id, "This bot will give you outfit ideas for the day.")
    bot.send_message(message.chat.id, "commands:\n/start\n/help\n/new_clothes\n/kill_myself")


@bot.message_handler(commands=['help'])
def answer_help(message):
    bot.reply_to(message, "commands:\n/start\n/help\n/new_clothes\n/kill_myself")


@bot.message_handler(commands=['kill_myself'])
def answer_kill_myself(message):
    bot.send_photo(message.chat.id, "https://sun9-10.userapi.com/impg/BQGF8mPOBIQ2BAvvl4i0cvuubBEKJMuAwHd7bA/KeY3nQOC-TA.jpg?size=320x263&quality=96&sign=a89dd78470e49421ba28389091be1083&c_uniq_tag=Qi3aIb8787p-NZCZaw_p3fO8YiZKVyNZr-r1IGYEWf8&type=album")


@bot.message_handler(commands=['new_clothes'])
def send_new_clothes(message):
    float_coin = random.random()
    if float_coin > 0.7:
        bot.send_message(message.chat.id, "Initialize yourself as a woman")
        bot.send_message(message.chat.id, "Women don't wear clothes")
        bot.send_message(message.chat.id, "Enjoy!")
    else:
        bot.send_message(message.chat.id, "You are man")
        bot.send_message(message.chat.id, "And here are your clothes")

        upper_underwear_coin = random.randint(0, 4)
        bottom_underwear_coin = random.randint(0, 4)
        upper_outerwear_coin = random.randint(0, 5)
        bottom_outerwear_coin = random.randint(0, 6)


        bot.send_message(message.chat.id, "Underwear:")
        bot.send_photo(message.chat.id, upper_underwear_images[upper_underwear_coin])
        bot.send_photo(message.chat.id, bottom_underwear_images[bottom_underwear_coin])

        if upper_outerwear_coin >= 5 or bottom_outerwear_coin >= 5:
            bot.send_message(message.chat.id, "No-Outerwear-Day!")
        else:
            bot.send_message(message.chat.id, "Outerwear:")
            bot.send_photo(message.chat.id, upper_outerwear_images[upper_outerwear_coin])
            bot.send_photo(message.chat.id, bottom_outerwear_images[bottom_outerwear_coin])

bot.infinity_polling()
