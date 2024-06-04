import pyautogui as pag, 
from time import sleep

sleep(1)

while True:
  printf("you will Now have autoclick");
  pag.click(button="left")
  sleep(0.5) # two clicks per second?

  pag.moveTo(100, 100) # move cursor to X=100 Y=100 pixels
