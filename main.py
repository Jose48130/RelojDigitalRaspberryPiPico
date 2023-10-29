from machine import I2C, Pin, RTC
from time import sleep
from i2c_lcd import I2cLcd

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

rtc = machine.RTC()
rtc.datetime((2023, 10, 25, 18, 18, 0, 0, 0))

while True:
    lcd.clear()
    timestamp=rtc.datetime()
    timestring="%04d-%02d-%02d      %02d:%02d:%02d"%(timestamp[0:3] +
                                                timestamp[4:7])
    lcd.putstr(timestring)
    sleep(0.7)
    