from . import base
import re
from utils import multiReplace

class EnglishBrain(base.BrainBase):
    def __init__(self):
        base.BrainBase.__init__(self)
        self.basic_responses = {
            "hello": "Hello.",
            "(what is)|(what's) your name": "My name is Jane Doe. The stupid developer didn't give me a name. I hate him.",
            "do you think (that )?cats are cute": "Yes! I absolutely agree!",
            "do you think (that )?dogs are cute": "Oh. Yeah. I, agree. I'm not lying. You know.",
        }
        self.exit_responses = {
            "bye": "Bye for now.",
        }

    def respondTo(self, text):
        text = text.lower()
        # basic responses
        for k, v in self.basic_responses.items():
            if re.match(re.compile(k), text):
                return v, False
            # end return response
        # end basic responses

        # exit responses
        for k, v in self.exit_responses.items():
            if re.match(re.compile(k), text):
                return v, True
            # end return response
        # end basic responses

        # my name is
        m = re.match("my name is (.+)", text)
        if m:
            return "Nice to meet you %s." % m.group(1), False
        # end my name is

        # say
        m = re.match("say (that )*(.+)", text)
        if m:
            return m.group(2), False
        # end say
        # can you
        m = re.match("can you (.+)", text)
        if m:
            newstr = multiReplace.multiReplace(m.group(1), {"your": "my", "yourself": "myself"})
            return "i can't %s" % newstr, False
        # end can you
        return "Sorry. I don't understand.", False
