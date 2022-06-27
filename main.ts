ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("TP-LINK_WiFi_2", "your_pwd")
basic.showLeds(`
    # . . . .
    . . . # .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    # # . . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    # # # . .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    # # # # .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.pause(1000)
basic.showLeds(`
    # # # # .
    . . . . .
    . . . . .
    . . . . .
    . . . . .
    `)
basic.pause(1000)
if (ESP8266_IoT.wifiState(true)) {
    basic.showLeds(`
        . . . . .
        . . . . #
        . . . # .
        # . # . .
        . # . . .
        `)
} else {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
}
basic.forever(function () {
	
})
