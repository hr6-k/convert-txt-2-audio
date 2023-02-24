import pyttsx3

# in windows;
# if u receive error such as no module named win32com.client,
# no module named win32, or no module named win32api, u just need to additionally install pypiwin32


# to create the actual text to a audio class, we make this class
class TextToSpeech:
    #its going to require an engine and that is going to be pyttsx3 dot engine
    engine: pyttsx3.Engine

    # net we need to cret an initializer
    # and creat some variable such as the voice that we want to use
    # and the rate at which we want to speak
    # and also the volume of the output audio which will be of type float
    def __init__(self, voice, rate: int, volume: float):
        # now the self dot engine is going to be equel to pyttsx3 dot initialize 
        self.engine = pyttsx3.init()
        # and if we want to change the default voice, we will just go ahead and say
        # if there is a voice
        if voice:
            # then we go ahead and call engine 
            # so slef dot engine, set property. and we want to set the voice(first voice), with the voice property (the second one) that we have selected
            self.engine.setProperty("voice", voice)
            # then we go ahead and call the engine again, and we are going to set the property for the rate
            self.engine.setProperty("rate", rate)
            # and also for the volume
            self.engine.setProperty("volume", volume)

    # to understand what type od the voices u have available in ur computer
    # to make it easier to understand, we r going to create a function that will list the available voices
    def list_available_voices(self):
        # and the voices are going to be type list, which is going to equel an array of self dot engine dot get property, and we r going to get the voices
        voices: list = [self.engine.getProperty("voices")]
        
        # no we are going to get all the elements inside this array
        for i, voice in enumerate(voices[0]):
            # lets go ahead and list those 
            # so lets print a formated string with i plus one, and we insert the voice name and also the voice dot age
            # and what we are going to do next, after the colone, lets get the voice dot languages at the index of zero, the voice dot gender and we also want to get the id
            # so in the end inside we create some square brackets, and some curly brackets, we are going to get the voice dot id
            # we need this voice dot id, this is going to be passed inside the initializer (above method) when we actually select a voice
            print(f"{i + 1} {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [{voice.id}]")
            ############################### test ######################
            # with this done, lets go ahead and see what voices we have, go to section 1 
            #############################

    # now after test section 1, we are coming back inside our speech class and we r going to creat another function
    # function text to speech, which is going to take a text of type string, followed by, whether we should save it or not, it is going to be false initially
    # and we want to take a file name, and the file name is going to have a default value output.mp3
    def text_to_speech(self, text: str, save: bool = False, file_name = "output.mp3"):
        # so first we r going ahead and call the engine
        # and we are going to say that we want to say the following text, inside the parentheses, we are going to pass the text we want it to say
        self.engine.say(text)
        # and we are also going to print, that engine is speaking
        print("I am speaking...")


        # and if save is set to True, ofcourse we are going ahead and save it in an audio file
        if save:
            # in parentheses means:  we want to save the following text, to the output file which is the file_name
            self.engine.save_to_file(text, file_name)

        # and to make this whole works, we need to call the engine 1 more time and say we want to run it and we want to wait 
        self.engine.runAndWait()




############ test section 1 ############################
"""
if __name__ == "__main__":
    # we are going to create an object of our Texttospeech class, tts (text to speech)
    # we r going to pass just None for now, since we have no voices to show, and rate gonna be 200 which is just the default, and 1.0 which is max volume
    tts = TextToSpeech(None, 200, 1.0)
    # and go ahead and say; tts, list all of available voices
    tts.list_available_voices() # when we run this programm, we should get a lot of different voices here
"""
#  I had some error to see all the voices, I had to open a py file in pyttxs3 package and delete a line
# infos are here: 
# https://stackoverflow.com/questions/74668118/voiceage-error-while-using-pyttsx3-module-to-add-voice-to-statements
# https://github.com/nateshmbhat/pyttsx3/issues/248

# I have done that and successsfuly could see the available languages in my mac

#there gonna be a lot of voice printed like this; 111 Sandy (English (UK)) None: en_GB (VoiceGenderNeuter) [com.apple.eloquence.en-GB.Sandy]
# I just take this part from inside the square brackets and continue :   com.apple.eloquence.en-GB.Sandy
# com.apple.eloquence.en-GB.Sandy
# or
# com.apple.speech.synthesis.voice.daniel.premium

################### end of test section 1 ########################


# tozihate in khotoute payin dakhele test section 1 neveshtast ghablan, faghat ye khatte jadid dare inja
if __name__ == "__main__":
    # à this is what we got after test section 1 , and we insert it instead of None
    # if u play with None, it is going to say that with my mac default voice
    # I am decreasing the pace from 200 to 170, to read that in a good pace
    tts = TextToSpeech("com.apple.speech.synthesis.voice.daniel.premium", 170, 1.0)
    # we dont need this line, that is just for test section 1
    # tts.list_available_voices() 
    # this is the new line we want, in parentheses, we give the text as str and when u run the program, it will go to read it for u
    tts.text_to_speech("Hello there! I am pythonize!")