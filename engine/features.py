
from pipes import quote
import struct
import subprocess
import time
from playsound import playsound
import eel,os,re,webbrowser,sqlite3
import pvporcupine
import pyaudio
import pyautogui
from engine.config import ASSISTANT_NAME
from engine.command import speak
import pywhatkit as kit
from engine.helper import extract_yt_term, remove_words
import google.generativeai as genai


conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()

@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\vendore\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower()

    app_name = query.strip()

    if app_name != "":
        try:
            print(f"Looking for app: {app_name}") 
            cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            print(f"Results from sys_command: {results}")  

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])

            else:
                cursor.execute('SELECT path FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()

                print(f"Results from web_command: {results}")  

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening " + query)
                    try:
                        os.system('start ' + query)
                    except Exception as e:
                        print(f"Error opening application: {e}")  
                        speak("not found")
        except Exception as e:
            print(f"An error occurred: {e}")  
            speak("something went wrong")


def PlayYoutube(query):
    search_term=extract_yt_term(query)
    speak("Playing "+search_term+" on Youtube")
    kit.playonyt(search_term)

def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try: 
        porcupine=pvporcupine.create(keywords=["jarvis","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
            keyword_index=porcupine.process(keyword)
            if keyword_index>=0:
                print("hotword detected")
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

def findContact(query):
    words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'whatsapp', 'video']
    query = remove_words(query, words_to_remove)
    try:
        query = query.strip().lower()
        cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
        results = cursor.fetchall()
        print(results[0][0])
        mobile_number_str = str(results[0][0])
        if not mobile_number_str.startswith('+91'):
            mobile_number_str = '+91' + mobile_number_str

        return mobile_number_str, query
    except:
        speak("Contact not found")
        return 0, 0

def whatsApp(mobile_no, message, flag, name):
    if flag == 'message':
        encoded_message = quote(message)
        whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"
        speak(f"Sending message to {name}")
        subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
        time.sleep(5) 
        pyautogui.press('enter')  
        speak(f"Message sent successfully to {name}")

    else:  
        whatsapp_url = f"whatsapp://send?phone={mobile_no}"
        speak(f"Opening WhatsApp chat with {name}")
        subprocess.run(f'start "" "{whatsapp_url}"', shell=True)
        time.sleep(5) 
        pyautogui.hotkey('ctrl', 'f')  
        time.sleep(1)
        pyautogui.write(name)  
        time.sleep(2)
        pyautogui.press('enter')  
        time.sleep(2)
        if flag == 'call':
            speak(f"Calling {name}")
            pyautogui.click(1832, 79) 
        elif flag == 'video':
            speak(f"Starting a video call with {name}")
            pyautogui.click(1759, 88)  

def makeCall(name, mobileNo):
    mobileNo = mobileNo.replace(" ", "")
    speak(f"Initiating a call to {name}")
    shortcut_url = f"https://www.icloud.com/shortcuts/b1fa369720204f348dc5b5630b6aaea9"   
    webbrowser.open(shortcut_url)  
    speak(f"Please confirm the call on your iPhone.") 

def sendMessage(message, mobileNo, name):
    mobileNo = mobileNo.replace(" ", "")
    encoded_message = quote(message)
    speak(f"Sending a message to {name}")
    shortcut_url = f"https://www.icloud.com/shortcuts/d44aab61a01b4ed89968ad27009aa724"
    webbrowser.open(shortcut_url)  
    speak(f"Please confirm the message on your iPhone.")

def chatBot(query):
    genai.configure(api_key="AIzaSyChYyAU8yaDJumsx4A6TEaIwtYMK1O1yoc")
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(query)
        reply = response.text
        print(reply)
        speak(reply)
        return reply

    except Exception as e:
        print(f"Error: {e}")
        return "I'm currently unavailable, please try again later."










    

