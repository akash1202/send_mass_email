import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
# https://myaccount.google.com/intro/security
#fromaddr = "YOUR EMAIL"
#toaddr = "EMAIL ADDRESS YOU SEND TO"

def send_mass_email(frm,rcv,sub,txt,server):
	rcvlist=rcv.split(" ")
	l1=0
	msg = MIMEMultipart()
	msg['From'] = frm
	msg['Subject'] = sub    #"SUBJECT OF THE EMAIL"
	body = txt 		#"TEXT YOU WANT TO SEND"
	ch=input("Would you like to attach a file(y/n):")
	if(ch=='y' or ch=='Y'):
		filename = raw_input('Enter filepath:')
		attachment = open(filename, "rb")
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		msg.attach(part)
	
	msg.attach(MIMEText(body, 'plain'))
	
	while(l1<len(rcvlist)):	
		msg['To'] = rcvlist[l1]
		text = msg.as_string()
		server.sendmail(frm,rcvlist[l1],text)
		print "sended mail to:",rcvlist[l1]
		l1=l1+1
print "--**--**-- Please Enter Below detail to send mass Email --**--**--\n\n"
fromaddr=raw_input('Enter your Email Address:')
password=raw_input('your Password:')
toaddr = raw_input('Receiver Address(separated by space):')
subject=raw_input('Enter Subject:')
text=raw_input('Enter Body Text:')
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
send_mass_email(fromaddr,toaddr,subject,text,server)
server.quit()
