def on_forever():
    led.plot(1, 0)
    led.plot(3, 0)
    led.plot(0, 1)
    led.plot(1, 1)
    led.plot(2, 1)
    led.plot(3, 1)
    led.plot(4, 1)
    led.plot(0, 2)
    led.plot(1, 2)
    led.plot(2, 2)
    led.plot(3, 2)
    led.plot(4, 2)
    led.plot(1, 3)
    led.plot(2, 3)
    led.plot(3, 3)
    led.plot(2, 4)
basic.forever(on_forever)
