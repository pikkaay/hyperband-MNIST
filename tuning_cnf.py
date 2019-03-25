from hyperopt import hp

cnf = {
  'batch_size_train': hp.choice( 'bs', (16,32,64,128,256)),
  'batch_size_test': hp.choice( 'bs', (16,32,64,128,256)),
}