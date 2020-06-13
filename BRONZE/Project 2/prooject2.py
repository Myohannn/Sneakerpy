'''
2. 简单shopify 监控器

- 支持如undefeated网站的单品尺码监控，即当监控的单品更新尺码时，发送提醒到自定义的webhook
- 支持自定义webhook
- 做好错误处理，需要能够长期运行
- 附加题 实现undfeated的上新监控

hint:
- 对于一个单品 如 https://undefeated.com/collections/all/products/nike-x-undefeated-air-max-90-pacificblue-vividpurple 可以在后面加.json获取一个json的页面(shopify特性)
- https://undefeated.com/products.json 可以看到一个shopify站的所有商品（某些站会关闭，但本project只要实现未关闭的站即可)
'''
import datetime
import time

import requests, jsonpath, json
from discord import Webhook, RequestsWebhookAdapter, Embed


def product_info(url):
    url = url + ".json"
    response = requests.get(url)
    j = json.loads(response.text)
    id = jsonpath.jsonpath(j, "$.product.variants[*].id")
    product_name = jsonpath.jsonpath(j, "$.product.title")[0]
    size_name = jsonpath.jsonpath(j, "$.product.variants[*].title")
    stock = jsonpath.jsonpath(j, "$.product.variants[*].inventory_quantity")
    price = jsonpath.jsonpath(j, "$.product.variants[0].price")[0]
    image = jsonpath.jsonpath(j, "$.product.image.src")[0]

    return id, product_name, size_name, stock, price, image


def avatar_url():
    return "https://cdn.discordapp.com/avatars/629184799990349856/23135dae22cea136748aa3eb235adb98.webp?size=128"


def sizes(id, size_name, stock, wbsiteurl):
    sizes = []
    size = ""

    if stock == 'undentified':
        for i in range(0, len(size_name)):
            if i != 0 and i % 5 == 0:
                sizes.append(size)
                size = ""

            size = size + "[" + size_name[i] + "]" + "({}".format(wbsiteurl) + "/cart/" + str(
                id[i]) + ":1)" + "\n"
        return sizes
    else:
        count = 0
        for i in range(0, len(size_name)):
            if stock[i] > 0:
                if i != 0 and i % 5 == 0:
                    sizes.append(size)
                    size = ""

                size = size + "[" + size_name[i] + "]" + "(https://{}".format(wbsiteurl) + "/cart/" + str(
                    id[i]) + ":1)" + "\n"
        return sizes


def send_webhook(id, product_name, size_name, url, stock, price, image_url, wbsiteurl):
    # lovely tester
    wb_link = "https://discordapp.com/api/webhooks/717620825687195698/8tn_uiJJbyIl7X9pGJWQmjiuITQ7wC_FYkM6f5zxTc3uZQJaziw00rKapyQ9fISEERy3"
    webhook = Webhook.from_url(wb_link, adapter=RequestsWebhookAdapter())

    username = "Myohan"
    embed = Embed(title=str(product_name), url=url[:-5],
                  description='Price: ' + price + '\nWebsite: ' + "[" + wbsiteurl + "]" + "(" + wbsiteurl + ")")

    size = sizes(id, size_name, stock, wbsiteurl)
    for s in size:
        embed.add_field(name="ACT Sizes", value=s, inline=True)

    time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    Myohan_url = "https://cdn.discordapp.com/avatars/629184799990349856/23135dae22cea136748aa3eb235adb98.webp?size=128"
    embed.set_footer(text="Myonitor • shopify | " + time, icon_url=Myohan_url)
    embed.set_thumbnail(url=image_url)
    webhook.send(embed=embed, avatar_url=avatar_url(), username=username)


def main():
    print('Project 2-shopify monitor')
    wbsiteurl = input('请输入网站链接: ')
    if not wbsiteurl.startswith('http'):
        wbsiteurl = 'https://' + wbsiteurl
    url = input('请输入商品链接: ')
    url = url + ".json"
    response = requests.get(url)
    j = json.loads(response.text)
    id = jsonpath.jsonpath(j, "$.product.variants[*].id")
    product_name = jsonpath.jsonpath(j, "$.product.title")[0]
    size_name = jsonpath.jsonpath(j, "$.product.variants[*].title")
    price = jsonpath.jsonpath(j, "$.product.variants[0].price")[0]
    image_url = jsonpath.jsonpath(j, "$.product.image.src")[0]

    stock = jsonpath.jsonpath(j, "$.product.variants[*].inventory_quantity")
    if not stock:
        stock = 'undentified'

    send_webhook(id, product_name, size_name, url, stock, price, image_url, wbsiteurl)

    error = 0

    while True:

        time.sleep(5)

        currenttime = datetime.datetime.now().strftime('%H:%M:%S')

        stock1 = stock
        try:
            stock2 = jsonpath.jsonpath(j, "$.product.variants[*].inventory_quantity")
            if not stock2:
                stock2 = 'undentified'
        except Exception as e:
            error += 1
            print('[{}] Find stock error!'.format(currenttime))
            if error < 5:
                continue
            else:
                print('Something wrong....')
                print('Bye')
                break

        if stock1 == stock2:
            print('[{}] Keep running....'.format(currenttime))
            continue
        else:
            send_webhook(id, product_name, size_name, url, stock2, price, image_url, wbsiteurl)
            stock = stock2



if __name__ == '__main__':
    main()
