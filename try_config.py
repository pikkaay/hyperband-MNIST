# -------------------------------------------------------------------#
# Tool to train on images
# Contact: mrinalhaloi11@gmail.com
# Copyright 2018 The Tefla Authors. All Rights Reserved.
# -------------------------------------------------------------------#
from __future__ import division, print_function, absolute_import

import click
import numpy as np

np.random.seed(127)
import tensorflow as tf

tf.set_random_seed(127)

from tefla.core.dir_dataset import DataSet
from tefla.core.iter_ops import create_training_iters
from tefla.core.learning_hb import SupervisedLearner
from tefla.da.standardizer import NoOpStandardizer
from tefla.utils import util
from hyperband import Hyperband


# pylint: disable=no-value-for-parameter





def try_config(n_iterations, t, args):

  # model, training_cnf, data_dir, parallel, start_epoch, weights_from, weights_dir, resume_lr,
         # gpu_memory_fraction, num_classes, is_summary, loss_type, weighted, log_file_name
  
  print(args.model)
#   model_def = util.load_module(model)
#   model = model_def.model
#   cnf = util.load_module(training_cnf).training_cnf
# # call tuning cnf and call hyperband
#   tuning_cnf = util.load_module(training_cnf).tuning_cnf




  # if weights_from:
  #   weights_from = str(weights_from)

  # data_set = DataSet(
  #     data_dir,
  #     model_def.image_size[0],
  #     mode=cnf.get('mode'),
  #     multilabel=cnf.get('multilabel', False))
  # standardizer = cnf.get('standardizer', NoOpStandardizer())
  # cutout = cnf.get('cutout', None)

  # training_iter, validation_iter = create_training_iters(
  #     cnf,
  #     data_set,
  #     standardizer,
  #     model_def.crop_size,
  #     start_epoch,
  #     parallel=parallel,
  #     cutout=cutout,
  #     data_balancing=cnf.get('data_balancing', False))
  # learner = SupervisedLearner(
  #     model,
  #     cnf,
  #     training_iterator=training_iter,
  #     validation_iterator=validation_iter,
  #     resume_lr=resume_lr,
  #     classification=cnf['classification'],
  #     gpu_memory_fraction=gpu_memory_fraction,
  #     num_classes=num_classes,
  #     is_summary=is_summary,
  #     loss_type=loss_type,
  #     weighted=weighted,
  #     log_file_name=log_file_name)
  
  # loss = learner.fit(data_set, weights_from, start_epoch=start_epoch, weights_dir=weights_dir, summary_every=399)
  
  # return {'loss': 'will update'}

