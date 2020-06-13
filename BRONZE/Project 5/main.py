def test_delay(proxy, url):
    import requests

    proxydata = proxy.split(":")
    proxy = "http://{}:{}@{}:{}".format(proxydata[2], proxydata[3], proxydata[0], proxydata[1])
    proxies = {
        'http': proxy,
        'https': proxy
    }
    try:
        ave_ping = 0
        for i in range(3):
            response = requests.get(url=url, proxies=proxies, timeout=5)
            ave_ping = ave_ping + response.elapsed.microseconds
        ave_ping = ave_ping / 3
        return int(ave_ping * 0.001)
    except Exception as e:
        return -1


def main():
    filename = input('请输入proxy文件名(.txt):')
    # url = input('请输入您想测试的网站地址:')
    url = 'http://google.com/'
    with open(filename, 'r') as f:
        proxy_list = f.readlines()

    good_proxy = []
    print('正在测试...')
    for proxy in proxy_list:
        proxy = proxy.replace("\n", "")
        delay = test_delay(proxy, url)
        if delay == -1:
            print('{} 这条proxy连不上 {}'.format(proxy, url))
        elif delay < 500:
            good_proxy.append(proxy)
            print('{} 的延迟为 {}ms,这很可以'.format(proxy, delay))
        else:
            print('{} 的延迟为 {}ms,这8太行'.format(proxy, delay))

    print('\n\n可以用的proxy为:')
    print(good_proxy)


if __name__ == '__main__':
    main()
