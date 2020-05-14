clear;
echo "
  _   _ _ _                _      ____                          
 | | | (_) |_   _____ _ __| |_   / ___|   _ _ ____   _____  ___ 
 | |_| | | \ \ / / _ \ '__| __| | |  | | | | '__\ \ / / _ \/ __|
 |  _  | | |\ V /  __/ |  | |_  | |__| |_| | |   \ V /  __/\__ \
 |_| |_|_|_| \_/ \___|_|   \__|  \____\__,_|_|    \_/ \___||___/
                                                                


Made by Jkutkut
See more at https://github.com/Jkutkut
Instalation will begin shortly.
-Making sure that Python3 and the libraries needed are installed";

echo "-Checking Python3:" &&
sudo apt install python3 &&
echo "-Checking pip3:" &&
sudo apt install python3-pip &&
echo "-Checking pygame:" &&
sudo pip3 install pygame &&
(echo "
~~~~~~~~    ERROR AT INSTALLATION   ~~~~~~~~
    Please check README.md
" && exit 1) && #if error, exit



echo "-------------------------------------------
All things needed are correctly installed. Now installing the application.
" &&
echo "-Creating icon for the app" &&
sudo cp hilvertCurve.png /usr/share/icons/ && # move the icon to the correct dir

echo "-Creating executable" &&
sudo cp hilvertCurve.py /usr/bin/hilvertCurve && # move the python code
sudo chmod 755 /usr/bin/hilvertCurve && # make it able to be executed

echo "-Creating Desktop Entry" &&
echo "[Desktop Entry]
Type=Application
Encoding=UTF-8
Name=Hilvert Curve
Comment=Made by Jkutkut
Exec=hilvertCurve
Icon=/usr/share/icons/hilvertCurve.png
Terminal=false" >> hilvertCurve.desktop && # create the .desktop file

sudo mv hilvertCurve.desktop /usr/share/applications/ &&
echo "
Installation ended.
HilvertCurve installed correctly" ||

echo "
~~~~~~~~    ERROR AT INSTALLATION   ~~~~~~~~
    Not able to install the game.
" #if error, exit