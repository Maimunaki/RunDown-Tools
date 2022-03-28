import self as self

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('discum')
install_and_import('colorama')
install_and_import('datetime')
from colorama import init, Fore, Back, Style
init(convert=True)
import re
import time
import random
from colorama import Fore, init
from sys import stdout
import requests
import os
if os.name != "nt":
    exit()

class Main:
    def __init__(self):
        clear()
        try:
            self.main_menu()
        except KeyboardInterrupt:
            Main()

init(convert=True, autoreset=True)
green, red, white, cyan, yellow, reset = (
    Fore.LIGHTGREEN_EX,
    Fore.LIGHTRED_EX,
    Fore.WHITE,
    Fore.LIGHTCYAN_EX,
    Fore.YELLOW,
    Fore.RESET,
)

def clear():
    if os.name == "nt":
        return os.system("cls")
    else:
        return os.system("clear")

pref2 = f"{white}[{red}!{white}]{reset} "
pref = f"{white}[{red}>{white}]{reset} "

def logo():
    print(Fore.MAGENTA + f"""                                                                                                                  
   ####                              #####                                                  
  ## ##             ##              ##   ##                            ##                   
  ## ##   ####   ##   ## ######     ##      ######  ######   #####  ##   ## ######   #####  
  ## ##      ##  ##  ### ##   ##    ##        ##    ##   ## ##   ## ##  ###   ##    ##      
  ## ##   #####  ## # ## ######     ##        ##    ######  ######  ## # ##   ##    ##      
 ####### ##  ##  ###  ## ##         ##   ##   ##    ##      ##      ###  ##   ##    ##      
 ##   ##  ###### ##   ## ##          #####    ##    ##       #####  ##   ##   ##     #####
 
""" + Fore.WHITE + f"{white}[{red}!{white}]{reset} BY MAIMUNAKI :)" + Fore.WHITE)

os.system("title RunDown Invite Checker")

inviteRegex = r'.*(discord.(gg|io|me|li)|discordapp.com/invite|discord.com/invite)/([A-Z-a-z-0-9]+)'

def get_info():
    with open(input(f"\n{pref2}INVITES FILE PATH FOR CHECKING:" + f"\n{pref}").replace('"', "").strip()) as f:
        ext = f.readlines()
        for code in ext:
            code = code.replace("\n", "")
            code = code.replace("https://discord.gg/", "")
            code = code.replace("http://discord.gg/", "")
            code = code.replace("discord.gg/", "")
            code = code.replace("https://discord.com/invite/", "")
            code = code.replace("http://discord.com/invite/", "")
            code = code.replace("discord.com/invite/", "")
            code = code.split(" ")
            code = code[0]

            os.system("cls")
            logo()

            try:
                r = requests.get(
                    f"https://discord.com/api/v6/invites/{code}?with_counts=true",
                    timeout=3,
                )
                data = r.json()
                try:
                    print(f"\n{pref2}MINIMUM MEMBER COUNT:")

                    self.min_members_count = int(input(f"{pref}"))
                    name = data["guild"]["name"]
                    total_count = data["approximate_member_count"]
                    online_count = data["approximate_presence_count"]
                    os.system("cls")
                    logo()
                    text = f.read()
                    # Split lines
                    lines = text.split("\n")
                    # Remove empty lines
                    lines = list(filter(None, lines))
                    # Loop through lines
                    os.system("cls")
                    logo()
                    print(f"\n{pref2}DELAY PER CHECK:")
                    delay = int(input(f"{pref}"))
                    for line in ext:
                        # Check if line matches regex
                        if re.match(inviteRegex, line):
                            # Get code
                            code = re.search(inviteRegex, line).group(3)
                            # Check if line is a valid invite
                            if total_count >= self.min_members_count:
                                if invite_check(code):
                                    print("[" + Fore.GREEN + "WORKING" + Fore.WHITE + "]" + " VALID INVITE: discord.gg/" + code)
                                    time.sleep(delay)
                                    # Check if it's in valid.txt, if not add it
                                    # creates file if it doesn't exist
                                    with open("valid.txt", "a+") as f:
                                        if "discord.gg/{}".format(code) not in f.read():
                                            f.write("discord.gg/{}\n".format(code))
                                            f.close
                            else:
                                if total_count < self.min_members_count:
                                    print("[" + Fore.RED + "INVALID" + Fore.WHITE + "]" + " INVALID INVITE: discord.gg/" + code)
                                    time.sleep(delay)
                                    f.close






                except:
                    print(Fore.RED + f"{pref2}" + Fore.RED + "ERROR GETTING INVITE DATA" + Fore.WHITE)
                    time.sleep(2)
                    main(self)
            except:
                print(Fore.RED + f"{pref2}" + Fore.RED + "ERROR CONNECTING TO DISCORD API" + Fore.WHITE)
                time.sleep(2)
                main(self)

def invite_check(code):
    """
        check if discord invite code is valid
        :param code: discord invite code
        :return: True if valid, False if not
    """
    r = requests.get("https://discordapp.com/api/v6/invite/" + code)
    if r.status_code == 200:
        return True
    elif r.status_code == 429:
        retry_after = r.json()['retry_after']
        # Convert to seconds
        retry_after = retry_after / 1000
        print("You are being rate limited. Waiting " +
              str(int(retry_after) + 1) + " seconds.")
        time.sleep(int(retry_after) + 1)
        return invite_check(code)
    else:
        return False



def main(self):
    os.system("cls")
    logo()
    print(f"""
[{red}1{reset}] RE-FORMAT
[{red}2{reset}] CHECK""")
    mainmenu = input(f"[{red}>{reset}] ")
    if mainmenu == "1":
        os.system("cls")
        logo()
        ins = input(f"\n{pref2}INVITES FILE PATH FOR RE-FORMATTING:" + f"\n{pref}").replace('"', "").strip()
        cows = []
        with open(ins, "r+", encoding="utf-8", errors="ignore") as f:
            codes = f.read().splitlines()
            for code in codes:
                pholder = "https://discord.gg/"
                code = code.replace("https://discord.gg/", "")
                code = code.replace("discord.gg/", "")
                pholder += code
                cows.append(pholder)
        os.remove(ins)

        with open(ins, "a", encoding="utf-8", errors="ignore") as f:
            for line in cows:
                f.write(line + "\n")
        print(f"{pref2}" + Fore.GREEN + "DONE" + Fore.WHITE)
        time.sleep(1)
        main(self)
            # Read file
    elif mainmenu == "2":
        os.system("cls")
        logo()
        get_info()





if __name__ == "__main__":
    os.system("cls")
    main(self)

