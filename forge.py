#1/Bienvenue sur le Forge Tools, je vous pris bien d'agréer cette outil malgrer que ce soit le début merci.Pour quelconque question je vous invite a aller sur ce server :https://discord.gg/e75xUHCU ou me DM net.web737
#2/je tien a préciser que je suis encore jeune développeur et des erreurs peuvent survenir lorsque des prochaines mises a jours venant de cette outil.Apprecier bien !

import os
from os import system

import requests
from pystyle import Colors, Colorate, Center
import sqlite3
from colorama import Fore, colorama_text, Style, init
import colorama
import subprocess
import webbrowser
import time
from program.info import get_info 
from program.ipinfo import get_ip_info

import base64

init(autoreset=True)

ACTUAL_VERSION = '1.5'
AUTHOR = '$"RH8™ '

class color:

    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT

class Color:

    RED = Fore.RED + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT

try: username_pc = os.getlogin()
except: username_pc = "username"

banner = f"""                                        
                                              _______   ______     _______    _______    _______  
                                             /"     "| /    " \   /"      \  /" _   "|  /"     "| 
                                            (: ______)// ____  \ |:        |(: ( \___) (: ______) 
                                             \/    | /  /    ) :)|_____/   ) \/ \       \/    |   
                                             // ___)(: (____/ //  //      /  //  \ ___  // ___)_  
                                            (:  (    \        /  |:  __   \ (:   _(  _|(:      "| 
                                             \__/     \"_____/   |__|  \___) \_______)  \_______) 
                                > [TM] Made by {AUTHOR}                 
                                > [?] version: {ACTUAL_VERSION}           
                                > [!] Connecter en tant que Administrateur           
                                       ╔═══════════════════════════════════════════════════════════╗
                        ┌─────────┐    ║                        Dev by RH8                         ║    ┌───────┐ 
                        │ DI$CORD │    ║                                                           ║    │ O$INT │
                        └─────────┘    ║                                                           ║    └───────┘
                  ╔════════════════════╩═════════════════════╗               ╔═════════════════════╩═════════════════════╗
                  ║  [1] /> Tools info                       ║               ║  [10] /> Email searcher                   ║
                     [2] /> Discord server info [INDISPONNIBLE]                 [11] /> IP info
                     [3] /> Discord nitro generator                             [12] /> IP info (SNUSBASE) [SOON]
                     [4] /> DDoS [WEBSITE]                                      [13] /> Username searcher 
                     [5] /> Id lookup                                           [14] /> Master Searcher [PAID] 
                     [6] /> WebhookSpammer                                      [15] /> DataDive [NEW]
                     [7] /> SOON
                     [8] /> SOON
                     [9] /> SOON

                                             
                  ║                                         ║                ║                                          ║
                  ╚═══                                   ═══╝                ╚═══                                    ═══╝
                        """

def main_screen():
    print(Colorate.Horizontal(Colors.green_to_cyan, banner))
    choice = int(input(Fore.GREEN+ 'Choose a option:/>' ))
    execute_script(choice)

def execute_script(choice):  
      
    if choice == 1:
        infotool = get_info()
        print(Fore.BLUE + infotool)
        input(Fore.GREEN +'Appuyez sur une touche pour continuer...')
        main_screen()
    elif choice == 768:
        os.system('python ./program/server_info.py') 
        main_screen()
    elif choice == 3:
        os.system('python ./program/nitro_gen.py')
        main_screen()
    elif choice == 4:
        webbrowser.open_new_tab('https://www.stressthem.se')
        main_screen()
    elif choice == 5:
        os.system('python ./program/id_lookup.py')        
    elif choice == 6:
        os.system('python ./program/forgespammer.py')
    elif choice == 11:
        domain_ip = input("Entrer une adresse IP ou un nom de domaine: ")
        get_ip_info(domain_ip)
    elif choice == 13:
        os.system('python ./program/username_search.py')
    elif choice == 15:
        os.system('python ./program/DataDive.py')

    execute_script(choice)

def get_location(ip):
    url = f'http://ip-api.com/json/{ip}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"{Colors.cyan}[+] Location for IP {ip}: {data['city']}, {data['region']}, {data['country']}")
    else:
        print(f"{Color.RED}[!] Error: {response.text}{Color.ENDC}")


if __name__ == "__main__":
    main_screen()