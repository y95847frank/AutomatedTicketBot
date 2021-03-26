# AutomatedTicketBot

### An automated python bot that reserves kktix tickets.

[![GitHub forks](https://img.shields.io/github/forks/y95847frank/AutomatedTicketBot)](https://github.com/y95847frank/AutomatedTicketBot/network)
[![GitHub stars](https://img.shields.io/github/stars/y95847frank/AutomatedTicketBot)](https://github.com/y95847frank/AutomatedTicketBot/stargazers)
[![GitHub license](https://img.shields.io/github/license/y95847frank/AutomatedTicketBot)](https://github.com/y95847frank/AutomatedTicketBot/blob/master/LICENSE)
[![HitCount](http://hits.dwyl.com/y95847frank/AutomatedTicketBot.svg)](http://hits.dwyl.com/y95847frank/AutomatedTicketBot)


### Execution

To book tickets in kktix, you need to fill your account and concert information in `cofig.yml` beforehead. Or, you  can update these through passing arguments as executing the script. Here is the script for booking concert tickets in kktix.

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
python3 
```

Can use the package as:
```python
import AutoTicketsBot as tBot
...
```

### Test

There're some testing program in tests directory (https://github.com/y95847frank/AutomatedTicketBot/tree/main/tests).

Test the bot
```bash
python tests/test.py
```