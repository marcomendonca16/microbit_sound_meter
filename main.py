def on_log_full():
    basic.show_icon(IconNames.SKULL)
datalogger.on_log_full(on_log_full)

def on_button_pressed_a():
    if logging:
        basic.show_number(pins.digital_read_pin(DigitalPin.P0))
    else:
        basic.show_icon(IconNames.HEART)
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global logging
    if input.logo_is_pressed():
        basic.show_icon(IconNames.NO)
        datalogger.delete_log()
        logging = False
        datalogger.set_column_titles("noise")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

logging = False
datalogger.set_column_titles("noise")
lcd1602.set_address(lcd1602.I2C_ADDR.ADDR1)
lcd1602.set_LCD_Show(lcd1602.visibled.VISIBLE)
lcd1602.set_backlight(lcd1602.on_off.ON)
lcd1602.clear()

def on_forever():
    lcd1602.put_number(pins.analog_read_pin(AnalogPin.P0), 8, 0)
basic.forever(on_forever)

def on_every_interval():
    if True:
        datalogger.log(datalogger.create_cv("noise", pins.analog_read_pin(AnalogPin.P0)))
loops.every_interval(100, on_every_interval)
