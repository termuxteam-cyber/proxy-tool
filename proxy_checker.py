import requests
import os
from concurrent.futures import ThreadPoolExecutor

GREEN="\033[92m"
RED="\033[91m"
CYAN="\033[96m"
YELLOW="\033[93m"
RESET="\033[0m"

live=0
dead=0

def banner():
    os.system("clear")
    print(CYAN+"""
████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝


████████╗███████╗ █████╗ ███╗   ███╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
   ██║   █████╗  ███████║██╔████╔██║
   ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝

          TERMUX TEAM PROXY CHECKER TOOL V1
"""+RESET)

def scrape():

    banner()

    print(YELLOW+"Scraping proxies...\n"+RESET)

    urls=[
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
    "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
    "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
    ]

    proxies=set()

    for url in urls:
        try:
            r=requests.get(url,timeout=10)
            for p in r.text.splitlines():
                proxies.add(p.strip())
        except:
            pass

    with open("proxies.txt","w") as f:
        for p in proxies:
            f.write(p+"\n")

    print(GREEN+f"Scraped {len(proxies)} proxies → saved to proxies.txt"+RESET)
    input("\nPress Enter...")

def check(proxy):

    global live,dead

    try:
        requests.get(
        "http://httpbin.org/ip",
        proxies={"http":"http://"+proxy,"https":"http://"+proxy},
        timeout=5)

        print(GREEN+"[LIVE] "+proxy+RESET)

        with open("live.txt","a") as f:
            f.write(proxy+"\n")

        live+=1

    except:
        print(RED+"[DEAD] "+proxy+RESET)
        dead+=1


def checker():

    banner()

    file=input("Proxy file: ")
    threads=int(input("Threads: "))

    if not os.path.exists(file):
        print("File not found")
        input()
        return

    with open(file) as f:
        proxies=f.read().splitlines()

    print(f"\nTotal proxies: {len(proxies)}\n")

    try:

        with ThreadPoolExecutor(max_workers=threads) as exe:
            exe.map(check,proxies)

    except KeyboardInterrupt:
        print("\nStopped")

    print("\n====== RESULT ======")
    print(GREEN+"Live :",live,RESET)
    print(RED+"Dead :",dead,RESET)
    print(CYAN+"Saved Live Proxies → live.txt"+RESET)
    
    input("\nPress Enter...")


while True:

    banner()

    print("[1] Scrape Proxies")
    print("[2] Check Proxies")
    print("[0] Exit\n")

    opt=input("Select option: ")

    if opt=="1":
        scrape()

    elif opt=="2":
        checker()

    elif opt=="0":
        break
