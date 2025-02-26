datalogger.onLogFull(function () {
    basic.showIcon(IconNames.Skull)
})
input.onButtonPressed(Button.A, function () {
    if (logging) {
        basic.showNumber(pins.digitalReadPin(DigitalPin.P0))
    } else {
        basic.showIcon(IconNames.Heart)
        basic.clearScreen()
    }
})
input.onButtonPressed(Button.AB, function () {
    if (input.logoIsPressed()) {
        basic.showIcon(IconNames.No)
        datalogger.deleteLog()
        logging = false
        datalogger.setColumnTitles("noise")
    }
})
let logging = false
datalogger.setColumnTitles("noise")
lcd1602.setAddress(
lcd1602.I2C_ADDR.addr1
)
lcd1602.set_LCD_Show(lcd1602.visibled.visible)
lcd1602.set_backlight(lcd1602.on_off.on)
lcd1602.clear()
basic.forever(function () {
    lcd1602.putNumber(
    pins.analogReadPin(AnalogPin.P0),
    8,
    0
    )
})
loops.everyInterval(100, function () {
    if (true) {
        datalogger.log(datalogger.createCV("noise", pins.analogReadPin(AnalogPin.P0)))
    }
})
