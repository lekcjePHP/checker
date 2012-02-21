import requests,sys,time,smtplib



def wyslij_mail(toaddrs,msg, username, password):
        sourceAddress = username +"@gmail.com"
        # The actual mail send  
        server = smtplib.SMTP('smtp.gmail.com:587')  
        server.starttls()  
        server.login(username,password)  
        server.sendmail(sourceAddress, toaddrs, msg)  
        server.quit()

def watcher(pageAddress, toaddrs,msg, username, password, szukanaFraza):


        while True:
               strona = requests.get(pageAddress)
               tekstStrony = strona.text

               time.sleep(10)
               if szukanaFraza in tekstStrony:
                     wyslij_mail(toaddrs, msg, username, password )
                     return 1
