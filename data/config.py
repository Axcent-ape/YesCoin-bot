# api id, hash
API_ID = 1488
API_HASH = 'abcde1488'

# auto complete tasks True/False
COMPLETE_TASKS = True

# autoupgrade fill rate; [True/False (use/no use), max upgrade lvl]
AUTOUPGRADE_FILL_RATE = [True, 10]

# minimum allowable energy
MINIMUM_ENERGY = 50

# daily boosters; True/False
BOOSTERS = {
    'USE_CHESTS': True,    # Chests
    'USE_RECOVERY': True   # Full energy recover
}

DELAYS = {
    'ACCOUNT': [5, 15],  # delay between connections to accounts (the more accounts, the longer the delay)
    'CLICKS': [2, 10],   # delay between clicks
    'TASKS': [1, 3]      # delay between completed tasks
}

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# session folder (do not change)
WORKDIR = "sessions/"

# timeout in seconds for checking accounts on valid
TIMEOUT = 30

SOFT_INFO = f"""{"Yescoin".center(40)}
Soft for https://t.me/theYescoin_bot; claim points;
claim daily boosters; complete tasks; upgrade 'FillRate';
register accounts in web app

The soft also collects statistics on accounts and uses proxies from {f"the {PROXY['PROXY_PATH']} file" if PROXY['USE_PROXY_FROM_FILE'] else "the accounts.json file"}
To buy this soft with the option to set your referral link write me: https://t.me/Axcent_ape
"""
