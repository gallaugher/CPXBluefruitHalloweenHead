import board
import neopixel
import time
import digitalio
import adafruit_lis3dh
import busio
import touchio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=True)

RED = (255, 0, 0)
ORANGE = (255, 50, 0)
YELLOW = (255, 165, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
INDIGO = (50, 0, 255)
VIOLET = (128, 0, 128)
BLACK = (0, 0, 0)

colors = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, BLACK]

touch_A1 = touchio.TouchIn(board.A1)

try:
    from audiocore import WaveFile
except ImportError:
    from audioio import WaveFile

try:
    from audioio import AudioOut
except ImportError:
    try:
        from audiopwmio import PWMAudioOut as AudioOut
    except ImportError:
        pass  # not always supported by every board!

# Enable the speaker
spkrenable = digitalio.DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = digitalio.Direction.OUTPUT
spkrenable.value = True

button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.DOWN)

def play_file(filename):
    wave_file = open(filename, "rb")
    with WaveFile(wave_file) as wave:
        with AudioOut(board.SPEAKER) as audio:
            audio.play(wave)
            while audio.playing:
                 pass
    print("Finished")

while True:
    if touch_A1.value:
        pixels.fill(ORANGE)
        play_file("evil_laugh.wav")
        pixels.fill(BLACK)
        time.sleep(0.5)

    if button_A.value:
        pixels.fill(RED)
        play_file("laugh.wav")
        pixels.fill(BLACK)
        time.sleep(0.5)