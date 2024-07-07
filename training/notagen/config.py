import os

KEY_AUGMENT = True
if KEY_AUGMENT:
    DATA_FOLDER = "/22A052/multitrackComposer-data/10_abc_rotated"
else:
    DATA_FOLDER = "/22A052/multitrackComposer-data/07_abc_rotated_CLAMP"
DATA_DUPLICATION_INDEX_PATH = "/22A052/multitrackComposer-data/08_abc_deduplicated/04_duplicated_files_imsleeping_tchai.jsonl"
DATA = os.path.splitext(os.path.split(DATA_DUPLICATION_INDEX_PATH)[-1])[0][len('04_duplicated_files_'):]

EVAL_SPLIT = 0.01

PATCH_DECODER_STRUCTURE = 'llama'    # 'llama'
BYTE_DECODER_STRUCTURE  = 'gpt2'    # 'llama'

# Configuration for the model
PATCH_MODE = 'barbyte'
PATCH_STREAM = True
PATCH_SIZE = 16                                                 # Patch Size
PATCH_LENGTH = 1024                                             # Patch Length

BYTE_NUM_LAYERS = 3                                             # Number of layers in the decoder
PATCH_NUM_LAYERS = 9                                           # Number of layers in the encoder
HIDDEN_SIZE = 768                                               # Hidden Size

# Configuration for the training
NUM_EPOCHS = 64                                                 # Number of epochs to train for (if early stopping doesn't intervene)
LEARNING_RATE = 1e-5                                            # Learning rate for the optimizer
BATCH_SIZE = 1                                                  # Batch size for training
ACCUMULATION_STEPS = 1                                          # Accumulation steps to simulate large batch size
PATCH_SAMPLING_BATCH_SIZE = 0                                   # Batch size for patch during training, 0 for full conaudio
LOAD_FROM_CHECKPOINT = False                                    # Whether to load weights from a checkpoint
LOAD_FROM_PRE_CHECKPOINT = False                                 # Whether to load pre-trained weights from a checkpoint
WANDB_LOGGING = True                                           # Whether to log to wandb

PRETRAINED_PATH = "weights_bgpt_llama_llama_musescore+midi_keyaugment_True_patchilizer_barbyte_stream_True_p_size_16_p_length_1024_p_layers_9_h_size_768_lr_0.0002_batch_20.pth" # Path to the pretrained weights
WEIGHTS_PATH = "weights_bgpt_" + PATCH_DECODER_STRUCTURE + \
                "_" + BYTE_DECODER_STRUCTURE + \
                '_' + DATA + \
                '_keyaugment_' + str(KEY_AUGMENT) + \
                "_patchilizer_" + PATCH_MODE + \
                "_stream_" + str(PATCH_STREAM) + \
                "_p_size_" + str(PATCH_SIZE) + \
                "_p_length_" + str(PATCH_LENGTH) + \
                "_p_layers_" + str(PATCH_NUM_LAYERS) + \
                "_h_size_" + str(HIDDEN_SIZE) + \
                "_lr_" + str(LEARNING_RATE) + \
                "_batch_" + str(BATCH_SIZE) + ".pth"                 # Path to save weights
LOGS_PATH = "logs_bgpt_" + PATCH_DECODER_STRUCTURE + \
            "_" + BYTE_DECODER_STRUCTURE + \
            '_' + DATA + \
            '_keyaugment_' + str(KEY_AUGMENT) + \
            "_patchilizer_" + PATCH_MODE + \
            "_stream_" + str(PATCH_STREAM) + \
            "_p_size_" + str(PATCH_SIZE) + \
            "_p_length_" + str(PATCH_LENGTH) + \
            "_p_layers_" + str(PATCH_NUM_LAYERS) + \
            "_h_size_" + str(HIDDEN_SIZE) + \
            "_lr_" + str(LEARNING_RATE) + \
            "_batch_" + str(BATCH_SIZE) + ".txt"                     # Path to save logs
WANDB_NAME = PATCH_DECODER_STRUCTURE + \
            "_" + BYTE_DECODER_STRUCTURE + \
            '_' + DATA + \
            '_keyaugment_' + str(KEY_AUGMENT) + \
            "_patchilizer_" + PATCH_MODE + \
            "_stream_" + str(PATCH_STREAM) + \
            "_p_size_" + str(PATCH_SIZE) + \
            "_p_length_" + str(PATCH_LENGTH) + \
            "_p_layers_" + str(PATCH_NUM_LAYERS) + \
            "_h_size_" + str(HIDDEN_SIZE) + \
            "_lr_" + str(LEARNING_RATE) + \
            "_batch_" + str(BATCH_SIZE)


# Configuration for inference
INFERENCE_WEIGHTS_PATH = WEIGHTS_PATH               # Path to weights for inference# Folder to save output files
TARGET_EXT = "abc"                                              # Target extension for inference
NUM_SAMPLES = 100                                               # Number of samples to generate (only for generate mode)
TOP_K = 0                                                       # Top k for sampling
TOP_P = 1                                                      # Top p for sampling
TEMPERATURE = 1.2                                                 # Temperature for sampling
# OUTPUT_FOLDER  = "output/bgpt_pretrain_musescore_v240612_deduplicated" + '_k_' + str(TOP_K) + '_p_' + str(TOP_P) + '_temp_' + str(TEMPERATURE)
OUTPUT_FOLDER = os.path.join('output', os.path.splitext(INFERENCE_WEIGHTS_PATH)[0] + '_k_' + str(TOP_K) + '_p_' + str(TOP_P) + '_temp_' + str(TEMPERATURE))
                                                                                   
