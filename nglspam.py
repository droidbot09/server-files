import json
import random
import time
import httpx
import sys
import os
import threading
import banner
from concurrent.futures import ThreadPoolExecutor
from msg import randomQuestions
from colorama import Fore, Style, init

# Initialize colorama
init()

sent, errored = 0, 0

description = f"""
{Fore.MAGENTA + Style.BRIGHT}🚀 NGL Message Sender 🚀
{Style.RESET_ALL}------------------
{Fore.RESET + Style.BRIGHT}This script is designed to automate the process of sending messages to a user's NGL link.
It supports sending messages concurrently using multiple threads and can be configured
to use proxies and random messages.

Created by: {Fore.CYAN + Style.BRIGHT}👨‍💻 Hacking0912
GitHub Repository: {Fore.RESET + Style.BRIGHT}🔗 https://github.com/Hacking0912/ngl-msd
{Fore.BLUE + Style.BRIGHT}Please star the repository if you find this script useful.

{Fore.YELLOW + Style.BRIGHT}⚠️ DISCLAIMER: This script is for educational purposes only. Do not use it for spamming or any form of harassment. ⚠️{Style.RESET_ALL}
"""

class Console:
    lock = threading.Lock()

    @staticmethod
    def get_time() -> str:
        return time.strftime("%H:%M:%S", time.gmtime())

    @staticmethod
    def logger(sent: int, errored: int, message="") -> None:
        with Console.lock:
            sys.stdout.write(
                f'\r{Style.BRIGHT + Fore.GREEN}Sent {Style.BRIGHT + Fore.YELLOW}{sent}{Style.BRIGHT + Fore.GREEN} messages, {Style.BRIGHT + Fore.RED}Errored {Style.BRIGHT + Fore.YELLOW}{errored}{Style.BRIGHT + Fore.GREEN} messages{Style.RESET_ALL} {message}')
            sys.stdout.flush()

    @staticmethod
    def clear() -> None:
        os.system("cls" if os.name == "nt" else "clear")

def main(username, message, deviceid, proxy, proxystatus):
    global errored
    global sent

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0",
    }

    if proxystatus:
        client = httpx.Client(headers=headers, proxies=proxy)
    else:
        client = httpx.Client(headers=headers)

    try:
        postresp = client.post(
            f"https://ngl.link/api/submit",
            data={
                "username": username,
                "question": message,
                "deviceId": deviceid,
            },
        )
        if postresp.status_code == 200:
            sent += 1
            Console.logger(sent, errored)

        elif postresp.status_code == 404:
            Console.logger(sent, errored, f"User {username} does not exist")
            exit()
        elif postresp.status_code == 429:
            Console.logger(sent, errored, f"User {username} is rate limited")
        else:
            Console.logger(sent, errored, f"{postresp.status_code}")

    except Exception as e:
        errored += 1
        Console.logger(sent, errored, f"{e}")

def messages():
    return random.choice(randomQuestions)

def proxy():
    return "http://" + random.choice(list(open("proxy.txt")))

def deviceid():
    return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyz-") for _ in range(36))

def handler():
    Console.clear()
    print(banner.banner)
    print(description)
    username = str(input(f"{Fore.CYAN + Style.BRIGHT}Enter username (Along with numbers in their NGL link): {Style.RESET_ALL}" + Style.BRIGHT))
    threadcount = int(input(f"{Fore.CYAN + Style.BRIGHT}Enter thread count (1-100): {Style.RESET_ALL}" + Style.BRIGHT))
    message = str(input(f"{Fore.CYAN + Style.BRIGHT}Enter message: {Style.RESET_ALL}" + Style.BRIGHT))

    start_time = time.time()  # Record the start time
    
    with open("config.json") as config_file:
        config_data = json.load(config_file)
        proxystatus = config_data.get("proxy", False)
        messagestatus = config_data.get("random_messages", False)
        delay = config_data.get("delay", 0)
        print(f'\n{Fore.MAGENTA + Style.BRIGHT}🚀 Attacking Started 🚀 {Style.RESET_ALL}')
        print('------------------\n')

    with ThreadPoolExecutor(max_workers=threadcount) as executor:
        for _ in range(threadcount):
            if messagestatus:
                executor.submit(
                    main, username, messages(), deviceid(), proxy(), proxystatus)
            else:
                executor.submit(main, username, message, deviceid(), proxy(), proxystatus)
            time.sleep(delay)

    elapsed_time = time.time() - start_time  # Calculate the elapsed time
    Console.logger(sent, errored)
    print(f'\n\n{Fore.MAGENTA + Style.BRIGHT}🎉 Attack Completed in {elapsed_time:.2f} seconds 🎉 {Style.RESET_ALL}\n')

if __name__ == "__main__":
    handler()


