from time import sleep
import pyautogui as pygui

def run():
    
    while True:
        accept_location = pygui.locateOnScreen('aceptar.png')
        
        if accept_location != None:
            accept_location = pygui.center(accept_location)
            
            mouse_pos = pygui.position()
            pygui.click(accept_location.x,accept_location.y)
            pygui.hotkey('alt','tab')
            pygui.moveTo(mouse_pos)
            print('clic!')

        else:
            print('no :(')
        
        
if __name__ == '__main__':
    run()