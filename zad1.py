from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt

def main():

    image_path = 'textExample.png'
    di_path = 'di.png'

# flatten - convert to grey-scale
    source = 255 - ndimage.imread(image_path, flatten=True)
    pattern = 255 - ndimage.imread(di_path, flatten=True)

#    plt.imshow(pattern, cmap='jet')
    plt.imshow(source)
    plt.savefig('foooo.png')
    plt.show()

    fi = np.fft.fft2(source)
    fp = np.fft.fft2(np.rot90(pattern, 2), fi.shape)
    m = np.multiply(fi, fp)
    #
    corr = np.fft.ifft2(m)
    corr = np.abs(corr)
    corr = corr.astype(float)
    #

    np.amax(corr)
    corr[corr < (0.95 * np.amax(corr))] = 0

    suma = ndimage.label(corr)
    print(suma[1])

    for i in range(len(corr)):
        for j in range(len(corr[0])):
            if corr[i][j] != 0:
                print(str(corr[i][j]) + ' ' + str(i) + ' ' + str(j), end=' ')
        print('')

    plt.imshow(corr)
    plt.savefig('foo.png')
    plt.show()

if __name__ == '__main__':
    main()
