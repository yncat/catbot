from google.cloud import texttospeech
import io
import wave


class SpeechSynthesizer:
    def __init__(self, pyaudio, gcp, voice_name):
        self.p = pyaudio
        self.gcp = gcp
        self.voice_name = voice_name
        self.client = texttospeech.TextToSpeechClient()

    def synthesize(self, text):
        voice = texttospeech.VoiceSelectionParams(
            language_code=self.gcp.getLanguageCode(),
            name=self.voice_name,
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        )
        input_text = texttospeech.SynthesisInput(text=text)
        response = self.client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config)
        bin = io.BytesIO(response.audio_content)
        wf = wave.open(bin, "rb")
        stream = self.p.open(
            format=self.p.get_format_from_width(
                wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)
        chunk = 1024
        data = wf.readframes(chunk)
        while data:
            stream.write(data)
            data = wf.readframes(chunk)
        # end play
        stream.close()
