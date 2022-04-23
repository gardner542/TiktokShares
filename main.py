import ssl, os, requests, time
from threading import active_count, Thread
from pystyle import Colorate, Colors, Write
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar
from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain
import colorama, replforks


class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
r = requests.Session()
ThreadCount = 0
TotalSendedShare = 0
TotalFailedReq = 0
DebugMode = False

r.cookies.set_policy(BlockCookies())


def Clear():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
    else:
        pass


def Title(Content):
    global DebugMode
    if os.name in ('posix', 'ce', 'dos'):
        pass
    elif os.name == 'nt':
        os.system(f"title {Content}")
        return False
    else:
        pass


def ReadFile(filename, method):
    with open(filename, method, encoding='utf8') as f:
        content = [line.strip('\n') for line in f]
        return content


def SendView(item_id):
    global TotalSendedShare, TotalFailedReq, DebugMode
    platform = choice(Platforms)
    osVersion = randint(1, 12)
    DeviceType = choice(DeviceTypes)
    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "user-agent": choice(UserAgent)
    }
    appName = choice(["tiktok_web", "musically_go"])
    Device_ID = randint(1000000000000000000, 9999999999999999999)
    apiDomain = choice(ApiDomain)
    channelLol = choice(Channel)
    URI = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
    Data = f"item_id={item_id}&share_delta=1"

    try:
        req = r.post(URI, headers=headers, data=Data, stream=True, verify=False)
        try:
            if (req.json()["status_code"] == 0):
                impr_id = req.json()["log_pb"]["impr_id"]
                TotalSendedShare += 1
                if DebugMode == True:
                    print(Colorate.Horizontal(Colors.blue_to_red, f"Sent Share: {TotalSendedShare}|"))
                else:
                    print(Colorate.Horizontal(Colors.blue_to_red, f"Sent Share: {TotalSendedShare}| "))
            else:
                pass
        except:
            TotalFailedReq += 1
    except:
        pass


def ClearURI(link):
    if ("vm.tiktok.com" in itemID or "vt.tiktok.com" in itemID):
        return \
        r.head(itemID, stream=True, verify=False, allow_redirects=True, timeout=5).url.split("/")[5].split("?", 1)[0]
    else:
        return itemID.split("/")[5].split("?", 1)[0]
      

if (__name__ == "__main__"):
    Clear()
    print("""



                            
   ██████╗░███████╗██████╗░██╗░░░░░██╗░░░██╗██████╗░
   ██╔══██╗██╔════╝██╔══██╗██║░░░░░██║░░░██║██╔══██╗
   ██║░░██║█████╗░░██║░░██║██║░░░░░██║░░░██║██████╔╝
   ██║░░██║██╔══╝░░██║░░██║██║░░░░░██║░░░██║██╔══██╗
   ██████╔╝███████╗██████╔╝███████╗╚██████╔╝██║░░██║
   ╚═════╝░╚══════╝╚═════╝░╚══════╝░╚═════╝░╚═╝░░╚═╝
                https://discord.gg/8EQd5d6M


    """)

    itemID = Write.Input(" « Video Link »  ", Colors.blue, interval=0.0001)
    amount = Write.Input(" « Amount »  ", Colors.yellow, interval=0.0001)
    NThread = 500

    itemID = ClearURI(itemID)

    if (int(amount) == 0):
        while True:
            Run = True
            while Run:
                if (active_count() <= int(NThread)):
                    Thread(target=(SendView), args=(itemID,)).start()
    else:
        for _ in range(int(amount)):
            if (active_count() <= int(NThread)):
                Thread(target=(SendView), args=(itemID,)).start()