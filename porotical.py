import os
import sys
from colorama import Fore, Style, Back
import requests
import json
import colorama

colorama.init(autoreset=True)


class internal(Exception):
    def __init__(self, message):
        self.message = message


def sendWebhook(content=None, username="PoroticalLib", AvUrl=None, Url=None):
    # URL del webhook
    if Url == None:
        print(f"{Style.BRIGHT, Fore.LIGHTMAGENTA_EX}Porotical: {Style.RESET_ALL, Fore.RESET}You can't leave the webhook URL with no string.")
    else:
        webhook_url = Url

    # Crea el payload del mensaje
    message = {
        "content": content,
        "username": username,
        "avatar_url": AvUrl
    }

    # Envía la solicitud POST al webhook
    response = requests.post(webhook_url, json=message)

    # Verifica el estado de la respuesta
    if response.status_code == 200:
        print(f"{Style.BRIGHT, Fore.LIGHTMAGENTA_EX}Porotical: {Style.RESET_ALL, Fore.RESET}Message sent correctlty!")
    else:
        print(f"{Style.BRIGHT, Fore.LIGHTMAGENTA_EX}Porotical: {Style.RESET_ALL, Fore.RESET}Check your connection? Or Webhook url might be deleted or not found.")

class util:
    def versionCheck(version_req, version_json_link, outdated_mess="Get a new version avaliable in porotical.interactive.co"):
        try:
            r = requests.get(version_json_link)
            status = r.status_code
            if status == 200:
                getJson = r.json()
                if getJson:
                    version = getJson.get("version")
                    if version == version_req:
                        pass
                    else:
                        print(outdated_mess)
                else:
                    raise internal("Sorry but, something is wrong with your json. Please make sure its: {'version': 'your_version_here'}")    
            else:
                raise internal("The website is unavaliable? Please check your conectivity to that server.")    
        except:
            raise internal("The website is unavaliable? Please check your conectivity to that server.")    