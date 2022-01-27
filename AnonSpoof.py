import string
import requests
import os
import time
import sys
import readline

def banner():
 print ('''
    _                      ____                     __
   / \   _ __   ___  _ __ / ___| _ __   ___   ___  / _|
  / _ \ | '_ \ / _ \| '_ \\\___ \| '_ \ / _ \ / _ \| |_
 / ___ \| | | | (_) | | | |___) | |_) | (_) | (_) |  _|
/_/   \_\_| |_|\___/|_| |_|____/| .__/ \___/ \___/|_|
                                |_| ----> https://t.me/HackForAll1
''')


def limpiar():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
limpiar()
banner()
print("Enter the number of the victim plus the country code")

phone = input("Enter number: ")

print("Enter a message, it is anonymous")

text = input("Enter Message to send : ")

resp = requests.post('https://textbelt.com/text',{
         'phone' : phone,
         'message' : text ,
         'key' : 'textbelt',
       })

aux1  = str(resp.json()['success'])
text  = 'Only one test text message is allowed per day.'
aux2  = str(resp.json()['error']) if 'error' in resp.json() else ''
if(aux1 == 'False') and (aux2 == text):
    limpiar()
    banner()
    print("\nIngles\t\t\tEspañol")
    print("\n\nOnly 1 sms for day\tSolo puedes 1 mensaje por dia")
    input('\nPress Enter To Exit... ')
if(aux1 == 'False') and (aux2 != '') and (aux2 != text):
    limpiar()
    banner()
    print("\nIngles\t\t\tEspañol\n")
    print("Error Occured\t\tOcurrio un Error")
    print("Failed to send SMS!\tFallo el envio del SMS! ")
    input('\nPress Enter To Exit...')
if(aux1 == 'True'):
    limpiar()
    banner()
    print("\nIngles\t\t\t\t Español\n")
    print("Message Sent Succesfully\t Mensage Enviado Exitoso")
    input('\nPress Enter To Exit...')
