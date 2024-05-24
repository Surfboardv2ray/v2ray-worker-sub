# V2ray Worker Sub

* This repository is mainly based on Vfarid's [V2ray-worker](https://github.com/vfarid/v2ray-worker) Project, version 2.3 with a minor change to return vmess:// proxies as well as vless:// correctly. Providers include Telegram Channels and publicly available v2ray subscriptions.

# How to deploy

* Since there's a daily limitation (100,000) on Cloudflare's behalf. There are two approaches to deploy your own version:
* You could  deploy [Your Own Worker](https://www.youtube.com/watch?v=Jb_6jmrKKyo) using this [Bug fixed release](https://github.com/Surfboardv2ray/v2ray-worker-sub/releases/download/2.3.1/worker.js) of the script.
* If you have a v2ray worker sub deployed on Cloudflare already, Fork this repository and create Actions Secret `INPUT_URL` and put your worker sub URL as the value.

# SpeedTest and Sorting

This code also uses [V2rayAggregator](https://github.com/mahdibland/V2RayAggregator) developed by Mahdibland to speedtest and sort vmess proxies.

# Subscription Links:

♦️ Worker sub: [Link](https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/main/sub)

♦️ Worker Base64: [Link](https://raw.githubusercontent.com/Surfboardv2ray/Vfarid-fix/main/sub64)

♦️ Eternity: [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity.txt)

♦️ Eternity Base64: [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/master/Eternity)
