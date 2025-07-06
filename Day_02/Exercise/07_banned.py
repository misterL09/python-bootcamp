user_input = input("input: ")
banned_words = ['moist','break','raise']
if user_input in banned_words:
    print("Banned")


if input("input: ") in ('moist','break','raise'):
    print("Banned")