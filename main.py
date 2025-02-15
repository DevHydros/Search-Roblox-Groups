from colorama import init, Fore
import requests
import time
import random

init()

DELAY_BETWEEN_REQUESTS = 10 

OUTPUT_FILE = "ownerless_groups.txt"

def get_group_info(group_id):
    url = f"https://groups.roblox.com/v1/groups/{group_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def is_group_ownerless(group_info):
    return group_info.get("owner") is None

def is_group_joinable(group_id):
    url = f"https://groups.roblox.com/v1/groups/{group_id}"
    response = requests.get(url)
    if response.status_code == 200:
        group_info = response.json()
        return group_info.get("publicEntryAllowed", False)
    return False

def get_group_url(group_id):
    return f"https://www.roblox.com/groups/{group_id}"

def save_group_to_file(group_id, group_url):
    with open(OUTPUT_FILE, "a") as file:
        file.write(f"Groups: {group_url}\n")

def find_ownerless_groups():
    while True:
        group_id = random.randint(1, 9999999)        
        group_info = get_group_info(group_id)       
        if group_info:
            if is_group_ownerless(group_info):
                if is_group_joinable(group_id):
                    group_url = get_group_url(group_id)
                    print(Fore.GREEN + f"Groups (not owned)! Link: {group_url} (Open to join)")

                    save_group_to_file(group_id, group_url)
                else:
                    print(Fore.RED + f"Группа {group_id} без владельца, но закрыта для вступления.")
            else:
                print(Fore.RED + f"Groups {group_id} has owned.")
        else:
            print(Fore.RED + f"Groups {group_id} does not exist, error.")
        
        time.sleep(DELAY_BETWEEN_REQUESTS)

find_ownerless_groups()