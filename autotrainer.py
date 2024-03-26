import random
import time
import schedule
from pyautogui import  *
import pyautogui as py

#Separador

def separador():
    print("----------------------------------------------------------------------------------------------")
    
#Bienvenida

print("""Bienvenido a 'Tibia Autotrainer Bot'
Empecemos ;)""")
separador()

#Introduccion de los datos

print("""Esta es la lista de armas equipables:
-Small stones""")
separador()
weapon = input("Indique el arma a utilizar: ")
separador()
time_minutes = float(input("Indique cada cuanto tiempo quiere que su personaje se mueva: "))
separador()
time_auto_heal = int(input("Indique cada cuanto tiempo quiere que su personaje sane: "))

#definicion de las variables

weapons = { 'Small stones': 'images/small_stones.png' }
focus_area = 'images/focus_area.png'
weapon_slot = 'images/weapon_slot.png'
time_seconds = time_minutes * 60
selected_weapon = weapon.capitalize()

#schedule function

def run_job(minutes: int, do):
    schedule.every(minutes).minutes.do(do)

#deficion de las funciones del movimiento automatico


def random_movement():
    arrow_keys = ['up', 'right', 'down', 'left']
    random.shuffle(arrow_keys)
    py.keyDown('ctrlleft')
    py.press(arrow_keys)
    py.keyUp('ctrlleft')
    
    
def image_check():
    try:
        if py.locateCenterOnScreen(focus_area, confidence=0.8) != ImageNotFoundException:
            random_movement()
            time.sleep(time_seconds)
            
    except:
        pass
    
#definicion de la funcion del sanador automatico

def auto_heal():
    py.press('f1')
    

#definicion de la funcion de equipar armas automaticamente
def equip_weapon():
    try:
      weapon_slot_x, weapon_slot_y = py.locateCenterOnScreen(weapon_slot)
      selected_weapon_x, selected_weapon_y = py.locateCenterOnScreen(weapons[selected_weapon])

      py.moveTo(selected_weapon_x // 2, selected_weapon_y // 2)
      py.dragTo(weapon_slot_x // 2, weapon_slot_y // 2, button='left')
    except:
      pass
    

    
run_job(time_auto_heal,auto_heal)
while True:
    
    image_check()
    equip_weapon()
    
    schedule.run_pending()
    time.sleep(1)

    

    
