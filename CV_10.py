import cv2 as cv


def merge_and_channels(input_dir, output_dir):
    for i in range(1, 101):
        path1 = str(input_dir) + '/' +'0' * (5 - len(str(i))) + str(i) + '_b.jpg'
        path2 = str(input_dir)+'/' + '0' * (5 - len(str(i))) + str(i) + '_g.jpg'
        path3 = str(input_dir)+'/' + '0' * (5 - len(str(i))) + str(i) + '_r.jpg'
        print(path1)

        image_b = cv.imread(path1)
        b, g1, r1 = cv.split(image_b)
        image_g = cv.imread(path2)
        b1, g, r2 = cv.split(image_g)
        image_r = cv.imread(path3)
        b2,  g2, r = cv.split(image_r)

        print(r)
        print(b)
        print(g)

        image_new = cv.merge([b, g, r])
        cv.imwrite(f'{output_dir}/img{i}.jpg', image_new)


merge_and_channels('data', 'data1')

