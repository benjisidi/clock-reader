# If we just used a simple circle and two line representation of a clock, every possible minute
# could be represented in 12*60 = 720 samples. To make this a bit more challenging, we're going to
# do two things:
#     Create different styles of clock
#     Vary the length and thickness of the hands


from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import math
from tqdm import tqdm


def get_minute_hand_angle(time):
    return


def get_hour_hand_angle(time):
    pass


class Clock:
    def __init__(self, time, widths=None, tickmarks=False, minute_tail=False):
        # Initialize pixel widths with default values
        if widths is None:
            widths = {}
        widths = {**{"clock": 5, "minute": 2, "hour": 2, "tickmark": 1}, **widths}

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

        if minute_tail:
            minute_tail_x = 50 - 10 * math.sin(math.radians(minute_hand_angle))
            minute_tail_y = 50 - 10 * math.cos(math.radians(minute_hand_angle + 180))
            draw.line(
                [50, 50, minute_tail_x, minute_tail_y],
                width=widths["minute"],
                fill="white",
            )

        if tickmarks:
            for hour in range(0, 12):
                tickmark_angle = hour * 30
                tickmark_start_x = 50 + 30 * math.sin(math.radians(tickmark_angle))
                tickmark_end_x = 50 + 40 * math.sin(math.radians(tickmark_angle))
                tickmark_start_y = 50 + 30 * math.cos(math.radians(tickmark_angle))
                tickmark_end_y = 50 + 40 * math.cos(math.radians(tickmark_angle))
                draw.line(
                    [
                        tickmark_start_x,
                        tickmark_start_y,
                        tickmark_end_x,
                        tickmark_end_y,
                    ],
                    "white",
                    widths["tickmark"],
                )

        self.img = img

    def show(self):
        plt.imshow(self.img)
        plt.show()

    def save(self, loc):
        pass


# clock1 = Clock([5, 30], {"clock": 1}, tickmarks=True, minute_tail=True)
# clock2 = Clock(
#     [3, 15], {"hour": 5, "minute": 5, "clock": 5}, tickmarks=True, minute_tail=True
# )

# clock1.show()
# clock2.show()

with tqdm(total=5 * 5 * 5 * 2 * 2 * 12 * 60) as pbar:
    for hourWidth in range(1, 6):
        for minuteWidth in range(1, 6):
            for clockWidth in range(1, 6):
                for tickmarks in range(2):
                    for minute_tail in range(2):
                        for hour in range(12):
                            for minute in range(60):
                                clock = Clock(
                                    [hour, minute],
                                    {
                                        "clock": clockWidth,
                                        "minute": minuteWidth,
                                        "hour": hourWidth,
                                    },
                                    tickmarks=tickmarks,
                                    minute_tail=minute_tail,
                                )
                                pbar.update(1)
