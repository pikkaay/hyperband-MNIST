from hyperopt.pyll.stochastic import sample
import importlib


class defs:
  def __init__(self, tuning_cnf):
    self.tuning_cnf = tuning_cnf
  
  def get_params(self):
    params = sample( self.tuning_cnf)
    return self.handle_integers(params)

  @staticmethod
  def handle_integers(params):
    new_params = {}
    for k, v in params.items():
      if type( v ) == float and int( v ) == v:
        new_params[k] = int( v )
      else:
        new_params[k] = v
    return new_params
  
  @staticmethod
  def load_module(mod):
    print('static call')
    return importlib.import_module(mod.replace('/', '.').split('.py')[0])