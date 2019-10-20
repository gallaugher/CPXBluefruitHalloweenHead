# By Prof. John Gallaugher as a demo of fun things you can do with the 
# Adafruit Circuit Playground Express Bluefruit
# for more projects, see: https://bit.ly/GallaugherYouTube
# Twitter: @gallaugher, or gallaugher.com
# video of build at: http://bit.ly/cpxb-halloween-head-video
import board
import neopixel
import digitalio
import analogio
import simpleio
import busio
import touchio
import time
from digitalio import DigitalInOut, Direction, Pull
from adafruit_ble.uart_server import UARTServer
from audiopwmio import PWMAudioOut as AudioOut
from audiocore import WaveFile

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket
from adafruit_bluefruit_connect.button_packet import ButtonPacket

# set up touchpads A1
touchpad_A1 = touchio.TouchIn(board.A1)

# setup pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3, auto_write=True)

# name colors so you don't need to refer to numbers
RED = (255, 0, 0)
ORANGE = (255, 50, 0)
BLACK = (0, 0, 0)

# setup bluetooth
uart_server = UARTServer()

def playfile(filename):
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                pass

def checkTouch():
    # check if touched. If so, play sound
    if touchpad_A1.value:
        print("Touched!")
        pixels.fill(ORANGE)
        playfile("ah_dont_take_candy_from_strangers.wav")
        pixels.fill(BLACK)

while True:
    # set CPXb up so that it can be discovered by the app
    uart_server.start_advertising()
    while not uart_server.connected:
        checkTouch()
        pass

    # Now we're connected

    while uart_server.connected:

        # check if touched. If so, play sound
        checkTouch()
            
        if uart_server.in_waiting:
            try:
                packet = Packet.from_stream(uart_server)
            except ValueError:
                continue # or pass. This will start the next iteration of the loop and try to get a valid packet again.
            
            if isinstance(packet, ColorPacket): # check if a color was sent from color picker
                pixels.fill(packet.color)
            if isinstance(packet, ButtonPacket): # check if a button was pressed from control pad
                if packet.pressed:
                    if packet.button == ButtonPacket.BUTTON_1: # if button #1
                        pixels.fill(RED)
                        playfile("hey.wav")
                        pixels.fill(BLACK)
                    if packet.button == ButtonPacket.BUTTON_2: # if button #2
                        pixels.fill(ORANGE)
                        playfile("hey_you.wav")
                        pixels.fill(BLACK)
                    if packet.button == ButtonPacket.BUTTON_3: # if button #2
                        pixels.fill(RED)
                        playfile("take_candy.wav")
                        pixels.fill(BLACK)
                    if packet.button == ButtonPacket.BUTTON_4: # if button #2
                        pixels.fill(ORANGE)
                        playfile("theres_candy_in_my_head.wav")
                        pixels.fill(BLACK)
                    if packet.button == ButtonPacket.UP: # if button #2
                        pixels.fill(RED)
                        playfile("open_my_head.wav")
                        pixels.fill(BLACK)
