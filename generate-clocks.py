# If we just used a simple circle and two line representation of a clock, every possible minute
# could be represented in 12*60 = 720 samples. To make this a bit more challenging, we're going to
# do two things:
#     Create different styles of clock
#     Vary the length and thickness of the hands


import math
import numpy as np
from tqdm import tqdm
from PIL import Image, ImageDraw

# Visualization to confirm correct loading of data
from matplotlib import pyplot as plt


def get_minute_hand_angle(time):
    return


def get_hour_hand_angle(time):
    pass


def create_clock(time, widths=None, tickmarks=False, minute_tail=False):
    # Initialize pixel widths with default values
    if widths is None:
        widths = {}
    widths = {**{"clock": 3, "minute": 2, "hour": 2, "tickmark": 1}, **widths}

    # Create empty image and calculate content
    img = Image.new(mode="L", size=(50, 50))
    minute_hand_angle = time[1] * 6
    minute_hand_x = 25 + 20 * math.sin(math.radians(minute_hand_angle))
    minute_hand_y = 25 + 20 * math.cos(math.radians(minute_hand_angle + 180))
    hour_hand_angle = time[0] * 30 + time[1] * 0.5
    hour_hand_x = 25 + 10 * math.sin(math.radians(hour_hand_angle))
    hour_hand_y = 25 + 10 * math.cos(math.radians(hour_hand_angle + 180))

    # Draw clock components
    draw = ImageDraw.Draw(img)
    draw.arc([2, 2, 48, 48], 0, 360, "white", width=widths["clock"])
    draw.line(
        [25, 25, minute_hand_x, minute_hand_y], width=widths["minute"], fill="white"
    )
    draw.line([25, 25, hour_hand_x, hour_hand_y], width=widths["hour"], fill="white")

    if minute_tail:
        minute_tail_x = 25 - 5 * math.sin(math.radians(minute_hand_angle))
        minute_tail_y = 25 - 5 * math.cos(math.radians(minute_hand_angle + 180))
        draw.line(
            [25, 25, minute_tail_x, minute_tail_y],
            width=widths["minute"],
            fill="white",
        )

    if tickmarks:
        for hour in range(0, 12):
            tickmark_angle = hour * 30
            tickmark_start_x = 25 + 23 * math.sin(math.radians(tickmark_angle))
            tickmark_end_x = 25 + 18 * math.sin(math.radians(tickmark_angle))
            tickmark_start_y = 25 + 23 * math.cos(math.radians(tickmark_angle))
            tickmark_end_y = 25 + 18 * math.cos(math.radians(tickmark_angle))
            draw.line(
                [tickmark_start_x, tickmark_start_y, tickmark_end_x, tickmark_end_y,],
                "white",
                widths["tickmark"],
            )
    return np.asarray(img, dtype=np.uint8)


clock_images = []
clock_labels = []

# test_clock = create_clock([3, 41], tickmarks=True)
# test_im = Image.fromarray(test_clock)
# plt.imshow(test_im)
# plt.show()


with tqdm(total=4 * 4 * 4 * 2 * 2 * 12 * 60) as pbar:
    for hourWidth in range(1, 5):
        for minuteWidth in range(1, 5):
            for clockWidth in range(1, 5):
                for tickmarks in range(2):
                    for minute_tail in range(2):
                        for hour in range(12):
                            for minute in range(60):
                                clock = create_clock(
                                    [hour, minute],
                                    {
                                        "clock": clockWidth,
                                        "minute": minuteWidth,
                                        "hour": hourWidth,
                                    },
                                    tickmarks=tickmarks,
                                    minute_tail=minute_tail,
                                )
                                clock_images.append(clock)
                                clock_labels.append(
                                    np.array([hour, minute], dtype=np.uint8)
                                )
                                pbar.update(1)
clock_image_array = np.array(clock_images, dtype=np.uint8)
clock_label_array = np.array(clock_labels, dtype=np.uint8)
with open("./clock_images.npy", "w") as f:
    clock_image_array.tofile(f)
with open("./clock_labels.npy", "w") as f:
    clock_label_array.tofile(f)
