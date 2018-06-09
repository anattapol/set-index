from random import randint
import numpy as np
import matplotlib.pyplot as plt
bagIS = [58.54,58.97,56.98,57.45,51.47,53.26,56.95,59.15,58.29,58.99,53.44,52.13,52.78,52,50.29,48.21,48.51,49.71,49.66,47.95,48.98,45.32]
bagOOS = [0,33.33,72.22,55.56,43.75,58.49,57.45,31.25,56.52,41.38,47.37,57.14,52.17,48.65,40.68,48.57,44.64,44.74,35.59,56.67,32]
def pickup(bag, n):
    sum = 0
    bagsize = len(bag)
    for i in range(n):
        sum += bag[randint(0,bagsize-1)]
    return sum/n

def main():
    x = []
    for i in range(10000):
        x.append(pickup(bagOOS,10000))
    # print(x)
    x = np.array(x)
    # print(x)
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    # plt.axis([40, 60, 0, 1])
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()