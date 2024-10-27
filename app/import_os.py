import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

# --- Tool Functions ---
def talk(text):
    """Speak out the provided text."""
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    """Capture and process user instruction."""
    instruction = ""
    try:
        with sr.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "tom" in instruction:
                instruction = instruction.replace('tom', '').strip()
                print("Command received:", instruction)
    except sr.UnknownValueError:
        talk("Sorry, I did not catch that. Could you please repeat?")
    except sr.RequestError:
        talk("Sorry, I'm having trouble connecting to the speech recognition service.")
    return instruction.strip()

# Define tools as functions
def play_on_youtube(query):
    """Play a video on YouTube based on the query."""
    talk(f"Searching YouTube for {query}")
    try:
        pywhatkit.playonyt(query)
    except Exception as e:
        print("Error searching YouTube:", e)
        talk("I'm having trouble finding that video on YouTube.")

def tell_time():
    """Provide the current time."""
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    talk(f"The current time is {current_time}")

def tell_date():
    """Provide the current date."""
    current_date = datetime.datetime.now().strftime('%d/%m/%Y')
    talk(f"Today's date is {current_date}")

def provide_greeting():
    """Respond to a greeting."""
    talk("Thanks! I'm fine. How about you?")

def tell_name():
    """Introduce the assistant's name."""
    talk("I am Tom. What can I do for you?")

def search_wikipedia(query):
    """Search Wikipedia for information about the query."""
    talk(f"Searching for information on {query}")
    try:
        info = wikipedia.summary(query, sentences=1)
        print(info)
        talk(info)
    except wikipedia.exceptions.PageError:
        print("Exact match not found. Searching for closest match...")
        search_results = wikipedia.search(query)
        if search_results:
            closest_match = search_results[0]
            print(f"Closest match: {closest_match}")
            try:
                info = wikipedia.summary(closest_match, sentences=1)
                talk(f"I couldn't find an exact match, but here's information on {closest_match}:")
                print(info)
                talk(info)
            except Exception as e:
                talk("Sorry, I couldn't find any information.")
                print(e)
        else:
            talk("Sorry, I couldn't find any information.")

def calculate(expression):
    """Evaluate and respond to a mathematical expression."""
    try:
        result = eval(expression)
        talk(f"The answer is {result}")
        print(f"Calculation result: {result}")
    except Exception as e:
        talk("Sorry, I couldn't calculate that.")
        print("Calculation error:", e)

# --- Central Function to Handle Commands ---
def play_jarvis():
    instruction = input_instruction()
    print("Processed instruction:", instruction)
    
    # Map the instruction to the appropriate tool
    if any(keyword in instruction for keyword in ["play", "search for", "find"]):
        song = instruction.replace("play", "").replace("search for", "").replace("find", "").strip()
        play_on_youtube(song)
    elif "time" in instruction:
        tell_time()
    elif "date" in instruction:
        tell_date()
    elif "how are you" in instruction:
        provide_greeting()
    elif "what is your name" in instruction:
        tell_name()
    elif "who is" in instruction:
        human = instruction.replace("who is", "").strip()
        search_wikipedia(human)
    elif any(keyword in instruction for keyword in ["calculate", "what is", "solve"]):
        expression = instruction.replace("calculate", "").replace("what is", "").replace("solve", "").strip()
        calculate(expression)
    elif "goodbye" in instruction or "exit" in instruction:
        talk("Goodbye! Have a great day!")
        return False
    else:
        talk("Please repeat.")
    
    return True

# --- Main Function to Run the Assistant ---
def main():
    while True:
        if not play_jarvis():
            break

if __name__ == "__main__":
    main()
