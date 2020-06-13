from discord import Webhook, RequestsWebhookAdapter, Embed, Color
import datetime


def cyber(wblink, product, productIcon, site, size, profile, orderNum, ProxyList, Mode, authorurl, boticon, authorname,
          botname):
    webhook = Webhook.from_url(wblink, adapter=RequestsWebhookAdapter())

    embed = Embed(title="Successfully checked out!", description=product, color=7203609)
    embed.set_thumbnail(url=productIcon)
    embed.add_field(name="Store", value=site, inline=True)
    embed.add_field(name="Size", value=size, inline=True)
    embed.add_field(name="Profile", value="||" + profile + "||", inline=True)
    embed.add_field(name="Order", value="||" + orderNum + "||", inline=True)
    embed.add_field(name="Proxy list", value="||" + ProxyList + "||", inline=True)
    embed.add_field(name="Mode", value=Mode, inline=True)
    time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
    embed.set_footer(text="CyberAIO•" + time, icon_url=boticon)

    webhook.send(embed=embed, avatar_url=author(authorurl, boticon, authorname, botname)[0],
                 username=author(authorurl, boticon, authorname, botname)[1])


def dashe(wblink, product, email, site, size, profile, orderNum, delay, boticon, authorurl, authorname, botname):
    webhook = Webhook.from_url(wblink, adapter=RequestsWebhookAdapter())

    embed = Embed(title="Dashe Checkout (" + site + ")", color=16711741)
    embed.add_field(name="Product", value=product, inline=False)
    embed.add_field(name="Size", value=size, inline=True)
    embed.add_field(name="Profile", value="||" + profile + "||", inline=True)
    embed.add_field(name="Email", value="||" + email + "||", inline=True)
    embed.add_field(name="Order Number", value="||" + orderNum + "||", inline=True)
    embed.add_field(name="Checkout Delay", value=delay, inline=True)
    embed.set_footer(text="Dashe", icon_url=boticon)

    webhook.send(embed=embed, avatar_url=author(authorurl, boticon, authorname, botname)[0],
                 username=author(authorurl, boticon, authorname, botname)[1])


def NSB(wblink, product, email, site, size, profile, productIcon, price, authorurl, boticon, authorname, botname):
    webhook = Webhook.from_url(wblink, adapter=RequestsWebhookAdapter())

    embed = Embed(title="COOK COOOOK COOOOOOOOOK!", color=16711741)
    embed.set_thumbnail(url=productIcon)
    embed.add_field(name="Product", value=product + "-" + size, inline=False)
    embed.add_field(name="Site", value=site, inline=False)
    embed.add_field(name="Size", value=size, inline=False)
    embed.add_field(name="Profile", value="||" + profile + "||", inline=False)
    embed.add_field(name="Email", value="||" + email + "||", inline=False)
    embed.add_field(name="Price", value=price, inline=False)
    embed.set_footer(text="NSB © 2020 - v2.4.21")

    webhook.send(embed=embed, avatar_url=author(authorurl, boticon, authorname, botname)[0],
                 username=author(authorurl, boticon, authorname, botname)[1])


def author(authorurl, boticon, authorname, botname):
    if authorurl == "":
        avatar_url = boticon
    else:
        avatar_url = authorurl

    if authorname == "":
        username = botname
    else:
        username = authorname
    return avatar_url, username


def main():
    wblink = input("请输入webhook link:")
    bot = input("请输入bot名称(Cyber, Dashe, NSB):")
    authorname = input("请输入author名字(默认请跳过):")
    authorurl = input("请输入author头像url(默认请跳过):")
    site = input("请输入购买网站名称:")
    product = input("请输入单品标题:")
    size = input("请输入购买的尺码:")

    if bot.lower() == "cyber":
        productIcon = input("请输入单品图片url:")
        profile = input("请输入使用的profile名称:")
        orderNum = input("请输入Order Number:")
        ProxyList = input("请输入Proxy List:")
        Mode = input("请输入使用的Mode:")
        botname = "CyberAIO"
        boticon = "https://cdn.discordapp.com/avatars/689549346479407139/b972ed09df1f477405707811da48c973.webp?size=128"
        cyber(wblink, product, productIcon, site, size, profile, orderNum, ProxyList, Mode, authorurl, boticon,
              authorname, botname)
    elif bot.lower() == "dashe":
        profile = input("请输入使用的profile名称:")
        orderNum = input("请输入Order Number:")
        email = input("请输入使用的Email:")
        delay = input("请输入Checkout Delay:")
        botname = "Dashe"
        boticon = "https://images-ext-1.discordapp.net/external/ONcrzo-4wBRmH5xn-KxWew-Wxb1KS59ltVOFu1Gntdc/https/i.imgur.com/c3G0FRi.png"
        dashe(wblink, product, email, site, size, profile, orderNum, delay, boticon, authorurl, authorname, botname)
    elif bot.lower() == "nsb":
        price = input("请输入单品价格:")
        productIcon = input("请输入单品图片url:")
        profile = input("请输入使用的profile名称:")
        email = input("请输入使用的Email:")
        botname = "NSB"
        boticon = "https://cdn.discordapp.com/avatars/710500489502130256/51c781071f37909543f2b8db3d0986fc.webp?size=128"
        NSB(wblink, product, email, site, size, profile, productIcon, price, authorurl, boticon, authorname, botname)
    print("Webhook sent! Check your server!")


if __name__ == '__main__':
    main()

'''

测试数据：

请输入购买网站名称: Shop Nice Kicks
请输入单品标题: YEEZY 350 V2 LINEN MENS LIFESTYLE SHOE - LINEN/LINEN
请输入购买的尺码: 13
请输入单品价格: 220
请输入单品图片url:
https://images-ext-2.discordapp.net/external/Ra9p5yY8LMoadDluTPdxRFvfBuIfwpqSSvRQPk3rB4I/%3Fv%3D1587096318/https/cdn.shopify.com/s/files/1/0267/9232/9325/products/FY5158-1.jpg?width=443&height=499
请输入使用的profile名称: US-MC
请输入Order Number: #7982
请输入Proxy List: Resigame-us
请输入使用的Email: TheCodingBunny@tcb.com
请输入Checkout Delay: 7862ms
请输入使用的Mode: Fast

'''
