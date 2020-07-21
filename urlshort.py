import pyfiglet
import time
import pyshorteners
import terminal_banner
from termcolor import colored
def banner():
        ascii_banner = pyfiglet.figlet_format("\tURL MANAGER")
        print(colored((ascii_banner),'red','on_blue'))
        text="CODED BY:- MANJUNATHAN.C\nYOUTUBE LINK:-https://bit.ly/2CPKEvh"
        my_banner = terminal_banner.Banner(text)
        print(my_banner)
banner()
def short():
        print("\n\n",colored('\tENTER YOUR CHOICE','blue','on_yellow'),"\n\n")
        choice=input("1.TINYURL\n2.BIT.LY\n3.CHILP.IT\n4.CLCK.RU\n5.CUTT.LY\n6.GIT.IO(ONLY SHORTEN GITHUB URLS)\n7.DA.GD\n8.NULLPOINTER\n9.OS.DB\n10.OW.LY\n11.PO.ST\n12.ADFLY\n13.QPS.RU\n14.SHORT.CM\n15.TINY.CC\n16.IS.GD\n\n")
        if(choice=='1'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()
                print(p.tinyurl.short(url))
        elif(choice=='2'):
                api=input("Paste your API token for Bit.ly\n")
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener(api_key=(api))
                print(p.bitly.short(url))
        elif(choice=='3'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()
                print(p.chilpit.short(url))
        elif(choice=='4'):   
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()
                print(p.clckru.short(url))
        elif(choice=='5'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()                
                print(p.cuttly.short(url))
        elif(choice=='6'):
                print("SHORT ONLY GITHUB URL\n")
                code=input("ENTER THE CODE YOU WANT TO PRINT\n")
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener(code=(code))
                print(p.gitio.short(url))
        elif(choice=='7'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()
                print(p.dagd.short(url))
        elif(choice=='8'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()                
                print(p.nullpointer.short(url))
        elif(choice=='9'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()
                print(p.osdb.short(url))
        elif(choice=='10'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()
                print(p.owly.short(url))
        elif(choice=='11'):
                api=input("ENTER THE API KEY FOR POST\n")
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener(api_key=(api))
                print(p.post.short(url))
        elif(choice=='12'):
                api=input("ENTER THE API KEY FOR ADFLY\n")
                uid=input("ENTER THE USER_ID FOR ADFLY\n")
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p= pyshorteners.Shortener(api_key=(api), user_id=(uid),domain='test.us', group_id=12, type='int')
                print(p.adfly.short(url))
        elif(choice=='13'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()                
                print(p.qpsru.short(url))
        elif(choice=='14'):
                api=input("ENTER THE API KEY FOR SHORTCM\n")
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener(api_key=(api))
                print(p.shortcm.short(url))
        elif(choice=='15'):
                api=input("ENTER THE API KEY FOR TINYCC\n")
                uid=input("ENTER THE USER_NAME FOR TINYCC\n")
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p= pyshorteners.Shortener(api_key=(api), login=(uid))
                print(p.tinycc.short(url))
        elif(choice=='16'):
                url=input("ENTER THE URL TO SHORT\n")
                print("THE SHORTENED URL is\n")
                p=pyshorteners.Shortener()
                print(p.isgd.short(url))
        else:   
                print("WRONG CHOICE\nENTER BETWEEN 1 TO 16 ONLY")
                exit()
                
def expand():
        print("\n\n",colored('\tENTER YOUR CHOICE','red','on_yellow'),"\n\n")
        choice=input("1.TINYURL\n2.BIT.LY\n3.CHILP.IT\n4.CLCK.RU\n5.CUTT.LY\n6.GIT.IO(ONLY SHORTEN GITHUB URLS)\n7.DA.GD\n8.NULLPOINTER\n9.OS.DB\n10.OW.LY\n11.PO.ST\n12.ADFLY\n13.QPS.RU\n14.SHORT.CM\n15.TINY.CC\n16.IS.GD\n\n")
        if(choice=='1'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.tinyurl.expand(url))
        elif(choice=='2'):
                api=input("Paste your API token for Bit.ly\n")
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener(api_key=(api))
                print(p.bitly.expand(url))
        elif(choice=='3'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.chilpit.expand(url))
        elif(choice=='4'):   
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.clckru.expand(url))
        elif(choice=='5'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.cuttly.expand(url))
        elif(choice=='6'):
                print("EXPAND ONLY IN GITHUB URL FORMAT\n")
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                code=input("ENTER THE CODE YOU WANT TO PRINT\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener(code=(code))
                print(p.gitio.expand(url))
        elif(choice=='7'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.dagd.expand(url))
        elif(choice=='8'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.nullpointer.expand(url))
        elif(choice=='9'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.osdb.expand(url))
        elif(choice=='10'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.owly.expand(url))
        elif(choice=='11'):
                api=input("ENTER THE API KEY FOR POST\n")
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener(api_key=(api))
                print(p.post.expand(url))
        elif(choice=='12'):
                api=input("ENTER THE API KEY FOR ADFLY\n")
                uid=input("ENTER THE USER_ID FOR ADFLY\n")
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p= pyshorteners.Shortener(api_key=(api), user_id=(uid),domain='test.us', group_id=12, type='int')
                print(p.adfly.expand(url))
        elif(choice=='13'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.qpsru.expand(url))
        elif(choice=='14'):
                api=input("ENTER THE API KEY FOR SHORTCM\n")
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener(api_key=(api))
                print(p.shortcm.expand(url))
        elif(choice=='15'):
                api=input("ENTER THE API KEY FOR TINYCC\n")
                uid=input("ENTER THE USER_NAME FOR TINYCC\n")
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p= pyshorteners.Shortener(api_key=(api), login=(uid))
                print(p.tinycc.expand(url))
        elif(choice=='16'):
                url=input("ENTER THE SHORTENED URL TO EXPAND\n")
                print("THE EXPANDED URL is\n")
                p=pyshorteners.Shortener()
                print(p.isgd.expand(url))
        else:   
                print("WRONG CHOICE\nENTER BETWEEN 1 TO 16 ONLY")
                exit()
                

def main():
        choice=input("ENTER WHAT ACTION YOU WANT TO PERFORM\n1.URL SHORTENER\n2.URL EXPANDER\n3.READ THE GUIDE BEFORE USE\n\n")
        if(choice=='1'):
                short()
        elif(choice=='2'):
                expand()
        elif(choice=='3'):
                f = open("README.txt", "r")
                print(f.read(),"\n\n\n")
                time.sleep(5)
                banner() 
                main()
        else:
                print("WRONG OPTION CHOOSE 1 OR 2\n")
                exit()
main()
