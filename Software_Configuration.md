
UrchinCAM microSD Formatting and Initial Raspberry Pi OS Configuration
---------------------------------------------------------------
Erase microSD card and format as ExFAT (camille’s github)

Install Raspberry Pi Imager 
Use Raspberry Pi Imager to download OS onto microSD
PW: urchin$

UrchinCAM Raspberry Pi Software Instructions
---------------------------------------------------------------
Set date and time to avoid errors with Raspberry Pi communication. 
    sudo date -s “2025-03-10 10:53:00”

Turn on WiFi and connect to network.
Note: UHM WiFi can cause issues. If that's the case, try using another network or a phone hotspot. 

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

Test camera 
  libcamera-hello 

Set Witty Pi schedule
Add urchincam_single_cycle.py script to the Witty Pi file afterStartup.sh
