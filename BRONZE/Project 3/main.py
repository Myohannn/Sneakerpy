#  footlocker eu账号激活器
#
# 跑过大象的都知道，之前yeezy 350有一次发售，需要强制账号才能加车
# 用大象注册时，会给你的邮箱发送一封 verify 邮件
# 本项目要求:
#
# - 输入为一个verify邮件中的激活链接的列表（提取方式有很多，可以读取你的email，也可以通过页面的正则等)
# - 自行研究ftl eu的账号激活流程
# - 利用程序实现，并将激活的结果进行输出
#
# hint:
# - ftl eu的激活就是对链接进行访问，但需要带上一些headers等信息，否则会失败
# - 成功与否需要对返回的html进行解析，具体字段请自行实验

def main():
    link = 'https://link.flxprogram.nl/u/nrd.php?p=ljvxLcRr6g_403475_330399_1_5&ems_l=475586&d=aHR0cHM6Ly93d3cuZm9vdGxvY2tlci5jby51ay9JTlRFUlNIT1Avd2ViL0ZMRS9Gb290bG9ja2VyLUZvb3Rsb2NrZXJfR0ItU2l0ZS9lbl9HQi8tL0dCUC9WaWV3VXNlckFjY291bnRBY3RpdmF0aW9uLUFjdGl2YXRlQWNjb3VudD9Mb2dpbj10ZXN0aW5ndGVzdGluZyU0MG15b2hhbi5jbHViJkhhc2g9ZTVjMWMyYzMtNTllNy00ZTI3LTgwZjMtYzQwZjljNzYxZjc5JmlzTG95YWx0eT10cnVl%7C'


if __name__ == '__main__':
    main()
