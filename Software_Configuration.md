
# UrchinCAM microSD Formatting and Initial Raspberry Pi OS Configuration

Erase microSD card and format as ExFAT (camille’s github)

Install Raspberry Pi Imager 
Use Raspberry Pi Imager to download OS onto microSD
PW: urchin$

# UrchinCAM Raspberry Pi Software Instructions

### Manually set date and time. 
    sudo date -s “2025-03-10 10:53:00”
    
### Turn on WiFi and connect to network.
Note: UHM WiFi can cause issues. If that's the case, try using another network or a phone hotspot. 

### Install Witty Pi package
  ```
  pi@raspberrypi:~ $ wget https://www.uugear.com/repo/WittyPi4/install.sh
  pi@raspberrypi:~ $ sudo sh install.sh
  ```

### Sync to Network Time 
  ```
  pi@raspberrypi:~ $ cd wittypi
  pi@raspberrypi:~/wittypi $ ./wittyPi.sh
  3 (sync with network time)
  13 (exit)
  cd ~
  ```

### Verify Git installation
  ```
  sudo apt-get install git
  ```

### Clone GitHub Repository onto Pi
  ```
  git clone https://github.com/maya-ocean/UrchinCAM_repo.git
  cd UrchinPOD_repo
  ```

### Test camera 
```
libcamera-hello
```
Adjust camera lens by increasing the duration of the preview. The code runs the camera for 1 minute. 
```
libcamera-vid -t 60000
```
### Initialize USB Flash Drive
Make a directory that the USB drive can be mounted to. 
```
cd ~
sudo mkdir -p /mnt/DATA
sudo chown pi:pi /mnt/DATA
```

Insert USB Flash Drive into OTG adapter. 

Check to make sure the Raspberry Pi has recognized it. 
```
lsblk
```
You should see a device listed that is named sda1, sdb1, or something similar. 

The UrchinCAM script will mount the USB drive on boot. 

### Set Witty Pi schedule
Move the file on_28_off_2.wpi to the Schedules folder in the Witty Pi directory. 

Choose a schedule script in the Witty Pi interface. 
```
pi@raspberrypi:~ $ cd wittypi
pi@raspberrypi:~/wittypi $ ./wittyPi.sh
What do you want to do? 6 (Choose schedule script)
Which schedule script do you want to use? 3 (on_28_off_2.wpi)
```

### Run Python script on boot using Witty Pi
Open the Witty Pi after startup script. This will run the UrchinCAM Python script after Witty Pi has booted up the Raspberry Pi and after Witty Pi has finished running the schedule script. 
```
pi@raspberrypi:~ $ cd wittypi
pi@raspberrypi:~/wittypi $ sudo nano afterStartup.sh
```
Add the following to the bottom of the script. 
```
python3 /home/pi/UrchinCAM_repo/UrchinCAM.py &
```
Save (ctrl+O) and exit (ctrl+X). 
