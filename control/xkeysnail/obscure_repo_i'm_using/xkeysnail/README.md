# Xkeysnail key mapping
Modify keys on Ubuntu like macOS

# Installation

+ xkeysnail  
```
sudo apt install python3-pip
sudo pip3 install xkeysnail
```

+ udev rules and systemd service
```
cd [working dir]
git clone git@github.com:MikiyaShibuya/xkeysnail.git
cd xkeysnail
sudo ./setup.sh
```
+ add user to groups
```
sudo groupadd uinput
sudo usermod -a -G input [user name]
sudo usermod -a -G uinput [user name]
# check if the user is added to the groups
cat /etc/group | grep [user name]
```

+ apply udev rules
```
sudo reboot
```

+ check the access permittion
```
python check_perm.py
```

+ enable and start systemd service
```
systemctl --user enable xkeysnail
systemctl --user start xkeysnail
```
