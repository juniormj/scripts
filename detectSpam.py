#!/usr/bin/python
'''
**********************************************************************************
<<<<<<< HEAD
   NOME: detectSpam.py
=======
   NOME: morretes.py
>>>>>>> 48e6e4eae430af530e1c3b7f1295f0be529173f0

   DATA
   11 de Junho de 2015

   ATUALIZACAO
<<<<<<< HEAD
   10 de Marco de 2017
=======
   25 de Outubro de 2016
>>>>>>> 48e6e4eae430af530e1c3b7f1295f0be529173f0

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
<<<<<<< HEAD
import commands
=======
>>>>>>> 48e6e4eae430af530e1c3b7f1295f0be529173f0
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

## Instancia das listas
line1 = []
line2 = []
resultado = []

<<<<<<< HEAD
os.system( "/usr/sbin/postqueue -p | awk '/^[0-9,A-F]/ {print $7}' | sort | uniq -c | sort -n | grep -v MAILER | grep -v excecaoCliente@dominio.com.br > /tmp/detectSPAM" )
=======
os.system( "/usr/sbin/postqueue -p | awk '/^[0-9,A-F]/ {print $7}' | sort | uniq -c | sort -n | grep -v MAILER | grep -v xmlgransmed@mdbrasil.com.br > /tmp/detectSPAM" )
>>>>>>> 48e6e4eae430af530e1c3b7f1295f0be529173f0

fila = open('/tmp/detectSPAM').readlines()
listaBloq = open('/etc/postfix/sender_checks').readlines()



for y in listaBloq:
    copy = y.rstrip('\n')
    line2.append(copy.split(' ')[0])

for x in fila:
    valor = int(x[0:8])
<<<<<<< HEAD
    if (valor > 150):
	os.system( '/usr/sbin/postqueue -p | grep '+x[8:].strip()+' > /tmp/filaMsgIndividual')
	filaMsgIndividual = open('/tmp/filaMsgIndividual').readlines()
	pegaUltimaFila = filaMsgIndividual[len(filaMsgIndividual) -1]
	cmd = commands.getoutput("echo " +pegaUltimaFila.strip()+ " | awk '{print $1}'")
	os.system('/usr/sbin/postcat -qv '+cmd+ '| grep "regular_text:" > /tmp/lerSpam')
	lerArqSpam = open('/tmp/lerSpam')
	conteudoSpam = lerArqSpam.read()
        ####### Envio de email #######
        email_to = 'detectspam@dominio.com.br'
        email_user = 'alerta@dominio.com.br'
        email_pwd = 'xxxxxxxx'
        ## ABRE CONEXAO PARA SMTP
        smtpserver = smtplib.SMTP("smtp.dominio.com.br", 587)
=======
    if (valor > 50):
        ####### Envio de email #######
        mdbrasil_to = 'detectspam@mdbrasil.com.br'
        mdbrasil_user = 'alerta@mdbrasil.com.br'
        mdbrasil_pwd = 'xxxxx'
        ## ABRE CONEXAO PARA SMTP
        smtpserver = smtplib.SMTP("smtp.mdbrasil.com.br", 587)
>>>>>>> 48e6e4eae430af530e1c3b7f1295f0be529173f0
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo
        ## FAZ AUTENTICACAO DO USER
<<<<<<< HEAD
        smtpserver.login(email_user, email_pwd)
        email_msg = MIMEMultipart("alternative")
        email_msg["Subject"] = "Possivel Ataque de SPAM no servidor de Email"
        email_msg['From'] = 'alerta@dominio.com.br'
        email_msg['To'] = 'detectspam@dominio.com.br'
        email_msg.attach(MIMEText(
            "Foi detectado um ataque de SPAM no Servidor de email vindo do Usuario: " + x[8:].strip() + " com: " + x[0:8].strip() + " emails na fila. \n Providenciar o Bloqueio do mesmo.\n\n"+
		"<tt>--------------------------------- Fonte do Email --------------------------------- \n\n\n"+
                conteudoSpam + " </tt> \n\n\n\nGerado pelo script detectSpam.py", "plain", "utf-8"))
        email_msg = email_msg.as_string().encode('ascii')
        smtpserver.sendmail(email_user, email_to, email_msg)
=======
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
>>>>>>> 48e6e4eae430af530e1c3b7f1295f0be529173f0
        smtpserver.close()
        line1.append(x[8:].strip())


resultado = list(set(line1).difference(set(line2)))
        ####### Envio dos enderecos para sender_checks #######
for user in resultado:
<<<<<<< HEAD
    os.system('/bin/echo ' + user + ' REJECT >> /etc/postfix/sender_checks')
=======
    os.system('/bin/echo ' + user + ' REJECT >> /tmp/postfix/sender_checks')
>>>>>>> 48e6e4eae430af530e1c3b7f1295f0be529173f0
os.system('/usr/sbin/postmap /etc/postfix/sender_checks')
os.system('/etc/init.d/postfix reload')
