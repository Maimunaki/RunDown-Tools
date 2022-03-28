def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)
install_and_import('subprocess')
install_and_import('easygui')
install_and_import('ctypes')
install_and_import('colorama')
install_and_import('hashlib')
install_and_import('stdiomask')
install_and_import('threading')
install_and_import('datetime')
install_and_import('dhooks')
install_and_import('os')
install_and_import('time')
install_and_import('requests')
install_and_import('random')
install_and_import('sys')
install_and_import('string')
install_and_import('getpass')
install_and_import('discord_webhook')
import colorama
import easygui
import hashlib
import os
import time
import requests
import ctypes
import random
import sys
import subprocess
import string
import getpass
import stdiomask
import discord_webhook
from datetime import datetime
from time import daylight, sleep
from colorama import Fore, Style, Back
from json import loads, dumps
from discord_webhook import DiscordWebhook
from colorama import Fore, Style, init
from easygui import fileopenbox
from ctypes import windll
import random
from sys import exit
init(convert=True)

red = Fore.LIGHTRED_EX
green = Fore.GREEN; Style.BRIGHT; Fore.GREEN
reset = Fore.RESET



logo = f"""
{Style.BRIGHT}{Fore.RED}▄▄▄  ▄• ▄▌ ▐ ▄ {Style.BRIGHT}{Fore.BLUE}·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄     {Style.BRIGHT}{Fore.WHITE}▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄  
{Style.BRIGHT}{Fore.RED}▀▄ █·█▪██▌•█▌▐█{Style.BRIGHT}{Fore.BLUE}██▪ ██ ▪     ██· █▌▐█•█▌▐█    {Style.BRIGHT}{Fore.WHITE}▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·
{Style.BRIGHT}{Fore.RED}▐▀▀▄ █▌▐█▌▐█▐▐▌{Style.BRIGHT}{Fore.BLUE}▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌▐█▐▐▌    {Style.BRIGHT}{Fore.WHITE}▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄ 
{Style.BRIGHT}{Fore.RED}▐█•█▌▐█▄█▌██▐█▌{Style.BRIGHT}{Fore.BLUE}██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌    {Style.BRIGHT}{Fore.WHITE}▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌
{Style.BRIGHT}{Fore.RED}.▀  ▀ ▀▀▀ ▀▀ █▪{Style.BRIGHT}{Fore.BLUE}▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪     {Style.BRIGHT}{Fore.WHITE}▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀ {Fore.RESET}

Welcome To RunDown Editor! Please Select A Function From The List Below:
"""

def module_logo(name):
    print(f"""
{Style.BRIGHT}{Fore.RED}▄▄▄  ▄• ▄▌ ▐ ▄ {Style.BRIGHT}{Fore.BLUE}·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄     {Style.BRIGHT}{Fore.WHITE}▄▄▄ .·▄▄▄▄  ▪  ▄▄▄▄▄      ▄▄▄  
{Style.BRIGHT}{Fore.RED}▀▄ █·█▪██▌•█▌▐█{Style.BRIGHT}{Fore.BLUE}██▪ ██ ▪     ██· █▌▐█•█▌▐█    {Style.BRIGHT}{Fore.WHITE}▀▄.▀·██▪ ██ ██ •██  ▪     ▀▄ █·
{Style.BRIGHT}{Fore.RED}▐▀▀▄ █▌▐█▌▐█▐▐▌{Style.BRIGHT}{Fore.BLUE}▐█· ▐█▌ ▄█▀▄ ██▪▐█▐▐▌▐█▐▐▌    {Style.BRIGHT}{Fore.WHITE}▐▀▀▪▄▐█· ▐█▌▐█· ▐█.▪ ▄█▀▄ ▐▀▀▄ 
{Style.BRIGHT}{Fore.RED}▐█•█▌▐█▄█▌██▐█▌{Style.BRIGHT}{Fore.BLUE}██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌    {Style.BRIGHT}{Fore.WHITE}▐█▄▄▌██. ██ ▐█▌ ▐█▌·▐█▌.▐▌▐█•█▌
{Style.BRIGHT}{Fore.RED}.▀  ▀ ▀▀▀ ▀▀ █▪{Style.BRIGHT}{Fore.BLUE}▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪     {Style.BRIGHT}{Fore.WHITE}▀▀▀ ▀▀▀▀▀• ▀▀▀ ▀▀▀  ▀█▄▀▪.▀  ▀ {Fore.RESET}

                                 {Fore.BLUE}[{Fore.RED}MODULE{Fore.BLUE}]{Fore.RESET} ~> {Fore.RED}{name}{Fore.RESET}
""")

modules = [
    "Anti Dupe",
    "Sorter A to Z",
    "Sorter Z to A",
    "Email to User",
    "User to Email",
    "Randomizer",
    "Split per X line(s)",
    "Split per X file(s)",
    "Add prefix to beginning of the combo line",
    "Add prefix to beginning of password",
    "Add suffix to end of the combo line",
    "Add suffix to end of email (before @)",
    "Remove bad lines (email:pass)",
    "Remove bad lines (user:pass)",
    "Remove Capture",
    "Domain Sorter",
    "Domains Extractor",
    "Combo Combiner",
    "Delimiter Switcher",
    "Basic Edits",
    "Advanced Edits"
]



def choose_combo():
    while True:
        try:
            r = open(fileopenbox(default='*.txt', title="Select combo file | Star"), encoding='utf-8').read().split("\n")
            return [x.strip() for x in r if x!='']
        except Exception as e:
            ee = input(f'{Style.BRIGHT}Press {Fore.RED}[ENTER]{Fore.RESET} To select file or type {Fore.RED}[Back]{Fore.RESET}... ')
            if ee == '':
                continue
            elif ee == "Back":
                main()
            else:
                continue


def save(module: str, name: str, filename: str, lines):
	if not os.path.exists(f'./results/{module}/{name}'):
		os.makedirs(f'./results/{module}/{name}')
	with open(f'./results/{module}/{name}/{filename}.txt', 'w+', encoding='utf-8') as f:
		for l in lines:
			f.write(f'{l}\n')


def edit(module):
    if module == "Anti Dupe":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Antidupe | RunDown Editor")
        module_logo("Antidupe")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] to start editing... ")

        start = time.time()
        v = list(dict.fromkeys([x for x in lines if x!='']))
        save(module = 'Anti Dupe', name = f'Dupes Removed ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully saved [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] lines!")
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Removed [{Fore.RED}{(len(lines) - len(v)):,}{Fore.RESET}] Duplicate lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f'{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...')
        main()


    elif module == "Sorter A to Z":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Sorter A to Z | RunDown Editor")
        module_logo("Sorter A to Z")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = list(sorted([x.strip() for x in lines if x != '']))
        save(module = 'Sorter A to Z', name = f'Sorted A to Z ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully sorted [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Sorter Z to A":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Sorter Z to A | RunDown Editor")
        module_logo("Sorter Z to A")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = list(sorted([x.strip() for x in lines if x != ''], reverse=True))
        save(module = 'Sorter Z to A', name = f'Sorted Z to A ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully sorted [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Email to User":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Email to User | RunDown Editor")
        module_logo("Email to User")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")
        start = time.time()
        v = [x.strip().split(":")[0].split("@")[0] + ":" + x.split(":")[1] for x in lines if "@" and ":" in x]
        save(module = 'email to user', name = f'email To user ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully converted [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines from email to user in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "User to Email":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("User to Email | RunDown Editor")
        module_logo("User to Email")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        domain = input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Enter domain (including @): ")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [x.strip().split(":")[0] + str(domain) + ":" + x.split(":")[1] for x in lines if ":" in x]
        save(module = 'user to email', name = f'user To email ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully converted [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines from user to email in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Randomizer":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Randomizer | RunDown Editor")
        module_logo("Randomizer")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        d = [(random.random(), x) for x in lines]
        d.sort()
        v = [x for _, x in d if x!='']
        save(module = 'Randomizer', name = f'Randomizer ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        
        print("\n")
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully randomized [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Split per X line(s)":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Split per X line(s) | RunDown Editor")
        module_logo("Split per X line(s)")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        liste = []
        a = 0
        linemax = 0
        linemax = int(input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} How many lines per file: "))
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        timer = f'[{time.strftime("%d-%m-%y %H-%M-%S")}]'
        starter = time.time()
        for i in range(0, len(lines)):
            line = lines[i]
            liste.append(line)
            e = len(lines) - i
            if len(liste) == linemax:
                a += 1
                save(module = 'Split per X line(s)', name = f'Splitted ~ {timer}', lines = liste, filename = f'Split {str(a)}')
                liste = []
        if e < linemax:
            a += 1
            save(module = 'Split per X line(s)', name = f'Splitted ~ {timer}', lines = liste, filename = f'Split {str(a)}')
            liste = []
        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully splitted [{Style.BRIGHT}{Fore.RED}{len(lines):,}{Fore.RESET}] lines into [{Style.BRIGHT}{Fore.RED}{a:,}{Fore.RESET}] Files having [{Fore.RED}{linemax:,}{Fore.RESET}] Lines each in [{Fore.RED}{(time.time() - starter):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Split per X file(s)":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Split per X file(s) | RunDown Editor")
        module_logo("Split per X file(s)")
        lines = choose_combo()

        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        liste = []
        a = 0
        linemax = 0
        filemax = int(input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} How many files: "))
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        timer = f'[{time.strftime("%d-%m-%y %H-%M-%S")}]'
        linemax = int(len(lines)/filemax)
        starter = time.time()
        for i in range(0, len(lines)):
            line = lines[i]
            liste.append(line)
            e = len(lines) - i
            if len(liste) == linemax:
                a += 1
                save(module = 'Split per X file(s)', name = f'Splitted ~ {timer}', lines = liste, filename = f'Split {str(a)}')
                liste = []
        if e < linemax:
            a += 1
            save( module = 'Split per X file(s)', name = f'Splitted ~ {timer}', lines = liste, filename = f'Split {str(a)}')
            liste = []
        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully splitted [{Style.BRIGHT}{Fore.RED}{len(lines):,}{Fore.RESET}] Lines into [{Style.BRIGHT}{Fore.RED}{a:,}{Fore.RESET}] Files in [{Fore.RED}{(time.time() - starter):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] to go back...")
        main()


    elif module == "Add prefix to beginning of the combo line":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Add prefix to beginning of the combo line | RunDown Editor")
        module_logo("Add prefix to beginning of the combo line")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        prefix = input(f'{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Enter prefix: ')
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [str(prefix)+str(x) for x in lines if x != '']
        save(module = 'Add Prefix', name = f'Added prefix [{prefix}] to beginning of combo line ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully added prefix to beginning of [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Add prefix to beginning of password":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Add prefix to beginning of password | RunDown Editor")
        module_logo("Add prefix to beginning of password")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        prefix = input(f'{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Enter prefix: ')
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [x.strip().split(":")[0] + ":" + (prefix) + x.split(":")[1] for x in lines if ":" in x]
        save(module = 'Add Prefix', name = f'Added prefix [{prefix}] to beginning of password ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully added prefix to beginning of [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] to go back...")
        main() 


    elif module == "Add suffix to end of the combo line":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Add suffix to end of the combo line | RunDown Editor")
        module_logo("Add suffix to end of the combo line")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        suffix = input(f'{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Enter suffix: ')
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [str(x)+str(suffix) for x in lines if x != '']
        save(module = 'Add Suffix', name = f'Added suffix [{suffix}] to end of combo line ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully added suffix to end of [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main() 


    elif module == "Add suffix to end of email (before @)":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Add suffix to end of email (before @) | RunDown Editor")
        module_logo("Add suffix to end of email (before @)")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        suffix = input(f'{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Enter suffix: ')
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [x.strip().split("@")[0] + str(suffix) + "@" + x.split("@")[1] for x in lines if x!='']
        save(module = 'Add Suffix', name = f'Added suffix [{suffix}] to end of email ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully added suffix to end of email of [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main() 


    elif module == "Remove bad lines (email:pass)":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Remove bad lines (email:pass) | RunDown Editor")
        module_logo("Remove bad lines (email:pass)")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [x.strip() for x in lines if "@" and ":" in x]
        save(module = 'Remove bad lines [email-pass]', name = f'Removed bad lines ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print("\n")
        print(f'{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Valid lines: [{Fore.RED}{len(v)}{Fore.RESET}]')
        print(f'{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Invalid lines: [{Fore.RED}{len(lines) - len(v)}{Fore.RESET}]')
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully removed [{Fore.RED}{len(lines) - len(v)}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] to go back...")
        main()


    elif module == "Remove bad lines (user:pass)":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Remove bad lines (email:pass) | RunDown Editor")
        module_logo("Remove bad lines (user:pass)")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] tT start editing... ")

        start = time.time()
        v = [x.strip() for x in lines if ":" not in x]
        save(module = 'Remove bad lines [user-pass]', name = f'Removed bad lines ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print(f'\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Valid lines: [{Fore.RED}{len(v)}{Fore.RESET}]')
        print(f'{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Invalid lines: [{Fore.RED}{len(lines) - len(v)}{Fore.RESET}]')
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully removed [{Fore.RED}{len(lines) - len(v)}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] to go back...")
        main()


    elif module == "Remove Capture":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Remove Capture | RunDown Editor")
        module_logo("Remove Capture")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [x.split(":")[0] + ":" + x.split(":")[1].split(" ")[0] for x in lines if x !='']
        save(module = 'Remove Capture', name = f'Capture removed ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')
        print(f'\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Cleaned [{Fore.RED}{len(v)}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!')
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully saved [{Style.BRIGHT}{Fore.RED}{len(v):,}{Fore.RESET}] Lines. Removed [{Fore.RED}{len(lines) - len(v):,}{Fore.RESET}] Invalid lines!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Domain Sorter":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Domain Sorter | RunDown Editor")
        module_logo("Domain Sorter")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        domain = input(f'{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Enter domain (including @): ')
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [x for x in lines if str(domain) in x and x!= '']
        save(module = 'Domain Sorter', name = f'Sorted Domain [{domain}] ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully extracted [{Fore.RED}{len(v):,}{Fore.RESET}] Lines for given domain ({Fore.RED}{str(domain)}{Fore.RESET}) in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Domains Extractor":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Domains Extractor | RunDown Editor")
        module_logo("Domains Extractor")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        e_v = ["@" + x.strip().split("@")[1].split(":")[0] for x in lines]
        v = list(dict.fromkeys([e for e in e_v if e!= '']))
        save(module = 'Domain Extractor', name = f'Extracted Domains  ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully extracted [{Fore.RED}{len(v):,}{Fore.RESET}] Domains in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Combo Combiner":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Combo Combiner | RunDown Editor")
        module_logo("Combo Combiner")
        files = fileopenbox(default='*.txt', title='Select files', multiple=True)

        start = time.time()
        e_v = []
        for file in files:
            with open(file, 'r') as kek:
                lol = kek.read().split('\n')
                for line in lol:
                    e_v.append(line)
        v = list(dict.fromkeys([x for x in e_v if x != '']))
        save(module = 'Combo Combiner', name = f'Combo Combined ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully combined all the files in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Removed [{Fore.RED}{(len(e_v) - len(v)):,}{Fore.RESET}] Duplicate lines from combined file.")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] to go back...")
        main()


    elif module == "Delimiter Switcher":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Delimiter Switcher | RunDown Editor")
        module_logo("Delimiter Switcher")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        delimiter = input(f'{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Enter delimiter: ')
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")

        start = time.time()
        v = [x.strip().split(':')[0] + str(delimiter) + x.split(":")[1] for x in lines]
        save(module = 'Delimiter Switcher', name = f'Delimeter Switched [{delimiter}] ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully switched delimiter of [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Basic Edits":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Basic Edits | RunDown Editor")
        module_logo("Basic Edits")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")


        start = time.time()
        e_v = []
        e_v.extend(x for x in lines if x!= '')

        e_v.extend('!'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '!' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '!' for x in lines if x!= '')

        e_v.extend('?'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '?' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '?' for x in lines if x!= '')

        e_v.extend('@'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '@' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '@' for x in lines if x!= '')

        e_v.extend('*'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '*' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '*' for x in lines if x!= '')

        e_v.extend('123'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '123' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '123' for x in lines if x!= '')

        v = list(dict.fromkeys([x for x in e_v if x != '']))
        
        save(module = 'Basic Edits', name = f'Basic Edits ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully edited [{Fore.RED}{len(lines):,}{Fore.RESET}] to [{Fore.RED}{len(e_v):,}{Fore.RESET}] Lines in [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Saved [{Fore.RED}{len(v)}{Fore.RESET}] Lines after removing [{Fore.RED}{(len(e_v) - len(v)):,}{Fore.RESET}] Duplicates from edited lines.")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To go back...")
        main()


    elif module == "Advanced Edits":
        os.system('cls' if os.name =='nt' else 'clear')
        windll.kernel32.SetConsoleTitleW("Advanced Edits | RunDown Editor")
        module_logo("Advanced Edits")
        lines = choose_combo()
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} [{Fore.RED}{len(lines):,}{Fore.RESET}] Lines got loaded!")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To start editing... ")


        start = time.time()
        e_v = []
        e_v.extend(x for x in lines if x!= '')

        e_v.extend('!'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '!' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '!' for x in lines if x!= '')

        e_v.extend('?'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '?' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '?' for x in lines if x!= '')

        e_v.extend('@'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '@' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '@' for x in lines if x!= '')

        e_v.extend('*'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '*' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '*' for x in lines if x!= '')

        e_v.extend('123'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '123' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '123' for x in lines if x!= '')

        e_v.extend('1'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '1' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '1' for x in lines if x!= '')

        e_v.extend('1234'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '1234' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '1234' for x in lines if x!= '')

        e_v.extend('12345'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '12345' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '12345' for x in lines if x!= '')

        e_v.extend('12'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '12' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '12' for x in lines if x!= '')

        e_v.extend('0'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '0' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '0' for x in lines if x!= '')

        e_v.extend('00'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '00' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '00' for x in lines if x!= '')

        e_v.extend('1!'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '1!' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '1!' for x in lines if x!= '')

        e_v.extend('$'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '$' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '$' for x in lines if x!= '')

        e_v.extend('!@'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '!@' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '!@' for x in lines if x!= '')

        e_v.extend('!@#'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '!@#' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '!@#' for x in lines if x!= '')

        e_v.extend('*$#'+x for x in lines if x!= '')
        e_v.extend(x.strip().split(':')[0] + ':' + '*$#' + x.split(':')[1] for x in lines if x!= '')
        e_v.extend(x + '*$#' for x in lines if x!= '')

        v = list(dict.fromkeys([x for x in e_v if x != '']))
        save(module = 'Advanced Edits', name = f'Advanced Edits ~ [{time.strftime("%d-%m-%y %H-%M-%S")}]', lines = v, filename = 'result')

        print(f"\n{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Successfully Edited [{Fore.RED}{len(lines):,}{Fore.RESET}] To [{Fore.RED}{len(e_v):,}{Fore.RESET}] Lines In [{Fore.RED}{(time.time() - start):,.5f}{Fore.RESET}] Seconds!")
        print(f"{Style.BRIGHT}{Fore.BLUE}({Fore.GREEN}+{Fore.BLUE}){Fore.RESET} Saved [{Fore.RED}{len(v)}{Fore.RESET}] Lines After Removing [{Fore.RED}{(len(e_v) - len(v)):,}{Fore.RESET}] Duplicates from edited lines.")
        input(f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} Press [{Fore.RED}ENTER{Fore.RESET}] To Go Back...")
        main()


def main():
    gay = (f"{Style.BRIGHT}{Fore.BLUE}({Fore.RED}>>{Fore.BLUE}){Fore.RESET} ")
    os.system('cls' if os.name == 'nt' else 'clear')
    windll.kernel32.SetConsoleTitleW("RunDown Editor")
    print(logo)
    print(
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}01{Fore.WHITE}]{Fore.RESET} Anti Dupe\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}02{Fore.WHITE}]{Fore.RESET} Sorter A to Z\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}03{Fore.WHITE}]{Fore.RESET} Sorter Z to A\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}04{Fore.WHITE}]{Fore.RESET} Email to User\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}05{Fore.WHITE}]{Fore.RESET} User to Email\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}06{Fore.WHITE}]{Fore.RESET} Randomizer\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}07{Fore.WHITE}]{Fore.RESET} Split per X line(s)\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}08{Fore.WHITE}]{Fore.RESET} Split per X file(s)\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}09{Fore.WHITE}]{Fore.RESET} Add prefix to beginning of the combo line\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}10{Fore.WHITE}]{Fore.RESET} Add prefix to beginning of password\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}11{Fore.WHITE}]{Fore.RESET} Add suffix to end of the combo line\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}12{Fore.WHITE}]{Fore.RESET} Add suffix to end of email (before @)\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}13{Fore.WHITE}]{Fore.RESET} Remove bad lines (email:pass)\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}14{Fore.WHITE}]{Fore.RESET} Remove bad lines (user:pass)\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}15{Fore.WHITE}]{Fore.RESET} Remove Capture\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}16{Fore.WHITE}]{Fore.RESET} Domain Sorter\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}17{Fore.WHITE}]{Fore.RESET} Domains Extractor\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}18{Fore.WHITE}]{Fore.RESET} Combo Combiner\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}19{Fore.WHITE}]{Fore.RESET} Delimiter Switcher\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}20{Fore.WHITE}]{Fore.RESET} Basic Edits\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}21{Fore.WHITE}]{Fore.RESET} Advanced Edits\n'
        f'{Style.BRIGHT}{Fore.WHITE}[{Fore.RED}X{Fore.WHITE}]{Fore.RESET} Quit\n'
    )
    choice = input(gay)


    if choice in ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21"]:
        edit(modules[int(choice) -1])

    elif choice == "X" or choice == "x":
        time.sleep(1)
        exit()

    else:
        print("Invalid Choice!")
        time.sleep(1)
        main()


if __name__ == "__main__":
    os.system("cls")
    main()