#!/usr/bin/python
'''
**********************************************************************************
   NOME: morretes.py

   DATA
   11 de Junho de 2015

   ATUALIZACAO
   25 de Outubro de 2016

   DESCRICAO
   Script para monitorar a fila de emails contra possiveis SPAM.

   REQUISITOS
   Endereco de email valida, que sera utilizada para envios dos emails.

   OBSERVACAO
   Detectando alguma conta de email maior que 300 emails presos na queue o sistema enviara
   um email para o suporte[ at ]mdbrasil.com.br com o endereco de email e a quantidade de
   emails na queue dessa mesma conta detectada.

   AUTOR
   Messias Manoel da Silva Junior

***********************************************************************************
'''

### BIBLIOTECAS ###
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## Instancia das listas
line1 = []
line2 = []
resultado = []

os.system( "/usr/sbin/postqueue -p | awk '/^[0-9,A-F]/ {print $7}' | sort | uniq -c | sort -n | grep -v MAILER | grep -v xmlgransmed@mdbrasil.com.br > /tmp/detectSPAM" )

fila = open('/tmp/detectSPAM').readlines()
listaBloq = open('/etc/postfix/sender_checks').readlines()



for y in listaBloq:
    copy = y.rstrip('\n')
    line2.append(copy.split(' ')[0])

for x in fila:
    valor = int(x[0:8])
    if (valor > 50):
        ####### Envio de email #######
        mdbrasil_to = 'detectspam@mdbrasil.com.br'
        mdbrasil_user = 'alerta@mdbrasil.com.br'
        mdbrasil_pwd = 'xxxxx'
        ## ABRE CONEXAO PARA SMTP
        smtpserver = smtplib.SMTP("smtp.mdbrasil.com.br", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        ## FAZ AUTENTICACAO DO USER
        smtpserver.login(mdbrasil_user, mdbrasil_pwd)
        mdbrasil_msg = MIMEMultipart("alternative")
        mdbrasil_msg["Subject"] = "Possivel Ataque de SPAM"
        mdbrasil_msg['From'] = 'alerta@mdbrasil.com.br'
        mdbrasil_msg['To'] = 'detectspam@mdbrasil.com.br'
        mdbrasil_msg.attach(MIMEText(
            "Foi detectado um ataque de SPAM no Servidor Morretes vindo do email: " + x[8:].strip() + " com: " + x[0:8].strip() + " emails na fila. \n Providenciar o Bloqueio do mesmo.", "plain",
            "utf-8"))
        mdbrasil_msg = mdbrasil_msg.as_string().encode('ascii')
        smtpserver.sendmail(mdbrasil_user, mdbrasil_to, mdbrasil_msg)
        smtpserver.close()
        line1.append(x[8:].strip())


resultado = list(set(line1).difference(set(line2)))
        ####### Envio dos enderecos para sender_checks #######
for user in resultado:
    os.system('/bin/echo ' + user + ' REJECT >> /tmp/postfix/sender_checks')
os.system('/usr/sbin/postmap /etc/postfix/sender_checks')
os.system('/etc/init.d/postfix reload')
