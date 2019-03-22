"imports and definitions shared by various defs files"

import numpy as np

try:
	from hyperopt import hp
	from hyperopt.pyll.stochastic import sample
except ImportError:
	print ("In order to achieve operational capability, this programme requires hyperopt to be installed (pip install hyperopt), unless you make get_params() use something else.")
	
#	

# handle floats which should be integers
# works with flat params
def handle_integers( params ):

	new_params = {}
	for k, v in params.items():
		if type( v ) == float and int( v ) == v:
			new_params[k] = int( v )
		else:
			new_params[k] = v
	
	return new_params
	
###


