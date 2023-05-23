import numpy as np
import matplotlib.pyplot as plt


def plot_circles(centres, large_radius, small_radius, save = False, savename=None):
    fig, ax = plt.subplots(figsize = (10, 10))
    ax.axis('off')
    ax.scatter(0,0, color = 'red')
    ax.add_patch(plt.Circle((0,0), radius = large_radius, fill = False, linewidth = 2.0, color = 'black'))
    ax.axis('scaled')
    for rad, centre in enumerate(centres):
        (x,y) = centre
        #ax.annotate(str(rad+1), (x,y), (x,y), fontsize = 16)
        ax.add_patch(plt.Circle(centre, radius = small_radius, fill = False, linewidth = 1.0, color = 'blue'))
    if save:
        plt.savefig(savename)
    plt.show()

def packing_density(centres, r, R = 1, NumSamples = 100000):
    '''
    centres: centres of the spheres [N,2], N: Number of spheres
    r: radius of each circle
    R: radius of enclosing circle
    NumSamples: number of points to be sampled towards density calculation
    '''
    x = np.random.normal(size=[NumSamples, 2])
    u = np.random.uniform(size=[NumSamples, 1])
    norm = np.linalg.norm(x, axis = 1, keepdims=True)

    #these points are distributed uniformly inside the circle
    coordinates = x*np.power(u, 1/2)/norm*R
    
    centres_reshaped = np.reshape(centres, [1, centres.shape[0], centres.shape[1]])
    coordinates_reshaped = np.reshape(coordinates, [coordinates.shape[0], 1, coordinates.shape[1]])
    distances_from_centres = np.linalg.norm(coordinates_reshaped - centres_reshaped, axis = 2)
    min_distances = np.min(distances_from_centres, axis = 1)
        
    return np.sum(min_distances < r)/NumSamples