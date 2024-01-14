import deepl
import sys
# if no args or args is "--help" or "-h", print help
if "-h" in sys.argv or "--help" in sys.argv or "-H" in sys.argv:
    print("Usage: python3 main.py <text> (--lang=<lang>-><lang>)\n")
    print("Example: python3 main.py \"Hello World!\"")
    print("         python3 main.py \"你好世界！\"")
    print("The example above, the program automatically detects the language.\n")
    print("If all characters are English, the program will translate the text to Chinese.")
    print("Otherwise, the program will consider the text as Chinese and translate it to English.\n")
    print("If you want to specify the language, you can use the --lang option. <lang> should be the ISO 639-1 code.")
    print("Examples: python3 main.py \"你好世界！\" --lang=ZH->EN")
    print("         python3 main.py --lang=EN->ZH \"Hello World!\"")
    print("         python3 main.py --lang=EN->ZH Hello World!")
    print()
    print("Or echo \"Hello World!\" | python3 main.py --lang=EN->ZH")
    sys.exit(0)
if "-v" in sys.argv or "--version" in sys.argv or "-V" in sys.argv:
    print("DeepL CLI v0.0.2")
    print("Type \"python3 main.py --help\" for help.")
    sys.exit(0)

# check args if --lang option is specified
lang = None
s=""
for arg in sys.argv[1:]:
    if arg.startswith("--lang="):
        if lang is not None:
            print("Error: --lang option has been specified more than once.")
            raise ValueError
        lang = arg.split("--lang=")[1]
    else:
        s += f"{arg} "

if not s:
    # read until EOF
    s = sys.stdin.readlines()
else:
    s=s[:-1].split("\n")

try:
    langs = lang.split("->")
except IndexError:
    print("Error: Invalid --lang option.")
    raise
except AttributeError:
    langs = None
else:
    if len(langs) != 2:
        print("Error: Invalid --lang option.")
        raise ValueError
# if no --lang option, detect language
for line in s:
    if not langs:
        try:
            line.encode('ascii')
            langs_tmp = ("EN", "ZH")
        except UnicodeEncodeError:
            langs_tmp = ("ZH", "EN")
        except Exception:
            print("Error: Invalid text.")
            raise
    else:
        langs_tmp = langs
    print(deepl.translate(text=line.strip(), source_language=langs_tmp[0], target_language=langs_tmp[1]))
