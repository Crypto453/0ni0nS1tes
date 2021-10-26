import os
import time
import random
import colorama
from colorama import Fore

def banner():
	os.system("clear")
	os.system("python3 banner")
def list_primary():
	sites = [Fore.YELLOW + "HiddenWiki" + Fore.GREEN + " http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page", Fore.YELLOW + "ProtonMail" + Fore.GREEN + " https://protonirockerxow.onion/", Fore.YELLOW + "Library Genesis" + Fore.GREEN + " http://genotypeinczgrxr.onion/", Fore.YELLOW + "Sci-Hub" + Fore.GREEN + " http://scihub22266oqcxt.onion/", Fore.YELLOW + "The Intercept" + Fore.GREEN + " http://xpxduj55x2j27l2qytu2tcetykyfxbjbafin3x4i3ywddzphkbrd3jyd.onion/", Fore.YELLOW + " ProPublica" + Fore.GREEN + " https://www.propub3r6espa33w.onion/", Fore.YELLOW + "Wasabi Wallet" + Fore.GREEN + " http://wasabiukrxmkdgve5kynjztuovbg43uxcbcxn6y2okcrsg7gb6jdmbad.onion", Fore.YELLOW + "Secure Drop" + Fore.GREEN + " http://secrdrop5wyphb5x.onion/", Fore.YELLOW + "Torch Search Engine" + Fore.GREEN + " http://xmh57jrzrnw6insl.onion/"]
	for sit in sites:
		print(sit)
		time.sleep(0.3)
banner()
list_primary()
