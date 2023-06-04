basic.showString("Jana")
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showIcon(IconNames.Heart)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(8)
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    for (let i = 0; i < 10; i++) {
        basic.showNumber(i)
    }
})
