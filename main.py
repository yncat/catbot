import time
import pyaudio
import audioPlayer
import audioRecorder
import brain
import gcpGlobal
import speechRecognizer
import speechSynthesizer

gcp = gcpGlobal.GCPGlobal("speech_key.json", "en-US")
p = pyaudio.PyAudio()
player = audioPlayer.AudioPlayer()
recorder = audioRecorder.AudioRecorder(p)
recognizer = speechRecognizer.SpeechRecognizer(gcp)
synthesizer = speechSynthesizer.SpeechSynthesizer(p, gcp, "en-US-Wavenet-F")
brain = brain.EnglishBrain()

while(True):
    player.playStartSound()
    bin = recorder.record()
    player.playStopSound()
    rstr = recognizer.recognize(bin, 44100)
    response, should_exit = brain.respondTo(rstr)
    synthesizer.synthesize(response)
    if should_exit:
        break

p.terminate()
