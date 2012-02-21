import requests,sys,time,smtplib



def wyslij_mail(toaddrs,msg, username, password):
        sourceAddress = username +"@gmail.com"
        # The actual mail send  
        server = smtplib.SMTP('smtp.gmail.com:587')  
        server.starttls()  
        server.login(username,password)  
        server.sendmail(sourceAddress, toaddrs, msg)  
        server.quit()

def watcher(pageAddress, toaddrs,msg, username, password):
        strona = requests.get(pageAddress)
        startSize = len(strona.text)
        while True:
               strona = requests.get(pageAddress)
               actualSize = len(stronaText)
               time.sleep(10)
               if actualSize != startSize:
                     wyslij_mail(toaddrs, msg, username, password )
                     return 1
