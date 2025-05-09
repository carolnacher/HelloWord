import time


message = "Hello world! Hola mundo! Bonjour le monde! Ciao mondo! こんにちは世界！🌍 Let's start a new challenge"
for letter in  message:
    print(letter, end='', flush=True)
    time.sleep(0.1)
