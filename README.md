# PocketSphinx Speech Recognition

## Installation

1. Set up wheel and upgrade/install `pocketsphinx` using the following commands.

`python -m pip install --upgrade pip setuptools wheel` and
`pip install --upgrade pocketsphinx`.

2. Install [pocketspinx]((https://anaconda.org/jiayi_anaconda/pocketsphinx)) in the conda environment, by using `conda install -c jiayi_anaconda pocketsphinx `
3. Clone the repository and change `lm` and `dic` path in file `speech_recognition_working.py` corresponding to the models `7723.lm.bin` and `7723.dic`.
4. Run `speech_recognition_working.py` file using command `python speech_recognition_working.py`.
5. Speak and enjoy!