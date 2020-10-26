'''
    chatbot.py
    
    This file tests all methods in chatbot.py.
'''

import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
import unittest
import chatbot
import app

KEY_INPUT = "arg1"
KEY_INPUT2 = "arg2"
KEY_EXPECTED = "expected"
KEY_MESSAGE = "message"
KEY_USER = "user"
KEY_PFP = "pfp_url"

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!! about",
                KEY_INPUT2: "",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Hi I'm a bot! I may be primitive, but I'm trying my best. My about command tells you about me, you can use funtranslate to do some weird translations, I can tell dad jokes, and give you specific anime information with !! anime {your_anime}",
                    KEY_USER: "Bot",
                    KEY_PFP: "<img src=" + "\"./botpfp.png\">",
                }
            },
            {
                KEY_INPUT: "!! help", 
                KEY_INPUT2: "",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Here are all the commands I know: about, funtranslate, dad, and anime.",
                    KEY_USER: "Bot",
                    KEY_PFP: "<img src=" + "\"./botpfp.png\">",
                }
            },
            {
                KEY_INPUT: "!! FWEVWIO", 
                KEY_INPUT2: "",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "Sorry, I didn't understand that command.",
                    KEY_USER: "Bot",
                    KEY_PFP: "<img src=" + "\"./botpfp.png\">",
                }
            },
            {
                KEY_INPUT: "https://www.clipartkey.com/mpngs/m/235-2358752_poggers-emote-clipart-png-download-transparent-background-poggers.png", 
                KEY_INPUT2: "https://www.clipartkey.com/mpngs/m/235-2358752_poggers-emote-clipart-png-download-transparent-background-poggers.png",
                KEY_EXPECTED: {
                    KEY_MESSAGE: "<img src=" + "\"" + "https://www.clipartkey.com/mpngs/m/235-2358752_poggers-emote-clipart-png-download-transparent-background-poggers.png" + "\">",
                    KEY_USER: "Bot",
                    KEY_PFP: "<img src=" + "\"./botpfp.png\">",
                }
            },
            
        ]
        
        self.failure_test_params = [
            # TODO HW13
        ]


    def test_bot_parse_message_success(self):
        for test in self.success_test_params[0:4]:
            response = chatbot.CoolBot().isCommand(test[KEY_INPUT], test[KEY_INPUT2])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response[KEY_MESSAGE], expected[KEY_MESSAGE])
            self.assertEqual(response[KEY_USER], expected[KEY_USER])
            self.assertEqual(response[KEY_PFP], expected[KEY_PFP])
            
    def test_parse_message_failure(self):
        for test in self.failure_test_params:
            print("Test")
            
class ImageTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: ["Hi!", "I", "Said", "https://www.clipartkey.com/mpngs/m/235-2358752_poggers-emote-clipart-png-download-transparent-background-poggers.png"], 
                KEY_INPUT2: [],
                KEY_EXPECTED: True
            },
        ]
        
        self.failure_test_params = [
        ]
            
    def test_check_img_success(self):
        for test in self.success_test_params:
            response = app.check_images(test[KEY_INPUT], test[KEY_INPUT2])
            expected = test[KEY_EXPECTED]
            self.assertEqual(response, expected)
                
if __name__ == '__main__':
    unittest.main()