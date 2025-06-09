import board
import displayio
import busio
import adafruit_displayio_ssd1306
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler

displayio.release_displays()

i2c = busio.I2C(scl=board.D7, sda=board.D6)  # GPIO7 = SCL, GPIO6 = SDA
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)  # 0x3C is default SSD1306 I2C addr
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

keyboard = KMKKeyboard()

# SW1, SW2, SW3 → GPIO0, GPIO1, GPIO2
keyboard.matrix = KeysScanner(
    pins=[board.D0, board.D1, board.D2],
    value_when_pressed=False,
)

# A/B/SW → GPIO28, GPIO27, GPIO26
encoder_handler = EncoderHandler()
encoder_handler.pins = (board.D28, board.D27, board.D26, False)
keyboard.modules.append(encoder_handler)

# Run KMK
if __name__ == '__main__':
    keyboard.go()

