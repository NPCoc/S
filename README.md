#  StarLabs - Discord 


![Logo](https://i.postimg.cc/rpLrDXrr/8e4fafbd-9319-4653-9f5a-fdf0f84974e7.png)

## [SEE ENGLISH VERSION BELOW ](https://github.com/0xStarLabs/StarLabs-Discord#english-version)👇

## 🔗 Links
[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/StarLabsTech)](https://t.me/StarLabsTech)

🔔 CHANNEL: https://t.me/StarLabsTech

💬 CHAT: https://t.me/StarLabsChat

💰 DONATION EVM ADDRESS: 0x620ea8b01607efdf3c74994391f86523acf6f9e1

📖 FULL TUTORIAL: https://teletype.in/@izanumi/star_labs_discord


## 🤖 | Функционал:

🟢 Вход на сервер 

🟢 Прожатие кнопок и реакций

🟢 Прохождений ботов защиты (Pandez, Sledgehammer, Captcha Bot...)

🟢 Отправка сообщений в чат

🟢 Смена имена, юзернейма, аватарки

🟢 Поддержка ретраев, прокси, пауз, потоков


## 🚀 Installation
```
# для работы необходимо установить NodeJS!
# https://nodejs.org/en/download/current

git clone https://github.com/0xStarLabs/StarLabs-Discord.git

cd StarLabs-Discord

pip install -r requirements.txt

# Перед началом работы настройте необходимые модули в файлах config.ini и /data

python main.py
```

## ⌨️ Control

Для управления в меню используются стрелочки Вверх/Вниз, для выбора действия Пробел и Enter для подтверждение выбора.

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

## Дисклеймер
Автоматизация учетных записей пользователей Discord, также известных как самостоятельные боты, является нарушением Условий обслуживания и правил сообщества Discord и приведет к закрытию вашей учетной записи (аккаунтов). Рекомендуется осмотрительность. Я не буду нести ответственность за ваши действия. Прочтите об Условиях обслуживания Discord и Правилах сообщества.

Это программное обеспечение было написано как доказательство концепции того, что учетные записи Discord могут быть автоматизированы и могут выполнять действия, выходящие за рамки обычных пользователей Discord, чтобы Discord мог вносить изменения. Авторы  освобождаются от любой ответственности, которую может повлечь за собой ваше использование.

## ENGLISH VERSION:

## 🤖 | Features :

🟢 Invite joiner

🟢 Pressing buttons and reactions

🟢 Bypass of protection bots (Pandez, Sledgehammer, Captcha Bot...)

🟢 Sending messages to chat

🟢 Change names, usernames, avatars

🟢 Retries, Proxies, Pauses, Threads


## 🚀 Installation
```
# You need to install NodeJS!
# https://nodejs.org/en/download/current

git clone https://github.com/0xStarLabs/StarLabs-Discord.git

cd StarLabs-Discord

pip install -r requirements.txt

# Before starting the tool make sure to configure it in config.ini and add information to data folder

python main.py
```

## ⌨️ Control

To navigate the CLI menu use the Up/Down arrows, Space to select one or more actions and Enter to confirm your choice.

## ⚙️ Config

| Name | Description |
| --- | --- |
| max_invite_retries | Amount of retries while joining the server |
| max_tasks_retries | Amount of retries while completing the task |
| pause_between_tasks | Pause between the tasks |
| capmonster_api_key | API key from https://capmonster.cloud/Dashboard |
| 2captcha_api_key | API key from https://2captcha.com/ |



## 🗂️ Data

Данные в папке data:

| Name | Description |
| --- | --- |
| discord_tokens.txt | DISCORD account tokens |
| failed_tokens.txt | Failed tokens |
| new_names.txt | Contains names for the name change function |
| new_passwords.txt | Contains new passwords for the password change feature |
| new_usernames.txt | Contains new usernames for the username change function |
| passwords.txt | Contains current account passwords |
| proxies.txt | Contains a proxy in the format user:pass@ip:port |
| profile_pictures | The folder contains pictures to change in profiles |

## Disclaimer

The automation of User Discord accounts also known as self-bots is a violation of Discord Terms of Service & Community guidelines and will result in your account(s) being terminated. Discretion is adviced. I will not be responsible for your actions. Read about Discord Terms Of service and Community Guidelines

Discord StarLabs was written as a proof of concept that Discord accounts can be automated and can perform actions beyond the scope of regular Discord Users like sending Embeds so that Discord can make changes. The Discord StarLabs authors are released of any liabilities which your usage may entail.


