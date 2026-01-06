from gtts import gTTS
from langdetect import detect, DetectorFactory
from IPython.display import Audio, display

DetectorFactory.seed = 0

def auto_tts(text):
    try:
        lang = detect(text)
        print("Detected language:", lang)
    except:
        print("Language detection failed ❌")
        return

    if lang.startswith('en'):
        tts_lang = 'en'
    elif lang.startswith('ta'):
        tts_lang = 'ta'
    elif lang.startswith('ml'):
        tts_lang = 'ml'
    elif lang.startswith('te'):
        tts_lang = 'te'
    else:
        print("❌ Language not supported")
        return

    tts = gTTS(text=text, lang=tts_lang)
    tts.save("output.mp3")
    display(Audio("output.mp3", autoplay=True))

text = input("Enter text: ")
auto_tts(text)
