from googletrans import Translator
import pyperclip
# To run this script run the following commands first:
#
# pip install googletrans==4.0.0-rc1
# pip install pyperclip

def translate(text, lang):
    """
    Translates text from English to the specified language.

    Parameters:
    - text: The text to be translated.
    - lang: The language code.

    Returns:
    - The translated text.
    """
    translator = Translator()
    return translator.translate(text, dest = lang).text

def copy_to_clipboard(text):
    """
    Copy the given text to the clipboard.

    Parameters:
    - text: The text to be copied.
    """
    pyperclip.copy(text)

def main():
    # Text, which is translated
    text = "Happy birthday, Simon."
    
    # All the languages, to which the text is translated to
    langs = ["af", "sq", "am", "ar", "hy", "az", "eu", "be", "bn", "bs", "bg", "ca", "ceb", "zh-CN", "zh-TW", "co", "hr", "cs", "da",
              "nl", "en", "eo", "et", "fi", "fr", "fy", "gl", "ka", "de", "el", "gu", "ht", "ha", "haw", "he", "hi", "hmn", "hu", "is",
              "ig", "id", "ga", "it", "ja", "kn", "kk", "km", "ko", "ku", "ky", "lo", "la", "lv", "lt", "lb", "mk", "mg", "ms", "ml",
              "mt", "mi", "mr", "mn", "my", "ne", "no", "ny", "or", "ps", "fa", "pl", "pt", "pa", "ro", "ru", "sm", "gd", "sr", "st",
              "sn", "sd", "si", "sk", "sl", "so", "es", "su", "sw", "sv", "tg", "ta", "te", "th", "tr", "uk", "ur", "ug", "uz", "vi",
              "cy", "xh", "yi", "yo", "zu"] 

    result = ""
    for lang in langs:
        # print("Current lang: " + lang)
        translated = translate(text, lang)
        result += translated + "\n"
        print(translated)
    
    pyperclip.copy(result + "\b")

if __name__ == "__main__":
    main()
