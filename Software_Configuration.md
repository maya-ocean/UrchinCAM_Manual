----------------------------------------------------
UrchinCAM microSD Formatting and Initial Raspberry Pi Installation
----------------------------------------------------






On laptop: Erase microSD card and format as ExFAT (camille’s github)
On laptop: Use Raspberry Pi Imager to download OS onto microSD
PW: urchin$
Plug microSD into Raspberry Pi 
Set date/time manually
sudo date -s “2025-03-10 10:53:00”
Turn on WiFi and connect to network (sometimes UHM is funky, try hotspot if errors)
Install Witty Pi package
pi@raspberrypi:~ $ wget https://www.uugear.com/repo/WittyPi4/install.sh
pi@raspberrypi:~ $ sudo sh install.sh
Reboot Pi
Use Witty Pi RTC to correct the time 
cd wittypi
pi@raspberrypi:~/wittypi $ ./wittyPi.sh
3 (to sync with network time)
13 (to exit)
cd ~
Verify Git installation
sudo apt-get install git
Clone GitHub Repository onto Pi
git clone https://github.com/maya-ocean/UrchinPOD_repo.git
cd UrchinPOD_repo
Test camera function 
libcamera-hello 
Set Witty Pi schedule
Add urchincam_single_cycle.py script to the Witty Pi file afterStartup.sh
