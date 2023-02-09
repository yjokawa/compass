def on_forever():
    if input.compass_heading() >= 316 or input.compass_heading() < 45:
        basic.show_string("N")
    elif input.compass_heading() >= 46 and input.compass_heading() < 135:
        basic.show_string("E")
    elif input.compass_heading() >= 136 and input.compass_heading() < 225:
        basic.show_string("S")
    else:
        basic.show_string("W")
basic.forever(on_forever)
