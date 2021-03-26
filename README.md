# AutomatedTicketBot

### An automated python bot that reserves kktix tickets.

[![GitHub forks](https://img.shields.io/github/forks/y95847frank/AutomatedTicketBot)](https://github.com/y95847frank/AutomatedTicketBot/network)
[![GitHub stars](https://img.shields.io/github/stars/y95847frank/AutomatedTicketBot)](https://github.com/y95847frank/AutomatedTicketBot/stargazers)
[![GitHub license](https://img.shields.io/github/license/y95847frank/AutomatedTicketBot)](https://github.com/y95847frank/AutomatedTicketBot/blob/master/LICENSE)
[![HitCount](http://hits.dwyl.com/y95847frank/AutomatedTicketBot.svg)](http://hits.dwyl.com/y95847frank/AutomatedTicketBot)

### Goal

This python bot can reserve concert tickets in kktix website using Splinter. The bot would start two minutes before the scheduled time. It log in to the home page automatically. When the website starts selling tickets, the bot would refresh the webpage and automatically fills in registration details. The bot not only refresh webpage faster than any human, but also is able to avoid any mistakes or delays.

### Execution

To book tickets in kktix, you need to fill your account and concert information in `cofig.yml` beforehead. Or, you  can update these arguments with `script/updateConfig.py`, which is an interative program. Here is the script for booking concert tickets in kktix.

Try:
```bash
python3 scripts/concert2021.py
```
### Installation

The bot requires a webdriver. I only tested with chromedriver (http://chromedriver.chromium.org/), but it should work well with other webriver.

Install AutomatedTicketBot package via:
```bash
python setup.py install
```

Then, set the path and account information via:
```bash
python3 scripts/updateConfig.py -d config.yml
```

Eventually, use the package as:
```python
import AutoTicketsBot as tBot
...
```

### Test

There's a testing program in the tests directory (https://github.com/y95847frank/AutomatedTicketBot/tree/main/tests).

Test the bot:
```bash
python tests/test.py
```