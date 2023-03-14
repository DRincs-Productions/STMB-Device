# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    call screen room_navigation

screen room_navigation():
    modal True
    # Tools
    frame:
        yalign 0.0 xalign 0.0
        hbox:
            textbutton "SmartPhone" action Show("smartphone")
            textbutton "Exit" action Quit(confirm=False)
