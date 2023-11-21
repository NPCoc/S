
![Logo](https://i.ibb.co/RQzG7Zp/8e4fafbd-9319-4653-9f5a-fdf0f84974e7.png)

# StarLabs - Discord 


## Config

max_invite_retries = 1 - количество попыток входа на сервер. Важно: если значение стоит больше 1, то попытки будут кратно увеличиться учитывая max_tasks_retries;проще говоря, если max_invite_retries = 3 и max_tasks_retries = 3 то бот попытается войти на сервер 3*3=9 раз.

max_tasks_retries = 3 - максимальное количество попыток, которое бот будет пытаться выполнить любое действие из меню.

pause_between_tasks = 1-3 - пауза между каждым действием. в данном примере и по умолчанию, пауза будет случайная от 1 до 3 секунд. 

capmonster_api_key = x - ключ от https://capmonster.cloud/Dashboard

2captcha_api_key = x - ключ от https://2captcha.com/.

## Data

Данные в папке data:

discord_tokens.txt - сюда необходимо вставить дискорд токены. 1 строчка = 1 токен

failed_tokens.txt - вставлять ничего не нужно, сюда бот будет сохранять токены, с которыми 
не получилось выполнить задания.

new_names.txt - сюда нужно вставить новые имена для функции смены имен.  1 строка = 1 имя

new_passwords.txt - новые пароли для функции смены паролей. 1 строчка = 1 пароль

new_usernames.txt - новые юзернеймы для функции смены юзернеймов. 1 строка = 1 юзернейм

passwords.txt - текущие пароли от аккаунтов. необходимы для функций смены паролей, смены юзернейма и аватарки профиля (иногда)

proxies.txt - прокси в формате user:pass@ip:port. 1 строка = 1 прокси

profile_pictures - папка для картинок, которые будут использованы при смене аватарок. 1 картинка = 1 аккаунт, по очереди.


## Links

PUBLIC: https://t.me/StarLabsTech

CHAT: https://t.me/StarLabsChat

DONATION EVM ADDRESS: 0x620ea8b01607efdf3c74994391f86523acf6f9e1
