from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt


def main():
    textExamplePath = 'textExample.png'
    ePath = 'foooo.png'

    source = 255 - ndimage.imread(textExamplePath, flatten=True)

    pattern = 255 - ndimage.imread(ePath, flatten=True)



    # plt.imshow(pattern, cmap='jet')
    plt.imshow(source, cmap='jet')
    # plt.savefig('foooo.png')
    plt.show()


    fi = np.fft.fft2(source)
    fp = np.fft.fft2(np.rot90(pattern, 2), fi.shape)
    m = np.multiply(fi, fp)
    #
    corr = np.fft.ifft2(m)
    corr = np.abs(corr)
    corr = corr.astype(float)
    #
    corr[corr < 0.8 * np.amax(corr)] = 0

    suma = ndimage.label(corr)
    print(suma[1])

    for i in range(len(corr)):
        for j in range(len(corr[0])):
            if corr[i][j] != 0:
                print(str(corr[i][j]) + ' ' + str(i) + ' ' + str(j), end=' ')
        print('')

    plt.imshow(corr, cmap='jet')
    plt.savefig('foo.png')
    plt.show()


if __name__ == '__main__':
    main()
