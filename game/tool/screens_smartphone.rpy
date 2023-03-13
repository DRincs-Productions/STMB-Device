define gui.smartphone_height = 1080
define gui.smartphone_width = 570

screen smartphone():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"

    image "/interface/smartphone_background00.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)

    image "/interface/smartphone.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width, gui.smartphone_height)

    # button for closure
    imagebutton:
        align (0.67, 0.18)
        idle '/interface/button/shutdown.webp'
        action [
            Hide('smartphone'),
        ]
        focus_mask True
        at smartphone_close_button

    # taskbar_apps
    hbox:
        align (0.49, 0.95)

        for app in taskbar_apps:
            # If the Locations where I am is the same as the Locations where the room is located
            button:
                frame:
                    background None

                    # App icon
                    imagebutton:
                        align (0.5, 0.0)
                        idle app.icon
                        # selected (True if cur_room and cur_room.id == room.id else False)
                        # sensitive not room.isDisabled(flags)
                        focus_mask True
                        at smartphone_app

                    # # App name
                    # text app.name:
                    #     size gui.little_text_size
                    #     drop_shadow [(2, 2)]
                    #     xalign 0.5
                    #     text_align 0.5
                    #     line_leading 0
                    #     line_spacing -2


    key 'K_ESCAPE' action Hide('smartphone')
    key 'mouseup_3' action Hide('smartphone')
