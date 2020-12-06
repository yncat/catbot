import io
import pyaudio
import wave
import audioop
import time

RMS_THRESHOLD = 2000
SILENCE_TIME_THRESHOLD = 2.0
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"


class AudioRecorder:
    def __init__(self, pyaudio):
        self.p = pyaudio

    def record(self):
        stream = self.p.open(format=FORMAT,
                             channels=CHANNELS,
                             rate=RATE,
                             input=True,
                             frames_per_buffer=CHUNK)
        frames = []
        talking = False
        talked = False
        silence_started = time.time()

        while True:
            data = stream.read(CHUNK)
            frames.append(data)
            rms = audioop.rms(data, 2)
            if rms >= RMS_THRESHOLD and not talking:
                talking = True
                talked = True
            # end talking on
            if rms < RMS_THRESHOLD and talking:
                talking = False
                silence_started = time.time()
            # end talking
            if talked and not talking and time.time()-silence_started > SILENCE_TIME_THRESHOLD:
                break
        # end process signal
        stream.stop_stream()
        stream.close()
        bin = io.BytesIO()
        bin.seek(0)
        wf = wave.open(bin, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        bin.seek(0)
        ret = bin.read()
        bin.close()
        return ret
