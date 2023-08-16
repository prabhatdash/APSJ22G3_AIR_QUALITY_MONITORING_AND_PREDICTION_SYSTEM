import smtplib
import random
def auth(user_id):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('group3@apsjorhat.org','apsj#12345678')
    otp=random.randint(111111,999999)
    message=str(otp)
    s.sendmail('group3@apsjorhat.org',user_id,message)
    s.quit()
    print('Enter the OTP:')
    val=int(input())
    if val==otp:
        print("Login Successful !!!")
    else:
        print("Incorrect OTP")