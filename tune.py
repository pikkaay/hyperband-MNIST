from hyperband import Hyperband
# from try_config import try_config
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', default='path/to/model', 
    help='Relative path to model.')
parser.add_argument('--training_cnf', default=None, 
    help='Relative path to training config file.')
parser.add_argument('--tuning_cnf', default=None, 
    help='Relative path to tuning config file.')
parser.add_argument('--data_dir', default=None, 
    help='Path to training directory.')
parser.add_argument('--parallel', default=True, 
    help='parallel or queued.')
parser.add_argument('--start_epoch', default=1, 
    help='Epoch number from which to resume training.')
parser.add_argument('--num_classes', default=5, 
    help='Number of classes to use for training.')
parser.add_argument('--gpu_memory_fraction', default=0.92, 
    help='Epoch number from which to resume training.')
parser.add_argument('--weights_from', default=None, 
    help='Path to initial weights file.')
parser.add_argument('--weights_dir', default=None, 
    help='Path to save weights file.')
parser.add_argument('--resume_lr', default=0.01, 
    help='Path to initial weights file.')
parser.add_argument('--loss_type', default='cross_entropy', 
    help='Loss fuction type.')
parser.add_argument('--weighted', default=False, 
    help='Whether to use weighted loss.')
parser.add_argument('--log_file_name', default='train_seg.log', 
    help='Log file name.')
parser.add_argument('--is_summary', default=False, 
    help='Path to initial weights file.')

args = parser.parse_args()

print(type(args))

hb = Hyperband(get_params, args)
hb.run_test