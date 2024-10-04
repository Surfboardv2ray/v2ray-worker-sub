# V2ray Worker Sub

* This repository is mainly based on Vfarid's [V2ray-worker](https://github.com/vfarid/v2ray-worker) Project, version 2.3 with a minor change to return vmess:// proxies as well as vless:// correctly. Providers include Telegram Channels and publicly available v2ray subscriptions.

# How to deploy

* Since there's a daily limitation (100,000 requests) on Cloudflare's behalf. There are two approaches to deploy your own version:
* You could  deploy [Your Own Worker](https://www.youtube.com/watch?v=Jb_6jmrKKyo) using this [Bug fixed release](https://github.com/Surfboardv2ray/v2ray-worker-sub/releases/download/2.3.1/worker.js) of the script.
* If you have a v2ray worker sub deployed on Cloudflare already, Fork this repository and create Actions Secret `INPUT_URL` and put your worker sub URL as the value.

* Update: Version 2.4 of the original script has been released, you can access it directly [from here](https://github.com/vfarid/v2ray-worker/releases/download/v2.4/worker.js).

# SpeedTest and Sorting

This code also uses [V2rayAggregator](https://github.com/mahdibland/V2RayAggregator) developed by Mahdibland to speedtest and sort vmess proxies.

# Subscription Links:

♦️ Worker sub (Daily Limitation): [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/sub)

♦️ Worker Base64 (Daily Limitation): [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/sub64)

♦️ Eternity: [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity.txt)

♦️ Eternity Base64: [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/Eternity)

♦️ Providers (Mega Sub): [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/providers/providers)

♦️ Providers Base64 (Mega Sub): [Link](https://raw.githubusercontent.com/Surfboardv2ray/v2ray-worker-sub/refs/heads/master/providers/providers64)


## Stargazers
[![Stargazers over time](https://starchart.cc/Surfboardv2ray/v2ray-worker-sub.svg?variant=adaptive)](https://starchart.cc/Surfboardv2ray/v2ray-worker-sub)
