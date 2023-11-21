# 🤩 StarLabs - Discord 

![Logo](https://i.postimg.cc/rpLrDXrr/8e4fafbd-9319-4653-9f5a-fdf0f84974e7.png)

Если кратко, то с данным функционалом вы сможете: 

- войти аккаунтами на сервер, пройдя самые популярные виды защиты

- прожать кнопку, будь то участие в розыгрыше, капча и так далее

- поставить реакцию на сообщение в чате

- отправить сообщение в чат с текстом который вы укажете

- сменить имя аккаунта, юзернейм, пароли, картинку профиля

## 🚀 Installation
```
git clone https://github.com/0xStarLabs/StarLabs-Discord.git

cd StarLabs-Discord

pip install -r requirements.txt

# Перед началом работы настройте необходимые модули в файлах config.ini и /data

python main.py
```

## ⚙️ Config

| Name | Description |
| --- | --- |
| max_invite_retries | Количество попыток входа на сервер |
| max_tasks_retries | Максимальное количество попыток при выполнении задания |
| pause_between_tasks | Пауза между каждым действием |
| capmonster_api_key | Ключ от https://capmonster.cloud/Dashboard |
| 2captcha_api_key | Ключ от https://2captcha.com/. |



## 🗂️ Data

Данные в папке data:

| Name | Description |
| --- | --- |
| discord_tokens.txt | Содержит дискорд токены |
| failed_tokens.txt | Содержит аккаунты которые не были выполнены |
| new_names.txt | Содержит имена для функции смены имен |
| new_passwords.txt | Содержит новые пароли для функции смены паролей |
| new_usernames.txt | Содержит новые юзернеймы для функции смены юзернеймов |
| passwords.txt | Содержит текущие пароли аккаунтов |
| proxies.txt | Содержит прокси в формате user:pass@ip:port |
| profile_pictures | Папка содержит картинки для смены в профилях |


## 🔗 Links

🔔 PUBLIC: https://t.me/StarLabsTech

💬 CHAT: https://t.me/StarLabsChat

💰 DONATION EVM ADDRESS: 0x620ea8b01607efdf3c74994391f86523acf6f9e1
