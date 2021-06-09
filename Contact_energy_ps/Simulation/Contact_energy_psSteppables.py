
from cc3d.core.PySteppables import *
import numpy as np
import random as random

class Contact_energy_psSteppable(SteppableBasePy):

    def __init__(self,frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        
        self.build_wall(self.BOUNDARY)
        
        for x in range(11, 125, 16):
            for y in range(11, 125, 16):
                
                self.cell_field[x : x+4, y : y+4, 0] = self.new_cell(self.CANCER)
                

        
        






        