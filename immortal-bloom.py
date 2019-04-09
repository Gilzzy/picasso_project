from sense_hat import SenseHat
sense = SenseHat()

blue = ( 0, 0, 50)
yellow = ( 0, 50, 0)

while True:
    acceleration = sense.get_accelerometer_raw()

    x = round(acceleration['x'],3)
    y = round(acceleration['y'],3)

    b1 = int(round(x*255,0))
    b2 = int(round(y*255,0))
    blue = ( b2, 0, b1)


    sense.show_message("x".format(x), text_colour=yellow, back_colour=blue, scroll_speed=0.01)

