basic.show_string("Jana")
def on_button_pressed_a():  
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_button_pressed_b():
    basic.show_number(8)
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_gesture_shake():   
    for i in range(10):
        basic.show_number(i)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)