from socket import gethostbyname

banner='''

             _                       _       ____  _       
          __| | ___  _ __ ___   __ _(_)_ __ |___ \(_)_ __  
         / _` |/ _ \| '_ ` _ \ / _` | | '_ \  __) | | '_ \ 
        | (_| | (_) | | | | | | (_| | | | | |/ __/| | |_) |
         \__,_|\___/|_| |_| |_|\__,_|_|_| |_|_____|_| .__/ 
                                                  |_|    

'''

def main(banner):
    print(banner)
    while True:
        try:
            domain=input("[+] Domain name > ")
            if len(domain)<=0:
                break;
            else:
                print(gethostbyname(domain))
        except:
            print("[! Error...!]")

if __name__=='__main__':
    main(banner)
