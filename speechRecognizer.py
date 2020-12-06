from google.cloud import speech as speechtotext
import wave


class SpeechRecognizer:
    def __init__(self, gcp):
        self.gcp = gcp
        self.client = speechtotext.SpeechClient()

    def recognize(self, bin, sample_rate_hertz):
        audio = speechtotext.RecognitionAudio(content=bin)
        config = speechtotext.RecognitionConfig(
            encoding=speechtotext.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate_hertz,
            language_code=self.gcp.getLanguageCode(),
        )
        response = self.client.recognize(config=config, audio=audio)

        words = []
        for elem in response.results:
            words.append(elem.alternatives[0].transcript)
        # end append
        return " ".join(words)
