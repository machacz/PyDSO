import parallel
from Pcs64i import Pcs64i

parport = parallel.Parallel()
dso = Pcs64i()
dso.setParallel(parport)

