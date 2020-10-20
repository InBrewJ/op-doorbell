# References

A list of helpful articles:

- https://trello.com/c/rEfEwtLt/99-op-doorbell

```
Super complex systemd service code for the case when script bugs out at start up:
https://github.com/FrankBau/dl161s/wiki

associated rpi thread:
https://www.raspberrypi.org/forums/viewtopic.php?t=180830
Edit - Add Link as Attachment - Delete
InBrewJ yesterday at 07:42

Long cable problem:

https://electronics.stackexchange.com/questions/49824/microcontroller-with-a-long-wire-for-digital-input/49984#49984
Edit - Add Link as Attachment - Delete
InBrewJ 18 Oct at 23:16

Someone with a floating button problem:

https://forum.arduino.cc/index.php?topic=59022.30
Edit - Add Link as Attachment - Delete
InBrewJ 18 Oct at 10:20

RPi log rotation:
https://www.raspberrypi.org/forums/viewtopic.php?t=158985
Edit - Add Link as Attachment - Delete
InBrewJ 17 Oct at 23:06 (edited)

Script to reconnect WiFi:
https://raspberrypi.stackexchange.com/questions/27475/wifi-disconnects-after-period-of-time-on-raspberry-pi-doesnt-reconnect

(but also just try Armbian again)
Edit - Add Link as Attachment - Delete
InBrewJ 17 Oct at 11:19

Daemon Python scripts (for send/receive)

https://pypi.org/project/python-daemon/
Edit - Add Link as Attachment - Delete
InBrewJ 17 Oct at 11:15

Different ways of running containers (like podman etc)

https://martinheinz.dev/blog/35
Edit - Add Link as Attachment - Delete
InBrewJ 17 Oct at 09:13

WiFi only works when ethernet plugged in:
https://www.raspberrypi.org/forums/viewtopic.php?t=81021
Edit - Add Link as Attachment - Delete
InBrewJ 15 Oct at 21:24

Download single folders from GitHub with svn:
https://stackoverflow.com/questions/7106012/download-a-single-folder-or-directory-from-a-github-repo
Edit - Add Link as Attachment - Delete
InBrewJ 15 Oct at 21:24

programming Arduino from the command line (i.e. from SwitchBox):
https://playground.arduino.cc/Learning/CommandLine/
Edit - Add Link as Attachment - Delete
InBrewJ 14 Oct at 21:32 (edited)

Investigation into RabbitMQ:
- https://www.rabbitmq.com/tutorials/tutorial-one-python.html
- https://hub.docker.com/_/rabbitmq
- https://funprojects.blog/2018/12/07/rabbitmq-for-iot/
Edit - Add Link as Attachment - Delete
InBrewJ 14 Oct at 21:29

Installed docker via:
- https://phoenixnap.com/kb/docker-on-raspberry-pi
Edit - Add Link as Attachment - Delete
InBrewJ 14 Oct at 19:53

Change hostname:
https://www.cyberciti.biz/faq/debian-change-hostname-permanently/
(but just restart the machines instead of doing the init.d thing - bc it doesn't work!)
Edit - Add Link as Attachment - Delete
InBrewJ 14 Oct at 09:28

mDNS for the Pi and the Pine64:

https://superuser.com/questions/1446206/mdns-not-working-for-raspberry-pi-zero-w
Edit - Add Link as Attachment - Delete
InBrewJ 13 Oct at 20:35

Network commands:

    Link quality
    https://askubuntu.com/questions/95676/a-tool-to-measure-signal-strength-of-wireless
    nmap scan
    https://itsfoss.com/how-to-find-what-devices-are-connected-to-network-in-ubuntu/
        sudo nmap -sn 192.168.1.0/24

Edit - Add Link as Attachment - Delete
InBrewJ 13 Oct at 18:54

Post arrival of a lovely RPi 3B+:

    How to automatically connect to the wifi:
    https://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/

Edit - Add Link as Attachment - Delete
InBrewJ 11 Oct at 19:01 (edited)

Connecting to wifi:
- https://medium.com/@daniel.cohen/setting-up-usb-wifi-dongle-on-pine64-dc41def83c75

Helpful commands:
- nmcli r wifi on
- nmcli dev wifi (to list networks, the command in that article didn't work)
- nmcli d wifi connect <SSID> password <password>

    cron @reboot start up script like:
    https://raspberrypi.stackexchange.com/questions/8734/execute-script-on-start-up

Edit - Add Link as Attachment - Delete
InBrewJ 11 Oct at 14:45 (edited)

Loads of problems with audio Jack on the Pine64:

Revolves around me having a board from 2016 with a very recent version of Armbian [sunglasses]

See this (unfortunately from 2016)
http://forum.pine64.org/showthread.php?tid=807&page=2

The general fix seemed to be to:
- run:
cat <<EOF >/etc/modules-load.d/pine64-audiojack.conf sunxi_codec sunxi_i2s sunxi_sndcodec EOF
- download longsleep's alsa config

Helpful commands include:
- aplay -l (listing audio devices)
- the everpresent alsamixer
- mplayer -ao alsa:device=hw=1.0 file_example_MP3_2MG.mp3 to specify the alsa device
- setting the default device:
- https://www.alsa-project.org/wiki/Setting_the_default_device

HDMI works fine, might need to downgrade the kernel to make the audio jack work, see this post from 2019:
https://forum.armbian.com/topic/9378-pine64-audio-jack-problem/

This post also exists:

https://forum.pine64.org/showthread.php?tid=9589

```
