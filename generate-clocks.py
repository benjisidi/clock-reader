# If we just used a simple circle and two line representation of a clock, every possible minute
# could be represented in 12*60 = 720 samples. To make this a bit more challenging, we're going to
# do two things:
#     Create different styles of clock
#     Vary the length and thickness of the hands


from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import math


def get_minute_hand_angle(time):
    return


def get_hour_hand_angle(time):
    pass


class Clock:
    def __init__(self, time, widths=None):
        # Initialize pixel widths with default values
        if widths is None:
            widths = {}
        widths = {**{"clock": 5, "minute": 2, "hour": 2}, **widths}

        # Create empty image and calculate content
        img = Image.new(mode="L", size=(100, 100))
        minute_hand_angle = time[1] * 6
        minute_hand_x = 50 + 40 * math.sin(math.radians(minute_hand_angle))
        minute_hand_y = 50 + 40 * math.cos(math.radians(minute_hand_angle + 180))
        hour_hand_angle = time[0] * 30 + time[1] * 0.5
        hour_hand_x = 50 + 20 * math.sin(math.radians(hour_hand_angle))
        hour_hand_y = 50 + 20 * math.cos(math.radians(hour_hand_angle + 180))

        # Draw clock components
        draw = ImageDraw.Draw(img)
        draw.arc([10, 10, 90, 90], 0, 360, "white", width=widths["clock"])
        draw.line(
            [50, 50, minute_hand_x, minute_hand_y], width=widths["minute"], fill="white"
        )
        draw.line(
            [50, 50, hour_hand_x, hour_hand_y], width=widths["hour"], fill="white"
        )
        self.img = img

    def show(self):
        plt.imshow(self.img)
        plt.show()


clock1 = Clock([5, 30], {"clock": 1})
clock2 = Clock([3, 15], {"hour": 3, "minute": 2, "clock": 4})

clock1.show()
clock2.show()
