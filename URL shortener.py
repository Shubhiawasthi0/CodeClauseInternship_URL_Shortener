import pyshorteners


url = input("\nEnter the url of your choice : ")

def shortenurl(url):
    s = pyshorteners.Shortener()
    print("\nshort url : ",s.tinyurl.short(url),"\n")

shortenurl(url)