# day 8
import sys


# Read the data
def read_command_line():
    if len(sys.argv) >= 2 and len(sys.argv[1]) > 0:
        return sys.argv[1]
    else:
        print("Please include the test data file as a command line argument.")


def decode_image(image, width, height, layers):
    blank = 9
    final_image = []
    for h in range(height):
        image_row = []
        for w in range(width):
            image_row.append(blank)
        final_image.append(image_row)

    for l in range(layers):
        for h in range(height):
            for w in range(width):
                if final_image[h][w] == blank:  # not colored yet
                    if image[l][h][w] == '1':
                        final_image[h][w] = 1
                    elif image[l][h][w] == '0':
                        final_image[h][w] = 0
                    elif image[l][h][w] == '2':
                        pass
                    else:
                        print('yatzee')

    for r in final_image:
        print(r)


def read_image(width, height, layers):
    file_name = read_command_line()

    image = []
    if file_name:
        data = open(file_name, "r")
        image = []

        lowest_layer = 999999999999999
        lowest_index = 0
        num_zero_one_twos = []
        for l in range(layers):
            num_zero_one_twos.append([0, 0, 0])
            image_layer = []
            for h in range(height):
                image_data = data.read(width)
                image_row = list(image_data)
                image_layer.append(image_row)
                num_zero_one_twos[l][0] += image_row.count('0')
                num_zero_one_twos[l][1] += image_row.count('1')
                num_zero_one_twos[l][2] += image_row.count('2')

            image.append(image_layer)
            print('layer', l)
            print(image_layer)
            if num_zero_one_twos[l][0] < lowest_layer:
                lowest_index = l
                lowest_layer = num_zero_one_twos[l][0]

        print("z:1*2 : ", num_zero_one_twos[lowest_index][0], num_zero_one_twos[lowest_index][1]*num_zero_one_twos[lowest_index][2])
        return image


if __name__ == "__main__":
    iw = 25  # 25, 6, 50
    ih = 6
    il = 50
    decode_image(read_image(iw, ih, il), iw, ih, il)  # hard coded 25x6 with 2 layers
