define gui.smartphone_height = 1080
define gui.smartphone_width = 570

screen smartphone():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"

    image "/interface/background00.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)

    image "/interface/smartphone.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width, gui.smartphone_height)

    # button for closure
    imagebutton:
        align (0.67, 0.18)
        idle '/interface/button_smartphone/shutdown.webp'
        action [
            Hide('menu_userinfo'),
        ]
        focus_mask True
        at close_smartphone

    key 'K_ESCAPE' action Hide('menu_userinfo')
    key 'mouseup_3' action Hide('menu_userinfo')
