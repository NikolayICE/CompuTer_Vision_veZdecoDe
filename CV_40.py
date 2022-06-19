import webcolors
import tensorflow as tf
import matplotlib.pyplot as plt
import csv


def closest_colour(requested_colour):
    min_colours = {}
    colors_arr = []
    for i in webcolors.CSS3_HEX_TO_NAMES.items():
        if i[1] == 'yellow' or i[1] == 'black' or i[1] == 'white' or i[1] == 'red' or i[1] == 'blue':
            colors_arr.append(i)
    for key, name in colors_arr:
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def calc_metric(image, x, y, w, h):
    image_cropped = image[y:y + h, x:x + w, 0:3].numpy()
    min_dist = 10000000000000
    plt.imshow(image_cropped)
    plt.show()
    dom_color = []
    for red in range(0, 256, 20):
        for green in range(0, 256, 20):
            for blue in range(0, 256, 20):
                dist = 0
                for height in range(0, h, 5):
                    for width in range(0, w, 5):
                        dist += ((red - image_cropped[height][width][0]) ** 2 + (
                                green - image_cropped[height][width][1]) ** 2 + (
                                         blue - image_cropped[height][width][2]) ** 2)
                if dist < min_dist:
                    min_dist = dist
                    dom_color = (red, green, blue)
    closest_color = closest_colour(dom_color)
    print(closest_color)
    return closest_color


anss = []

for j in range(1, 101):

    image = tf.io.read_file(f'/content/sample_data/img{j}.jpg')

    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, [400, 400])
    image = tf.cast(image, dtype=tf.uint8)
    ans = calc_metric(image, image.shape[0] // 2 - 100, image.shape[1] // 2 - 50, 175, 175)
    if ans == 'white':
        ans = 'white_silver'
    elif ans == 'blue':
        ans = 'blue_cyan'
    anss.append(ans)

file = open('output_colors.csv', 'w')
writ = csv.writer(file)
names = ['0' * (5 - len(str(i))) + str(i + 1) + '.jpg' for i in range(99)]
for i in range(99):
    writ.writerow([names[i], anss[i]])

