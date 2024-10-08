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
import sys 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# read the .env
dotenv.load_dotenv()

if dotenv.dotenv_values() == None:
    raise Exception("Cannot read the load env")    

PERCENTAGE_HD = int(os.getenv('PERCENTAGE_HD'))
HOST_EMAIL = os.getenv('HOST_EMAIL')
PORT_EMAIL = os.getenv('PORT_EMAIL')
USER_EMAIL = os.getenv('USER_EMAIL')
PSWD_EMAIL = os.getenv('PSWD_EMAIL')
IP_ADDRESS = os.getenv('IP_ADDRESS')
TODAY = datetime.today().strftime('%Y%m%d')

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

# Configurações do e-mail
to_email = ['flima@jpti.com.br']  # Lista de destinatários principais
cc = ['jmira@jpti.com.br']  # Lista de usuários em cópia
subject = 'HD USE'
mensagem = 'Esta é a mensagem do email.'

# Criação do objeto MIMEMultipart
msg = MIMEMultipart()
msg['From'] = USER_EMAIL
msg['To'] = ', '.join(to_email)  # Concatena a lista de destinatários principais
msg['Cc'] = ', '.join(cc)  # Concatena a lista de usuários em cópia
msg['Subject'] = subject


# Lista de todos os destinatários (para enviar corretamente o e-mail)
all_emails = to_email + cc

if percentage_free >= PERCENTAGE_HD:
    try:
        if os.path.exists('log/' + TODAY):
            sys.exit()
        # Conecta ao servidor SMTP do Gmail usando SSL
        servidor = smtplib.SMTP_SSL(HOST_EMAIL, PORT_EMAIL)  # Usa SSL na porta 465
        
        # Autentica no servidor SMTP
        servidor.login(USER_EMAIL, PSWD_EMAIL)
        
        # Corpo da mensagem em HTML
        mensagem = f"""
        <html>
          <head></head>
          <body>
            <h1 style="color: #5e9ca0;">Alerta de Capacidade do HD</h1>
            <p>Olá,</p>
            <p>Este é um alerta sobre a capacidade do HD do servidor {IP_ADDRESS}</p>
            <p>HD em uso: {used_hd}GB</p>
            <p>HD em disponível: {free_hd}GB</p>
            <p>HD total: {total_hd}GB</p>
            <p>Porcentagem do uso: {percentage_free}%</p>
            <p>Alerta definido em: {PERCENTAGE_HD}%</p>
            <p><strong>Por favor, tome as ações necessárias.</strong></p>
            <p>Atenciosamente,<br>Equipe de Monitoramento</p>
          </body>
        </html>
        """

        msg.attach(MIMEText(mensagem, 'html'))

        # Envia o email
        servidor.sendmail(USER_EMAIL, all_emails, msg=msg.as_string())
        
        with open('log/'+TODAY,'w') as file:
            file.write(TODAY)
            file.close()

    except Exception as e:
        print(f"Erro ao enviar o email: {e}")
    finally:
        servidor.quit()  