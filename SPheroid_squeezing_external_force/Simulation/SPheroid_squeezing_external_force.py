
from cc3d import CompuCellSetup
        

from SPheroid_squeezing_external_forceSteppables import SPheroid_squeezing_external_forceSteppable

CompuCellSetup.register_steppable(steppable=SPheroid_squeezing_external_forceSteppable(frequency=1))


CompuCellSetup.run()
