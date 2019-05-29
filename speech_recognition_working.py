# import os
# from pocketsphinx import LiveSpeech, get_model_path

# model_path = get_model_path()
# print (model_path)

# # from pocketsphinx import LiveSpeech

# for phrase in LiveSpeech(): print(phrase)

import os
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()

# speech = LiveSpeech(
#     verbose=False,
#     sampling_rate=16000,
#     buffer_size=2048,
#     no_search=False,
#     full_utt=False,
#     hmm=os.path.join(model_path, 'en-us'),
#     lm=os.path.join('/home/pocketsphinx', '7723.lm'),
#     dic=os.path.join('/home/pocketsphinx', '7723.dic')
# )

speech = LiveSpeech(
    sampling_rate=16000,
    hmm=os.path.join(model_path, 'en-us'),
    lm='/home/dasun/Documents/FYPpocketsphinx_python/7723.lm.bin',
    dic='/home/dasun/Documents/FYPpocketsphinx_python/7723.dic'
)

for phrase in speech:
    print(phrase)