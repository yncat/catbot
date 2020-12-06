import unittest
from brain.english import EnglishBrain


class TestEnglish_basicResponses(unittest.TestCase):
    def test_greetings(self):
        brain = EnglishBrain()
        self.assertEqual(brain.respondTo("hello"),
                         ("Hello.", False))
        self.assertEqual(brain.respondTo("Hello"),
                         ("Hello.", False))
        self.assertEqual(
            brain.respondTo("what is your name"),
            ("My name is Jane Doe. The stupid developer didn't give me a name. I hate him.",
             False))
        self.assertEqual(
            brain.respondTo("what's your name"),
            ("My name is Jane Doe. The stupid developer didn't give me a name. I hate him.",
             False))

    def test_regexpAnimals(self):
        brain = EnglishBrain()
        self.assertEqual(
            brain.respondTo("do you think that cats are cute"),
            ("Yes! I absolutely agree!",
             False))
        self.assertEqual(brain.respondTo(
            "do you think cats are cute"), ("Yes! I absolutely agree!", False))
        self.assertEqual(
            brain.respondTo("do you think that dogs are cute"),
            ("Oh. Yeah. I, agree. I'm not lying. You know.",
             False))
        self.assertEqual(
            brain.respondTo("do you think dogs are cute"),
            ("Oh. Yeah. I, agree. I'm not lying. You know.",
             False))


class TestEnglish_exitResponses(unittest.TestCase):
    def test_greetings(self):
        brain = EnglishBrain()
        self.assertEqual(brain.respondTo("bye"),
                         ("Bye for now.", True))


class TestEnglish_myNameIs(unittest.TestCase):
    def TestEnglish_myNameIs(self):
        brain = EnglishBrain()
        self.assertEqual(brain.respondTo("my name is cat"),
                         ("Nice to meet you cat.", False))
        self.assertEqual(brain.respondTo(
            "say that i am a hero"), ("i am a hero", False))


class TestEnglish_say(unittest.TestCase):
    def TestEnglish_say(self):
        brain = EnglishBrain()
        self.assertEqual(brain.respondTo("say i am a hero"),
                         ("i am a hero", False))
        self.assertEqual(brain.respondTo(
            "say that i am a hero"), ("i am a hero", False))


class TestEnglish_canYou(unittest.TestCase):
    def TestEnglish_CanYou(self):
        brain = EnglishBrain()
        self.assertEqual(
            brain.respondTo("can you destroy the world"),
            ("I can't destroy the world.",
             False))
