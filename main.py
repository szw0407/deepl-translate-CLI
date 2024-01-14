import deepl
import sys
# if no args or args is "--help" or "-h", print help
if len(sys.argv) == 1 or sys.argv[1] == "--help" or sys.argv[1] == "-h":
    print("Usage: python3 main.py <text> (--lang=<lang>-><lang>)\n")
    print("Example: python3 main.py \"Hello World!\"")
    print("Example: python3 main.py \"你好世界！\"")
    print("The example above, the program automatically detects the language.\n")
    print("If all characters are English, the program will translate the text to Chinese.")
    print("Otherwise, the program will consider the text as Chinese and translate it to English.\n")
    print("If you want to specify the language, you can use the --lang option.")
    print("Example: python3 main.py \"你好世界！\" --lang=ZH->EN")
    print("Example: python3 main.py \"Hello World!\" --lang=EN->ZH")
    sys.exit(0)
# get text
s = sys.argv[1]
# if --lang option is specified
try:
    lang = sys.argv[2]
except IndexError:
    try:
        s.encode('ascii')
        lang = "EN->ZH"
    except UnicodeEncodeError:
        lang = "ZH->EN"
    except Exception:
        print("Error: Invalid text.")
        raise
else:
    try:
        lang = lang.split("--lang=")[1]
    except IndexError:
        print("Error: Invalid --lang option.")
        raise
finally:
    try:
        langs = lang.split("->")
    except IndexError:
        print("Error: Invalid --lang option.")
        raise
    else:
        if len(langs) != 2:
            print("Error: Invalid --lang option.")
            raise ValueError
    print(deepl.translate(text=s, source_language=langs[0], target_language=langs[1]))
