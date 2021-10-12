from picamera import PiCamera
from time import sleep
from gpiozero import Button

savepath = '/home/pi/Pictures'

button=Button(21)
camera=PiCamera()

camera.resolution = (1280,720)
camera.framerate(15)
camera.rotation=0
now = datetime.datetime.now()
filename = now.strftime('%Y-%m-%d %H:%M:%S')
camera.start_preview()
button.wait_for_press()
camera.stop_preview()
camera.ca[ture(savepath + '/' +filename + '.jpg')