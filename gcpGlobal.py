import os


class GCPGlobal:
    def __init__(self, key_file_name, language_code):
        self.language_code = language_code
        if not os.path.exists(key_file_name):
            raise SystemError("%s not found" % key_file_name)
            return
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.abspath(
            key_file_name)

    def getLanguageCode(self):
        return self.language_code
