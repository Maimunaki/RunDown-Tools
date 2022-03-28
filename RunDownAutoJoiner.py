import os
def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import('uuid')
os.system("cls")
install_and_import('random_user_agent')
os.system("cls")
install_and_import('colorama')
os.system("cls")
install_and_import('requests')
os.system("cls")
install_and_import('discum')
os.system("cls")
install_and_import('selenium')
os.system("cls")
install_and_import('stdiomask')
os.system("cls")
install_and_import('discord_webhook')
os.system("cls")
install_and_import('datetime')
os.system("cls")

import webbrowser, time, ctypes, re, random, string, json, subprocess, hashlib, getpass, platform, socket
from requests import exceptions
from datetime import datetime
from requests.api import post
from time import daylight, sleep
from json import loads, dumps
from discord_webhook import DiscordWebhook
from selenium import webdriver
from colorama import Fore, Style, Back
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

current_date = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")

try:
    os.system(Fore.BLACK + "pip install urllib3==1.25.8" + Fore.WHITE)
except:
    pass
os.system("cls")

colorama.init()

black = Fore.BLACK
red = Fore.LIGHTRED_EX
green = Fore.GREEN;
Style.BRIGHT;
Fore.GREEN
reset = Fore.RESET
token = ""

logo = f""" 
{Style.BRIGHT}{Fore.RED} ██▀███   █    ██  ███▄    █{Style.BRIGHT}{Fore.BLUE} ▓█████▄  ▒█████   █     █░ ███▄    █ 
{Style.BRIGHT}{Fore.RED}▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █{Style.BRIGHT}{Fore.BLUE} ▒██▀ ██▌▒██▒  ██▒▓█░ █ ░█░ ██ ▀█   █ 
{Style.BRIGHT}{Fore.RED}▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██{Style.BRIGHT}{Fore.BLUE}▒░██   █▌▒██░  ██▒▒█░ █ ░█ ▓██  ▀█ ██▒
{Style.BRIGHT}{Fore.RED}▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██{Style.BRIGHT}{Fore.BLUE}▒░▓█▄   ▌▒██   ██░░█░ █ ░█ ▓██▒  ▐▌██▒
{Style.BRIGHT}{Fore.RED}░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██{Style.BRIGHT}{Fore.BLUE}░░▒████▓ ░ ████▓▒░░░██▒██▓ ▒██░   ▓██░
{Style.BRIGHT}{Fore.RED}░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒{Style.BRIGHT}{Fore.BLUE}  ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ▒░   ▒ ▒ 
{Style.BRIGHT}{Fore.RED}  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒{Style.BRIGHT}{Fore.BLUE}░ ░ ▒  ▒   ░ ▒ ▒░   ▒ ░ ░  ░ ░░   ░ ▒░
{Style.BRIGHT}{Fore.RED}  ░░   ░  ░░░ ░ ░    ░   ░ ░{Style.BRIGHT}{Fore.BLUE}  ░ ░  ░ ░ ░ ░ ▒    ░   ░     ░   ░ ░ 
{Style.BRIGHT}{Fore.RED}   ░        ░              ░{Style.BRIGHT}{Fore.BLUE}    ░        ░ ░      ░             ░ 
{Style.BRIGHT}{Fore.RED}                            {Style.BRIGHT}{Fore.BLUE}  ░                                  {reset}"""

def main():
    try:
        os.mkdir("output")
    except:
        pass
    os.system("cls")
    global token
    print(logo)
    print(f"{Fore.WHITE}Welcome To RunDown! Please Select A Function From The List Below:")
    print(f"""
[{red}0{reset}] Join The Discord
[{red}1{reset}] Server Scraper
[{red}2{reset}] Discord Invite Checker
[{red}3{reset}] Server Joiner""")
    mainmenu = input(f"[{red}>{reset}] ")
    if mainmenu == "0":
        os.system("cls")
        print(f"[{red}!{reset}] Opening Link In: 3.")
        time.sleep(1)
        print(f"[{red}!{reset}] Opening Link In: 2..")
        time.sleep(1)
        print(f"[{red}!{reset}] Opening Link In: 1...")
        time.sleep(1)
        print(f"[{red}!{reset}] Opened.")
        new = 2
        url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        webbrowser.open(url, new=new)
        os.system("cls")
        main()
    elif mainmenu == "1":
        os.system("cls")
        print(logo)
        token = input(f"[{red}!{reset}] Enter Token: ")
        bot = discum.Client(token=str(token), log=False)

        @bot.gateway.command
        def helloworld(resp):
            if resp.event.ready_supplemental:  # ready_supplemental is sent after ready
                user = bot.gateway.session.user
                print(
                    Fore.GREEN + "[>] Logged In As {}#{}".format(user['username'], user['discriminator']) + Fore.WHITE)

        @bot.gateway.command
        def detectinv(resp):
            if resp.event.message:
                message = resp.parsed.auto()
                if "discord.gg/" in message['content']:
                    messagecontent = message['content']
                    scrapedlinks = re.findall(r'(https?://[^\s]+)', messagecontent)
                    print(f"Found Message With Links: " + Fore.GREEN + str(scrapedlinks) + Fore.WHITE + " Saved To TXT")
                    invitestxt = open("output/invites.txt", "a+")
                    for x in range(len(scrapedlinks)):
                        try:
                            invitestxt.write("\n" + str(scrapedlinks[x]))
                        except Exception as e:
                            print("Error Writing Invite. Probably Invalid: " + str(e))
                        invitestxt.close()

        bot.gateway.run(auto_reconnect=True)
    elif mainmenu == "2":
        os.system("cls")
        print(logo)
        print(f"""
[{red}1{reset}] Invites Checker
[{red}2{reset}] Format Converter""")
        mainmenu = input(f"[{red}>{reset}] ")
        if mainmenu == "1":
            os.system("cls")
            print(logo)
            listname = input(f"[{red}!{reset}] Enter Invites List: ")
            delay = int(input(f"[{red}!{reset}] Enter Delay In Seconds: "))
            try:
                file = open(listname, "rt")
                data = file.read()
                try:
                    data = data.replace(f"https://discord.gg/", "")
                except:
                    pass
                try:
                    data = data.replace(f"discord.gg/", "")
                except:
                    pass
                file.close()
                fin = open(listname, "wt")
                fin.write(data)
                fin.close()
            except FileNotFoundError:
                print(f"[{red}ERROR{reset}] File Doesn't Exist!")
                input()
                main()
            try:
                ok = datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
                with open(listname) as f:
                    for line in f:
                        try:
                            tooreexiscool = requests.get(
                                f"https://canary.discord.com/api/v6/invite/{line}?with_counts=true")
                            if tooreexiscool.status_code == 200:
                                infokekr = json.loads(tooreexiscool.text)
                                print(
                                    f"{reset}[{red}+{reset}] Name: {green}{infokekr['guild']['name']}{reset} | Members: {green}{infokekr['approximate_member_count']}{reset} | Link: {green}{infokekr['code']}")
                                with open(f"output/Working_Invites[{ok}].txt", "a+") as out:
                                    out.write(line)
                                    out.close
                                time.sleep(delay)
                            elif tooreexiscool.status_code == 404:
                                time.sleep(delay)
                                pass
                            elif tooreexiscool.status_code == 429:
                                print(f"[{red}!{reset}] Rate-limited! Sleeping 60s")
                                time.sleep(60)
                            else:
                                time.sleep(delay)
                                pass
                        except KeyboardInterrupt:
                            print(f"[{red}!{reset}] Stopped!")
                            time.sleep(delay)
                            main()
                        except Exception as e:
                            print(f"[{red}ERROR{reset}] {e}")
                            time.sleep(delay)
            except KeyboardInterrupt:
                print(f"[{red}!{reset}] Stopped!")
                time.sleep(1)
                main()
        elif mainmenu == "2":
            os.system("cls")
            print(logo)
            ins = input(f"[{red}!{reset}] Enter Invites File You Want To Re-Formatt: ").replace('"', "")

            cows = []
            with open(ins, "r+", encoding="utf-8", errors="ignore") as f:
                codes = f.read().splitlines()
                for code in codes:
                    pholder = "https://discord.gg/"
                    code = code.replace("https://discord.gg/", "")
                    code = code.replace("discord.gg/", "")
                    pholder += code
                    print(pholder)
                    cows.append(pholder)
            os.remove(ins)

            with open(ins, "a", encoding="utf-8", errors="ignore") as f:
                for line in cows:
                    f.write(line + "\n")
        print(Fore.GREEN + "Done" + Fore.WHITE)
        time.sleep(1)
        main()

    elif mainmenu == "4":
        os.system("cls")
        print("""
                                            .%%%#                               
                                           %%%%%%%%                             
                                           %%%%%%%/                             
                              %%%%%%%%%%%%%%# *,       %%%.                     
                            %%%%%%%%%%%%%%%%%%%/    .%%%%%.                     
                          %%%%%    %%%%%%%%%%%%%%%(%%%%%                        
                        %%%%%    %%%%%%%%%%*  .%%%%%%(                          
                       .%%%   .%%%%%%%%%%*       .,                             
                            .%%%%%%%%%%,                                        
                           %%%%%%%%%%%%%%.                                      
                         %%%%%%%%*%%%%%%%%%%                                    
            ,%%%%%%%%%%%%%%%%%%     /%%%%%%%%,                                  
@@@@@@@@   #%%%%%%%%%%%%%%%%%          %%%%%%                                   
@@@@@@@@.                              (%%%%#                                   
@@@@@@@@,                              %%%%%.                                   
&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,     ,%%%%%                                    
&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/     %%%%%.                                    
%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/    .%%%%%                                     
                        .@@@@@@@&(/////((//////////////*.                       
                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                      
                         &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.                      
                                               .#@@@@@@@@*                      
                                                /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                                                /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
        print(f"\n[{red}:){reset}] Maimunaki Says Hi!")
        time.sleep(5)
        main()
    elif mainmenu == "3":
        os.system("cls")
        print(logo)
        os.system("cls")
        print(logo)
        token = input(f"[{red}!{reset}] Enter Token: ")
        browserconfig = input(f"[{red}!{reset}] Select Browser (Chrome Or Firefox): ")
        if browserconfig != "chrome" or browserconfig != "firefox" or browserconfig != "Chrome" or browserconfig != "Firefox":
            seleniumjoiner(browserconfig)
        else:
            print("Not valid")

    else:
        main()


def seleniumjoiner(browser):

    filepath = input(f"[{red}!{reset}] Select Invite File: ")
    invsraw = open(filepath, "r")
    invs = invsraw.read().split("\n")
    speed = int(input(f"[{red}!{reset}] Select Speed (Seconds): "))

    print( + "Secret")

    print(f"Opening Browser!")
    if browser == "chrome" or browser == "Chrome":
        print("Using Chrome!")
        try:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')  # engage headless mode
            driver = webdriver.Chrome(chrome_options=options)
        except Exception as e:
            print("Error Opening Chome: " + str(e))
            print("Press Enter To Close!")
            input("> ")
            exit()
    elif browser == "firefox" or browser == "Firefox":
        print("Using Firefox!")
        try:
            options = webdriver.FirefoxOptions()
            options.add_argument('headless')  # engage headless mode
            driver = webdriver.Firefox(firefox_options=options)


        except Exception as e:
            print("Error Opening Firefox: " + str(e))
            print("Press Enter To Close!")
            input("> ")
            exit()

    print("Logging In!")
    try:
        driver.get("https://discord.com/login")
        time.sleep(2)
        driver.execute_script("""
        function login(token) {
            setInterval(() => {
              document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
            }, 50);
            setTimeout(() => {
              location.reload();
            }, 2500);
          }

        login('""" + str(token) + """');""")
        print(Fore.GREEN + "Should Be Logged In Now! Joining" + Fore.WHITE)
    except Exception as e:
        print("Error Logging In!: " + str(e))
        print("Press Enter To Close!")
        input("> ")
        exit()

#ODkzNDc5NjA0MTUxNTE3MjU1.YVcD3A.H4goZ2zD6LR1VhIJg-oWTHHz14M

    for x in range(len(invs)):
        if invs[x].startswith("https://discord.gg") == False:
            print("bad link")
        else:

            actualinvite = invs[x].replace('https://discord.gg/', '')
            try:
                time.sleep(int(speed))
                driver.get(str(invs[x]))
                time.sleep(2)
                driver.find_element_by_class_name("contents-18-Yxp").click()
                print("Should Have Joined Server!")
            except Exception as e:
                print(e)
                print("Error joining guild - Continuing")


if __name__ == "__main__":
    os.system("cls")
    main()
