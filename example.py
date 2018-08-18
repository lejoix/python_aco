import numpy as np
import xml.etree.ElementTree as ET

from ant_colony import AntColony

distances = np.array([[np.inf, 2, 2, 5, 7],
                      [2, np.inf, 4, 8, 2],
                      [2, 4, np.inf, 1, 3],
                      [5, 8, 1, np.inf, 2],
                      [7, 2, 3, 2, np.inf]])


def loadTsp (name='gr21.xml'):
    tree = ET.parse(name)
    root = tree.getroot()

    distances = np.empty([[]])
    return distances


ant_colony = AntColony(distances, 1, 1, 100, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.run()
print "shorted_path: {}".format(shortest_path)

