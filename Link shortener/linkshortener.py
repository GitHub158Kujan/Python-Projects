import pyshorteners
link=input("Enter a link : ")
shortner =pyshorteners.Shortener()
x=shortner.tinyurl.short(link)
print("Short link : ",x)