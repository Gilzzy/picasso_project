from sense_hat import SenseHat
import time
sense = SenseHat()

blue = ( 0, 0, 50)
yellow = ( 0, 50, 0)

while True:
    acceleration = sense.get_accelerometer_raw()

    x = round(acceleration['x'],3)
    y = round(acceleration['y'],3)

    b1 = int(round(x*255,0))
    b2 = int(round(y*255,0))
    blue = (255, 255, 255)
    
    for x in range(0,8):
        for y in range(0,8):
            sense.set_pixel(x, y, (0,0,255))
            time.sleep(0.050)
           # print(x)
           # print(y)
    sense.clear()

    for x in range(0,255):
        for y in range(0,255):
            sense.set_pixel(0,0, (x,0,y))
            time.sleep(0.001)

    sense.clear()
    
    #    sense.show_message("x".format(x), text_colour=yellow, back_colour=blue, scroll_speed=0.01)

