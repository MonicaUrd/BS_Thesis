
from cc3d import CompuCellSetup
        

from Contact_energy_psSteppables import Contact_energy_psSteppable

CompuCellSetup.register_steppable(steppable=Contact_energy_psSteppable(frequency=1))


CompuCellSetup.run()
