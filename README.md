# PocketSphinx Speech Recognition

## Installation

1. Deactivate all the virtual environments (including `conda`, `venv`).
2. Clone the repository and change `lm` and `dic` path in file `speech_recognition_working.py` corresponding to the models `7723.lm.bin` and `7723.dic`.
3. Install `pocketsphinx` using `pip install pocketsphinx`. If an error occurs, try by giving `sudo apt-get install libasound2-dev` command.
4. Run `speech_recognition_working.py` file using command `python speech_recognition_working.py`.
5. Speak and enjoy!