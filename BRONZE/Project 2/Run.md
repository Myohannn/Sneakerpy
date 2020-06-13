运行结果:

以https://juicestore.com/collections/nike/products/react-vision-3 为例

![image](https://cdn.discordapp.com/attachments/678916771507339276/721362119534182490/unknown.png)

收到的webhook:

![image](https://cdn.discordapp.com/attachments/678916771507339276/721362154770399242/unknown.png)

每5秒请求一次库存，如果有库存变化就会发送webhook

![image](https://cdn.discordapp.com/attachments/678916771507339276/721363315665666130/unknown.png)

如果连续请求出错5次，监控停止