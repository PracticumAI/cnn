import numpy as np
import matplotlib.pyplot as plt

img_size = 20

img = np.random.uniform(size=(img_size, img_size))
img = np.where(img>.5, 0, 1)

# The get_results function

def get_results(element):
    result = np.zeros((img_size, img_size))
    binary_result = np.zeros((img_size, img_size)) 
    for y in range(1, img_size-1):
        for x in range(1, img_size-1):
            sum = 0
            for ey in range(3):
                for ex in range(3):
                    sum += img[y+ey-1][x+ex-1]*element[ey][ex] 
            result[y][x] = sum
            binary_result[y][x] = sum==3
    return (result, binary_result)

# Show the five pictures for applying an element to an image

def show_five(img, element, result, binary_result, filename):
    plt.subplot(1, 5, 1)
    plt.imshow(element, interpolation='nearest', vmin=-1, vmax=1, cmap='autumn')
    plt.plot([.5, .5], [-.5, 2.5], color='black')
    plt.plot([1.5, 1.5], [-.5, 2.5], color='black')
    plt.plot([-.5, 2.5], [.49, .49], color='black')
    plt.plot([-.5, 2.5], [1.5, 1.5], color='black')
    plt.xticks([],[])
    plt.yticks([],[])
    plt.title('(a)')
    plt.subplot(1, 5, 2)
    plt.imshow(img, interpolation='nearest', cmap='gray')
    plt.xticks([],[])
    plt.yticks([],[])
    plt.title('(b)')
    plt.subplot(1, 5, 3)
    plt.imshow(result, interpolation='nearest', vmin=-6, vmax=3, cmap='cool')
    plt.xticks([],[])
    plt.yticks([],[])
    plt.title('(c)')
    plt.subplot(1, 5, 4)
    plt.imshow(binary_result, interpolation='nearest', cmap='gray')
    plt.xticks([],[])
    plt.yticks([],[])
    plt.title('(d)')
    plt.subplot(1, 5, 5)
    mask_result = np.zeros(img.shape)
    for y in range(0, img_size):
        for x in range(0, img_size):
            mask_result[y][x] = .45 + (.1 * img[y][x])
    for y in range(0, img_size):
        for x in range(0, img_size):
            for ty in range(-1, 2):
                for tx in range(-1, 2):
                    if (y+ty >= 0) and (y+ty < img_size) and (x+tx >= 0) and (x+tx < img_size):
                        if binary_result[y+ty][x+tx] > .5:
                            mask_result[y][x] = img[y][x]
    plt.imshow(mask_result, interpolation='nearest', cmap='gray')
    
    plt.xticks([],[])
    plt.yticks([],[])
    plt.title('(e)')
    plt.tight_layout()
    plt.savefig(filename)
    plt.show()