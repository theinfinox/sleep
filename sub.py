from textblob import TextBlob
# import speech_recognition as sr
# import pyttsx3
# # from main import global_dict
#
#
# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
def senti(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    dict={"polarity":sentiment.polarity,"subjectivity":sentiment.subjectivity}
    return dict

# def talksub(text):
#     engine.say(text)
#     engine.runAndWait()

# def take_command_s():
#     try:
#         with sr.Microphone() as source:
#             print('listening...')
#             listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
#             voice = listener.listen(source, timeout=5)  # Set a timeout for listening
#             command = listener.recognize_google(voice)
#             command = command.lower()
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return ""
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")
#         return ""
#     return command
def wordfind(text):
    if 'good' or 'great' in text:
        if 'not' in text:
            return 'bad'
        else:
            return 'good'
    elif 'okay' or 'ok' in text:
        return 'ok'
    else:
        return 'bad'

def feelfind(text):
    feelings = ["anger", "fear", "sad", "happy", "good", "bad", "ok", "okay", "fine", "great", "fun", "low", "depressed" ]
    feelingsList = []
    words_in = text.split()
    for i in words_in:
        if i in feelings:
            feelingsList.append(i)
    return feelingsList
def analyze_mood(text):
    if 'one' in text:
        return "bad"
    elif 'two' in text:
        return "moderate"
    elif 'three' in text:
        return "fine"
    elif 'four' in text:
        return "good"
    elif 'five' in text:
        return "great"

def yes_no(text):
    if 'yes' in text:
        return 'yes'
    elif 'no' in text:
        return 'no'
    else:
        return 'repeat'
        # talksub('Yes or No answer will be much easy to understand')
        # talksub('Do you want to do anything about the above feelings?')
        # a4 = take_command_s()
        # global_dict["ans4"] = a4
        # yes_no(a4)
