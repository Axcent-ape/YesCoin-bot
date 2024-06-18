# YesCoin-bot
clicker for https://t.me/theYescoin_bot/Yescoin

More crypto themes and softs in telegram: [ApeCryptor](https://t.me/+_xCNXumUNWJkYjAy "ApeCryptor") 🦧
Additional soft information: https://t.me/ApeCryptorSoft/93

## Functionality
| Functional                                                       | Supported |
|------------------------------------------------------------------|:---------:|
| Multithreading                                                   |     ✅     |
| Binding a proxy to a session                                     |     ✅     |
| Auto-complete tasks; claim points; claim daily boosts            |     ✅     |
| Random sleep time between accounts, complete tasks, claim points |     ✅     |
| Support pyrogram .session                                        |     ✅     |
| Get statistics for all accounts                                  |     ✅     |

## Settings data/config.py
| Setting                      | Description                                                                                    |
|------------------------------|------------------------------------------------------------------------------------------------|
| **API_ID / API_HASH**        | Platform data from which to launch a Telegram session                                          |
| **DELAYS-ACCOUNT**           | Delay between connections to accounts (the more accounts, the longer the delay)                |
| **DELAYS-CLICKS**            | Delay between clicks                                                                           |
| **DELAYS-TASKS**             | Delay between completed tasks                                                                  |
| **COMPLETE_TASKS**           | Auto complete tasks True/False                                                                 |
| **AUTOUPGRADE_FILL_RATE**    | Autoupgrade fill rate; [True/False (use/no use), max upgrade lvl]                              |
| **MINIMUM_ENERGY**           | Minimum allowable energy                                                                       |
| **BOOSTERS-USE_CHESTS**      | Spent daily boost chests True/False                                                            |
| **BOOSTERS-USE_RECOVERY**    | Spent daily boost energy recover True/False                                                    |
| **PROXY_TYPE**               | Proxy type for telegram session                                                                |
| **WORKDIR**                  | directory with session                                                                         |

## Requirements
- Python 3.9 (you can install it [here](https://www.python.org/downloads/release/python-390/)) 
- Telegram API_ID and API_HASH (you can get them [here](https://my.telegram.org/auth))

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
## Usage
1. Run the bot:
   ```bash
   python main.py
   ```
