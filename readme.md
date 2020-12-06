# catbot

You can talk to this bot. its brain is customisable. Have fun.

## setup

pip install -r requirements.txt

Additionally, if you're using windows, you must manually download pyaudio whl from here:

https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

## Google credentials setup

You must get your own key info from Google Cloud Platform. Once got it, place the JSON as speech_key.json in the repo directory (git ignored).

Your key must have access to Google Cloud text-to-speech and speech-to-text API's.

## Usage

- Run main.py
- Talk to the bot
- Have fun
- say bye to quit
- customize the brain
- Have some more fun

# Run brain test

Make sure brains work correctly. Run unittest discover brain to run tests. I strongly recommend writing tests for every response of your customized brain.
