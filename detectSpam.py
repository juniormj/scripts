#!/usr/bin/python
'''
**********************************************************************************
   NOME: morretes.py

   DATA
   11 de Junho de 2015

   DESCRICAO
   Script para monitorar a fila de emails contra possiveis SPAM.

   REQUISITOS
   Endereco de email valida, que sera utilizada para envios dos emails.

   OBSERVACAO
   Detectando alguma conta de email maior que 300 emails presos na queue o sistema enviara
   um email para o suporte[ at ]dominio.com.br com o endereco de email e a quantidade de
   emails na queue dessa mesma conta detectada.

   AUTOR
   Messias Manoel da Silva Junior

***********************************************************************************
'''

### BIBLIOTECAS
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

####### CRIA UM ARQUIVO E PEGA A CONTA COM MAIOR DISPARO DE EMAIL
os.system( "/usr/sbin/postqueue -p | awk '/^[0-9,A-F]/ {print $7}' | sort | uniq -c | sort -n | grep -v MAILER | tail -1 > /tmp/detectSPAM" )
os.system( "sed 's/[^0-9]//g' /tmp/detectSPAM > /tmp/qnt" )
os.system( "sed 's/[^a-zA-Z@.]//g' /tmp/detectSPAM > /tmp/user" )

### ABRE O ARQUIVO PARA LEITURA
qnt = open('/tmp/qnt').read()
user = open('/tmp/user').read()

### CONVERTE qnt DE STRING PARA INTEGER
print qnt
qntd = int(qnt)

### SE O NUMERO DE ENVIO FOR MAIOR QUE 300 E DIFERENTE DE MAILER-DAEMON ENVIE UM EMAIL
if(qntd > 300 ):

    dominio_to = 'detectspam@dominio.com.br'
    dominio_user = 'alerta@dominio.com.br'
    dominio_pwd = 'senha'
## ABRE CONEXAO PARA SMTP
    smtpserver = smtplib.SMTP("smtp.dominio.com.br",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
## FAZ AUTENTICACAO DO USER
    smtpserver.login(dominio_user, dominio_pwd)
    dominio_msg = MIMEMultipart("alternative")
    dominio_msg["Subject"] = "Possivel Ataque de SPAM"
    dominio_msg['From'] = 'alerta@dominio.com.br'
    dominio_msg['To'] = 'detectspam@dominio.com.br'
    dominio_msg.attach( MIMEText("Foi detectado um ataque de SPAM no Servidor Morretes vindo do: \n email: " + user.rstrip('\n') + " com: " + qnt.rstrip('\n') + " emails na fila. \n Providenciar o Bloqueio do mesmo.", "plain", "utf-8" ) )
    dominio_msg = dominio_msg.as_string().encode('ascii')

    smtpserver.sendmail(dominio_user, dominio_to, dominio_msg)
    smtpserver.close() 
