
screen smartphone():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"

    image "/interface/background00.webp":
        align (0.5, 0.5)
        size (570, 1070)

    image "/interface/smartphone.webp":
        align (0.5, 0.5)
        size (600, 1080)

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
