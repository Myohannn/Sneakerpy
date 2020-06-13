import random


def gen_proxy(region, amount, total_amount, bot_list):
    port_list = range(10000, 20000)
    proxyperRegion = []
    proxies = {}
    ports = random.sample(port_list, total_amount)
    for port in ports:
        proxy = '{}.smartproxy.com:{}:username:password'.format(region, port)
        proxyperRegion.append(proxy)

    head = 0
    for bot in bot_list:
        proxies[bot] = proxyperRegion[head:head + amount[bot]]
        head = head + amount[bot]

    return proxies


def save(proxies):
    for bot in proxies:
        with open(bot + '.txt', 'w') as f:
            s = ('\n'.join(proxies[bot]))
            f.write(s)


def main():
    region_list = input('请输入你想要的地区:').split(' ')
    bot_list = input('请输入你想用的bot(s):').split(' ')
    amount = {}
    proxies = {}
    total_amount = 0
    for bot in bot_list:
        amount_initial = int(input('请输入{}需要的proxy数量:'.format(bot)))
        if amount_initial % len(region_list) == 0:
            amount_need = amount_initial // len(region_list)
        else:
            amount_need = amount_initial // len(region_list) + 1
        amount[bot] = amount_need

        total_amount += amount[bot]
        proxies[bot] = []

    for region in region_list:
        new_dict = gen_proxy(region, amount, total_amount, bot_list)
        for bot in bot_list:
            proxies[bot] = proxies[bot] + new_dict[bot]

    save(proxies)


if __name__ == '__main__':
    main()
