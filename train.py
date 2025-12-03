# AWS SageMaker 
import os 


SM_MODEL_DIR=os.environ.get('SM_MODEL_DIR', ".")
SM_CHANNEL_TRAINING=os.environ.get('SM_CHANNEL_TRAINING', "./data/training")
SM_CHANNEL_VALIDATION=os.environ.get('SM_CHANNEL_VALIDATION',"./data/validation")
SM_CHANNEL_TESTING=os.environ.get('SM_CHANNEL_TESTING',"./dtata/testing")