ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("TP-LINK_WiFi_2", "your_pwd")
basic.show_leds("""
    # . . . .
        . . . # .
        . . . . .
        . . . . .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    # # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    # # # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    # # # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.pause(1000)
basic.show_leds("""
    # # # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.pause(1000)
if ESP8266_IoT.wifi_state(True):
    basic.show_leds("""
        . . . . .
                . . . . #
                . . . # .
                # . # . .
                . # . . .
    """)
else:
    basic.show_leds("""
        # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
    """)

def on_forever():
    pass
basic.forever(on_forever)
