# Old functions cleaning up Default_Functions
from gtts import gTTS
import pyttsx3
import speech_recognition as sr
from PyQt5.QtWidgets import *
import csv

# Initialize the recognizer
recognizer = sr.Recognizer()
r = sr.Recognizer()

# Defining file name
filename = "reminder.csv"
path = f'./{filename}'

# create_csv_file with checks
def create_csv_file():
    # Defining file name
    path = './CPU.csv'

    check_file = os.path.isfile(path)

    if check_file:
        write_log(Message='CPU.csv already exist', FuncName='create_csv_file', ErrorType='Info')
        return 0
    else:
        try:
            write_log(Message='Creating file CPU.csv', FuncName='create_csv_file', ErrorType='Info')
            with open('CPU.csv', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["CPU", "AVG Usage", "Number Of Cores"])
            return 0
        except Exception as e:
            write_log(Message='Error Creating file ' + str(e), FuncName='create_csv_file', ErrorType='Critical')
        return 2


# Writing to a CSV File with checks
def write_to_csv(filename, coldata):
    CSVFILE = create_csv_file()

    if CSVFILE == 0:
        try:
            write_log(Message='Opening file CPU.csv', FuncName='write_to_csv', ErrorType='Info')
            with open(f'{filename}', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([f"{coldata}"])
        except Exception as e:
            write_log(Message='Error Opening file ' + str(e), FuncName='write_to_csv', ErrorType='Critical')
    elif CSVFILE == 2:
        write_log(Message='Error Opening file ' + str(), FuncName='write_to_csv', ErrorType='Critical')


def check_create_reminder_file():
    # checking file and creating it if needed
    check_reminder_csv = os.path.isfile(path)

    if check_reminder_csv:
        write_log(Message=f'{filename} already exist', FuncName='check_write_create_reminder_csv', ErrorType='Info')
        return 0
    else:
        try:
            write_log(Message=f'Creating file{filename}', FuncName='check_write_create_reminder_csv', ErrorType='Info')
            with open(f'{filename}', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(["Index", "Task", "Time", "Date", "Status"])
            return 0
        except Exception as e:
            write_log(Message='Error Creating file ' + str(e), FuncName='check_write_create_reminder_csv', ErrorType='Critical')
        return 2


def write_reminder_file(coldata):
    csv_file = check_create_reminder_file()

    if csv_file == 0:
        try:
            write_log(Message='Opening file CPU.csv', FuncName='write_to_csv', ErrorType='Info')
            with open(f'{filename}', 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([f"{coldata}"])
        except Exception as e:
            write_log(Message='Error Opening file ' + str(e), FuncName='write_to_csv', ErrorType='Critical')
    elif csv_file == 2:
        write_log(Message='Error Opening file ' + str(), FuncName='write_to_csv', ErrorType='Critical')


# Creates mp3 for speech
def text_to_speech(text):
    write_log(Message='Starting text_to_speech Functions', FuncName='text_to_speech', ErrorType='Info')
    # Initialize gTTS with the text to convert
    speech = gTTS(text)

    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)

    # Play the audio file
    os.system('afplay ' + speech_file)
    write_log(Message='Closing text_to_speech Functions', FuncName='text_to_speech', ErrorType='Info')


def record_audio():
    write_log(Message='Starting record_audio Functions', FuncName='record_audio', ErrorType='Info')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        print(f"🤪 Listening...")
        text_to_speech(text="I'm Listening...")
        audio = r.listen(source=source)
    write_log(Message='Closing record_audio Functions', FuncName='record_audio', ErrorType='Info')
    return audio


def recognize_speech(audio):
    write_log(Message='Starting recognize_speech Functions', FuncName='recognize_speech', ErrorType='Info')
    try:
        text = recognizer.recognize_google(audio)
        print(f"🤪 You said: {text}")
        write_log(Message='Closing recognize_speech Functions', FuncName='recognize_speech', ErrorType='Info')
        return text
    except sr.UnknownValueError:
        print(f"🤪 Sorry, I couldn't understand that.")
        text = "Sorry, I couldn't understand that."
        write_log(Message='Closing recognize_speech Functions', FuncName='recognize_speech', ErrorType='Error')
        return text
    except sr.RequestError:
        print(f"🤪 Sorry, there was an error processing your request.")
        text = "Sorry, there was an error processing your request."
        write_log(Message='Closing recognize_speech Functions', FuncName='recognize_speech', ErrorType='Critical')
        return text


def get_speech():
    write_log(Message='Starting get_speech Functions', FuncName='get_speech', ErrorType='Info')
    # Getting speech instead of having to type to Lucy
    audio = record_audio()
    query = recognize_speech(audio)
    write_log(Message='Closing get_speech Functions', FuncName='get_speech', ErrorType='Info')
    return query


# Lucy function with Training
def lucy():
    write_log(Message='Starting Lucy Functions', FuncName='Lucy', ErrorType='Info')
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
    from chatterbot.trainers import ChatterBotCorpusTrainer

    chatbot = ChatBot(
        "Lucy",
        storage_adapter="chatterbot.storage.SQLStorageAdapter",
        # database="Bot1.sqlite3",
        database_uri='sqlite:///site////lucy.sqlite3',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I am not sure how to respond to that, I am still learning',
                'maximum_similarity_threshold': 0.60
            }
        ]
    )

    # Disabling trainers

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    trainer = ListTrainer(chatbot)
    trainer.train([
        "Hi",
        "Hello, I am Lucy!!! 🤗",
    ])
    trainer.train([
        "What is your name?",
        "I am Lucy!!! 🤗",
    ])
    trainer.train([
        "Hi",
        "Hello, what a great day!",
    ])
    trainer.train([
        "Hello, AI",
        "Welcome to Lucy!!! 🤗",
    ])
    trainer.train([
        "Are you a plant?",
        "No, I am Lucy an AI System to help you LOL",
    ])
    trainer.train([
        "What is your purpose?",
        "To Help make your life better!",
    ])
    # Define a list of conversation pairs
    conversation = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great, thank you! How can I help you today?",
        # ... more conversation pairs
    ]
    conversation2 = [
        "Funny how they have the load I pickup deliver Monday but, I got 13hrs now. I get back 5 tonight, then 2 then 11 lol",
        "I have two like 3 hour days, not sure if I'll be able to actually make this load on time",
        "It's impossibl in their time frame, Cuz I'll get to Portland at least then somewhere between there and Richland I'll be bobtail so... maybe space age or something I can make a spot idk.  Then I'll basically have no time, and only get 5hrs for tomorrow lolllll. Stupid. Can't do 2044 total miles by Monday morning.",
    ]
    conversation3 = [
        "Whats a good allergy med for dogs",
        "Benadryl",
        "Roger that, How much for foxy",
        "According to the Merck Veterinary Manual, the standard dose for Benadryl® is 2 to 4 milligrams per kilogram of body weight, or 0.9 to 1.8 milligrams mg of Benadryl® per pound. Therefore, a simple and practical dose is 1 mg of Benadryl® per pound of your dogs weight, given two to three times a day.",
        "You rock!",
        "Most bendryl is 25 mg. So Id say 1/3-1/2 pill,  You cant OD on benedryl, A pistachio cream, cold brew grande, Haha. Changed my mind. A pistachio latte 12 ounce hot",
        "Roger that.  Be there in a few!",
        "Headed your way",
        "Sweet! See you in a bit, I got the discs from Jen",
        "Serena is coming. But she doesnt want to play. She just wants to get out of the house for a bit.",
        "Headed to Nampa now then your place",
        "See you soon. I have your Lego! And you have my water bottle. 🙃 Also if you bring your camp stove and tanae cover I can work on getting those posted for sale.",
        "I will bring them over today.",
        "It was great seeing you today 🙃🤔",
    ]
    # Train the chatbot with your custom conversation
    trainer.train(conversation)
    trainer.train(conversation2)
    trainer.train(conversation3)

    # Training the AI with a CSV file with standard questions and answers
    # making data frame from csv file
    data = pd.read_csv("conversations.csv", index_col="Index")
    i = 0
    for row in data.index:
        # retrieving row by loc method
        first = (data['Conversations'].values[i])
        # second = (data['Answer'].values[i])

        # Adding info from the csv file for training...
        question = f'{first}'
        # answer = f'{second}'

        # print(f"{question}", f"{answer}")
        trainer.train([
            f"{question}",
            # f"{answer}",
        ])
        i += 1

    exit_conditions = (":q", "quit", "exit")
    while True:
        # Getting speech instead of having to type to chatpot
        input("Press Enter to continue...")
        audio = record_audio()
        query = recognize_speech(audio)
        # query = input("> ")
        if query is None:

            audio = record_audio()
            query = recognize_speech(audio)
        elif query in exit_conditions:
            speech = f"Goodbye"

            print(f"🪴 {speech}")
            # text_to_speech(text=speech)
            break
        elif 'get weather' in query or 'what is the weather' in query:
            speech = f"What City would you like me to check for you?"
            print(f"🤪 {speech}")
            # text_to_speech(text=speech)
            audio = record_audio()
            checkCity = recognize_speech(audio)

            speech = f"Getting weather for {checkCity}! Please wait a second..."
            print(f"🤪 {speech}")
            # text_to_speech(text=speech)

            weather = get_weather(city=f"{checkCity}")
            print(f"🪴 Here is your weather {weather}")
            speech = f"Here is your weather {weather}"
            # text_to_speech(text=speech)
        else:
            # EmotionsMarker = emotions_chat_marker(get_emotion = f"{query}")
            speech = f"{chatbot.get_response(query)}"
            # print(f"🤪 {speech}" + f"🤔 Your emotional marker is {EmotionsMarker}")
            print(f"🤪 {speech}")
            # text_to_speech(text=speech)

    write_log(Message='Closing Lucy Functions', FuncName='Lucy', ErrorType='Info')
# End Lucy


# Creating gui parameters
class MAIN_WINDOW(QMainWindow):
    # Creating a gui for the main LUCY app

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lucy UI 1.0.1.13")
        self.setFixedWidth(600)
        self.setFixedHeight(450)
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 1000
        # self.initUI()

        # def initUI(self):
        self.label = QLabel()
        self.TextBox = QTextBrowser()

        self.Button = QPushButton("Submit Text Question")
        self.Button.setCheckable(True)
        self.Button.setDefault(True)
        self.Button.clicked.connect(self.the_button_was_clicked)
        self.Button2 = QPushButton("Submit Spoken Question")
        self.Button2.setCheckable(True)
        self.Button2.setDefault(False)
        self.Button2.clicked.connect(self.speech)
        self.input = QLineEdit()
        self.input.returnPressed.connect(self.Button.click)
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.TextBox)
        layout.addWidget(self.Button)
        layout.addWidget(self.Button2)

        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window.
        self.setCentralWidget(container)

    def the_button_was_clicked(self):
        textboxValue = self.input.text()
        # print(f"Clicked! {textboxValue}")
        self.TextBox.append(f"🤓 {textboxValue}")
        response = lucy_gui(query=f"{textboxValue}")
        self.TextBox.append(f"{response}")
        self.input.clear()
        if 'Goodbye' in response:
            sys.exit()

    def speech(self):
        # print("Getting speech to text")
        query = get_speech()
        self.TextBox.append(f"🤓 {query}")
        response = lucy_gui(query=f"{query}")
        self.TextBox.append(f"{response}")
        if 'Goodbye' in response:
            sys.exit()


def gui():
    # TODO need to change this to pygame for better response within the app
    app = QApplication(sys.argv)

    window = MAIN_WINDOW()
    window.show()
    # Start the event loop
    app.exec()
