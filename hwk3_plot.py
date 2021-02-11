import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    fname_part1 = 'problem_1_2_data.txt'
    data_to_plot = np.loadtxt(fname_part1,delimiter=',',skiprows=2)
    print("Plot regarding error of Forward and Central difference method: ")

    plt.plot(data_to_plot(:,0))
    plt.plot(data_to_plot(:,1))
    plt.xlabel('values of h')
    plt.ylabel('error')
    plt.savefig('plot3.png')
    
