import gtts
from playsound import playsound
import speech_recognition as sr
import datetime

listener = sr.Recognizer()
is_awake = False


def talk(text_str):
    try:
        tts = gtts.gTTS(text_str)
        # Save the audio file in the 'voice' directory
        date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
        filename = "voice" + date_string + ".mp3"
        file_path = "voice/" + filename  # Concatenate the directory and filename
        tts.save(file_path)
        playsound(file_path)
    except Exception as e:
        print(e)
        talk("Could you say the command again")


def activate_wake_word():
    global is_awake
    while not is_awake:
        try:
            with sr.Microphone() as source:
                print('Listening for the wake word catalyst...')
                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source, timeout=None)  # No timeout for wake word detection
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'catalyst' in command:  # You can replace 'catalyst' with your desired wake word
                    is_awake = True
                    talk("I'm awake. How can I help you?")
        except Exception as e:
            print(e)


def input_ans():
    try:
        with sr.Microphone() as source:
            print('Listening to your Answer...')
            talk('Listening to your Answer...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            # talk(command)
            try:
                return command
            except Exception as e:
                print(e)
                talk("Can you Please answer again")
                input_ans()

    except Exception as e:
        print(e)
        print("Not able to understand what you said")
        input_ans()


def analyze_mood(feeling, rating):
    # Analyze mood based on provided keywords
    if feeling is None:
        return 'fine'
    # Keywords for each mood category
    bad_keywords = ['anger', 'fear', 'sad', 'tensed', 'stressed']
    good_keywords = ['happy', 'joy', 'satisfied']
    moderate_keywords = ['normal', 'fine', 'okay']

    # Convert user input to lowercase for case-insensitive matching
    feeling_lower = feeling.lower()

    # Check for keywords in the user's feeling
    if any(keyword in feeling_lower for keyword in bad_keywords):
        return 'bad'
    elif any(keyword in feeling_lower for keyword in good_keywords):
        return 'good'
    elif any(keyword in feeling_lower for keyword in moderate_keywords):
        return 'moderate'
    else:
        return 'fine'


def recommend_cbti_tools(keywords):
    recommended_tools = set()

    for keyword in keywords:
        if keyword in ['Grief', 'bad', 'very Low', 'depressed', 'exhausted', 'anxiety', 'stressed']:
            recommended_tools.update([1, 2, 3, 9, 12, 13, 14, 15])
        elif keyword in ['Pain', 'discomfort', 'uneasy']:
            recommended_tools.update([1, 3, 5, 10, 12, 14])
        elif keyword in ['Fear', 'anxious', 'stressed', 'tired']:
            recommended_tools.update([1, 2, 4, 5, 7, 8, 9, 11, 13, 14, 15])
        elif keyword in ['Joy', 'happy', 'peace', 'satisfied', 'content', 'healthy', 'better', 'positive']:
            recommended_tools.update([1, 8, 9, 10, 11])
        elif keyword in ['Neutral', 'nothing', 'normal', 'fine', 'ok', 'good']:
            recommended_tools.update([1, 2, 3, 8, 9, 10, 11, 15])

    display_recommendations(recommended_tools)


def display_recommendations(recommended_tools):
    print('Recommended CBTi tools:')
    talk('Recommended CBTi tools:')
    for tool_id in recommended_tools:
        print(get_cbti_tool_description(tool_id))
        talk(get_cbti_tool_description(tool_id))


def get_cbti_tool_description(tool_id):
    cbti_tool_descriptions = {
        1: "Relaxation techniques: Imagery (visualizations), Progressive muscle relaxation, Autogenic training",
        2: "Cognitive Restructuring: Recognizing and Changing Negative Sleep Thoughts",
        3: "Guided Discovery: Ask questions to understand the issue and emotion deeply",
        4: "Activity Rescheduling and Successive Approximation",
        5: "Journaling: Redirect to journal and scribble section or suggest writing down thoughts",
        6: "Behavioral Experiments",
        7: "Role Playing: Improve problem-solving skills",
        8: "Activity Outside/Involving Members: Playing board games, singing along, sharing stories",
        9: "Joy Journal and Gratitude: Maintain a journal with what makes you happy and 5 things to be grateful for",
        10: "Grounding Techniques: Walk barefoot on grass, look at the sky, use senses",
        11: "Affirmations: Positive self-affirmations",
        12: "Forgiveness Exercise",
        13: "Parts Work: Imaginary exercise of sitting as a middle man and letting all parts with different thoughts be seen",
        14: "Recognition: Repeat lines like 'I recognize I feel...', 'I recognize my need to feel...', etc.",
        15: "Breathing Exercises: Left nostril breathing, deep breath with holding, belly slow deep breath"
    }

    return cbti_tool_descriptions.get(tool_id, "Unknown CBTi Tool")


# # Example usage:
# keywords = ['Grief', 'anxious', 'happy']
# recommend_cbti_tools(keywords)

def sleep_questions():
    # Question 1
    talk('How was your day? Was it Good, Bad, or Okay?')
    answer_1 = input_ans()
    # Analyze the answer_1 (you can use sentiment analysis libraries for more advanced analysis)

    # Question 2
    talk('How are you feeling now?')
    answer_2 = input_ans()
    # Analyze the answer_2 and categorize the mood (e.g., happy, sad, stressed)

    # Question 3
    talk('Can you rate your mood out of 5? 1 is the worst, 5 is great.')
    answer_3 = input_ans()
    # Use answer_3 to determine the mood category (BAD, MODERATE, FINE, GOOD, GREAT)

    # Question 4
    talk('Do you want to do anything about the above feelings? Yes or No.')
    answer_4 = input_ans()
    if 'yes' in answer_4:

        # Implement CBTi activities based on the mood category
        mood_category = analyze_mood(answer_2, answer_3)

        if 'bad' in mood_category:
            recommend_cbti_tools(['Grief', 'bad', 'very Low', 'depressed', 'exhausted', 'anxiety', 'stressed'])

        elif 'moderate' in mood_category:
            recommend_cbti_tools(['low', 'sad', 'fear', 'discomfort', 'negative'])

        elif 'fine' in mood_category:
            recommend_cbti_tools(['normal', 'fine', 'okay', 'good'])

        elif 'good' in mood_category:
            recommend_cbti_tools(['happy', 'joy', 'satisfied', 'better', 'positive'])

        elif 'great' in mood_category:
            recommend_cbti_tools(['joy', 'energetic', 'peace', 'satisfied', 'healthy'])

    else:
        # Recommend relaxing techniques
        talk("'It's okay.Sometimes, taking a break or practicing relaxation techniques can help.")

    # Question 5
    talk('What is happening in your mind and why?')
    answer_5 = input_ans()
    # Process and analyze answer_5

    # Question 6
    talk('What are the 5 things that you are grateful for?')
    answer_6 = input_ans()
    # Process and analyze answer_6

    # Question 7
    talk('Anything you want to share or note?')
    answer_7 = input_ans()
    # Process and analyze answer_7

    # Provide a closing message
    talk('Take care and have a good day!')

    global_ans_dict = {
                        "Answer_1": answer_1,
                        "Answer_2": answer_2,
                        "Answer_3": answer_3,
                        "Answer_4": answer_4,
                        "Answer_5": answer_5,
                        "Answer_6": answer_6,
                        "Answer_7": answer_7
                    }

    return global_ans_dict


def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, timeout=5)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            # talk(command)
            try:
                if 'sleep' in command:
                    data_value  = sleep_questions()

                elif 'time' in command:
                    current_time = datetime.datetime.now().strftime('%I:%M %p')
                    talk('The current time is ' + current_time)

                elif 'date' in command:
                    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
                    talk('Today is ' + current_date)

                elif 'day' in command:
                    current_day = datetime.datetime.now().strftime('%A')
                    talk('Today is ' + current_day)

                elif 'weather' in command:
                    # Add weather API integration or use a weather library to get the current weather
                    talk('I am sorry, I do not have weather information at the moment.')

                elif 'greet' in command:
                    talk('Hello! How can I assist you today?')

                elif 'how are you' in command:
                    talk('I am just a computer program, but thank you for asking!')

                elif "who are you" in command or "define yourself" in command:
                    speak = '''Hello, I am your personal Assistant.
                            I am here to make your life easier. You can command me to perform
                            various tasks. I will also help you to sleep.'''
                    talk(speak)

                elif 'your name' in command:
                    talk('You can call me Catalyst.')

                elif 'shutdown' in command:
                    talk('Goodbye!')

                else:
                    talk("Can you Please ask again")
                    take_command()
            except Exception as e:
                print(e)
                talk("Can you Please ask again")
                take_command()

    except Exception as e:
        print(e)
        print("Not able to understand what you said")


if __name__ == "__main__":
    talk("Hi, Your personal Voice Assistant is Turned ON")

    while True:
        if not is_awake:
            activate_wake_word()
        else:
            take_command()
            is_awake = False
