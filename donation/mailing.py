from django.core.mail import EmailMessage
# to send mail 
def send_mail_A(send_to,attach_file):
    #prepare the emal message adding subject and body of email 
	msg = EmailMessage("Subject","Body of Email","Kalamenrichinglives@gmail.com",send_to)
	msg.attach_file(attach_file)
	msg.send()