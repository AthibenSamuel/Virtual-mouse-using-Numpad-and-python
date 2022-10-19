from clicknium import clicknium as cc
import keyboard
def func1():
    x,y=cc.mouse.position()
    cc.mouse.move(x,y-3)
def func2():
    x,y=cc.mouse.position()
    cc.mouse.move(x,y+3)
def func3():
    x,y=cc.mouse.position()
    cc.mouse.move(x-3,y)
def func4():
    x,y=cc.mouse.position()
    cc.mouse.move(x+3,y)
def func5():
    x,y=cc.mouse.position()
    cc.mouse.move(x+3,y-3)
def func6():
    x,y=cc.mouse.position()
    cc.mouse.move(x-3,y-3)
def func7():
    x,y=cc.mouse.position()
    cc.mouse.move(x+3,y+3)
def func8():
    x,y=cc.mouse.position()
    cc.mouse.move(x-3,y+3)
def func9():
    x,y=cc.mouse.position()
    cc.mouse.click(x,y,"left")
def func10():
    x,y=cc.mouse.position()
    cc.mouse.click(x,y,"right")
keyboard.add_hotkey('8', func1, args =())
keyboard.add_hotkey('2', func2, args =())
keyboard.add_hotkey('4', func3, args =())
keyboard.add_hotkey('6', func4, args =())
keyboard.add_hotkey('9', func5, args =())
keyboard.add_hotkey('7', func6, args =())
keyboard.add_hotkey('3', func7, args =())
keyboard.add_hotkey('1', func8, args =())
keyboard.add_hotkey('-', func9, args =())
keyboard.add_hotkey('+', func10, args =())
keyboard.wait('esc')