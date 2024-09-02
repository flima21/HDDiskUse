# try:
#     # Conecta ao servidor SMTP do Gmail usando SSL
#     servidor = smtplib.SMTP_SSL("mxpro3.anuv.com.br", 465)  # Usa SSL na porta 465
    
#     # Autentica no servidor SMTP
#     servidor.login(email_remetente, senha)
    
#     # Envia o email
#     servidor.sendmail(email_remetente, email_destinatario, mensagem.as_string())
#     print("Email enviado com sucesso!")
    
# except Exception as e:
#     print(f"Erro ao enviar o email: {e}")
# finally:
#     servidor.quit()  

import psutil
import smtplib
import dotenv
import os
import socket

# read the .env
dotenv.load_dotenv()

if dotenv.dotenv_values() == None:
    raise Exception("Cannot read the load env")    

PERCENTAGE_HD = int(os.getenv('PERCENTAGE_HD'))
HOST_EMAIL = os.getenv('HOST_EMAIL')
PORT_EMAIL = os.getenv('PORT_EMAIL')
USER_EMAIL = os.getenv('USER_EMAIL')
PSWD_EMAIL = os.getenv('PSWD_EMAIL')

HOSTNAME = socket.gethostname()
IP_ADDRESS = socket.gethostbyname(HOSTNAME)

print(f"IP ADDRESS {IP_ADDRESS}")

hdd = psutil.disk_usage('/')

# HDD Total
total_hd = (hdd.total // (2**30))
used_hd = (hdd.used // (2**30))
free_hd = (hdd.free // (2**30))

if total_hd == 0:
    raise Exception("Impossible divided by zero (0)")

percentage_free = (round((used_hd * 100) / (total_hd),0))

print("*" * 20)

print(f'USED HD: {used_hd}')
print(f'FREE HD: {free_hd}')
print(f'TOTAL HD: {total_hd}')

print("*" * 20)

if percentage_free >= PERCENTAGE_HD:
    try:
        # Conecta ao servidor SMTP do Gmail usando SSL
        servidor = smtplib.SMTP_SSL(HOST_EMAIL, PORT_EMAIL)  # Usa SSL na porta 465
        
        # Autentica no servidor SMTP
        servidor.login(USER_EMAIL, PSWD_EMAIL)
        
        # mensagem 
        mensagem = f"The HD use is define to alert with capacity free the {PERCENTAGE_HD}, but the use currently with {percentage_free}. Pay attention"

        # Envia o email
        servidor.sendmail(USER_EMAIL, 'flima@jpti.com.br', msg=mensagem)
    except Exception as e:
        print(f"Erro ao enviar o email: {e}")
    finally:
        servidor.quit()  