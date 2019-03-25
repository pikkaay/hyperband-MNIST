import tensorflow as tf
from tefla.core.lr_policy import StepDecayPolicy

cnf = {
    'multilabel': True,
    # 'classification':True,
    # 'validation_scores': [('validation accuracy', util.accuracy_wrapper), ('validation kappa', util.kappa_wrapper)],
    'validation_scores': [('accuracy', tf.contrib.metrics.f1_score)],
    'num_epochs': 20,
    'lr_policy': StepDecayPolicy(
        schedule={
            0: 0.01,
            10: 0.003,
            90: 0.0003,
            110: 0.003,
            120: 0.0003,
            200: 0.00003,
        }
    ),

    'batch_size_train':
      16,
    'batch_size_test':
    16,
    'aug_params': {
        'zoom_range': (1 / 1.15, 1.15),
        'rotation_range': (0, 0),
        'shear_range': (0, 0),
        'translation_range': (0, 0),
        'do_flip': False,
        'allow_stretch': False,
    },
    'input_size': (28,28,3),

    }
