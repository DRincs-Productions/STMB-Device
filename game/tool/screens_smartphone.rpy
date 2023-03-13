define gui.smartphone_height = 1080
define gui.smartphone_width = 570
define gui.smartphone_column_app_number = 4

default smartphone_current_app = None 

screen smartphone():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"

    if not smartphone_current_app or not smartphone_current_app.label_name:
        use smartphone_home
    else:
        $ renpy.call(smartphone_current_app.label_name)

    image "/interface/smartphone.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width, gui.smartphone_height)

screen smartphone_home():

    image "/interface/smartphone_background00.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)

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
                xysize (100, 100)
                has vbox xsize 75 spacing 0
                frame:
                    xysize (85, 85)
                    background None

                    # App icon
                    imagebutton:
                        align (0.5, 0.5)
                        idle app.icon
                        # selected (True if cur_room and cur_room.id == room.id else False)
                        # sensitive not room.isDisabled(flags)
                        focus_mask True
                        at smartphone_app

                # # App name
                # text app.name:
                #     size 20
                #     drop_shadow [(2, 2)]
                #     align (0.5, 0.5)
                #     line_leading 0
                #     line_spacing -2

    vpgrid:
        xysize (gui.smartphone_width-60, gui.smartphone_height-300)
        align (0.5, 0.4)
        cols gui.smartphone_column_app_number
        spacing 2

        $ number_app = len(df_apps)
        $ fraction = number_app % gui.smartphone_column_app_number
        $ empty_holes_number = gui.smartphone_column_app_number - fraction
        $ for_number = number_app + empty_holes_number

        # apps
        if ((for_number % gui.smartphone_column_app_number) == 0):
            for index in range(for_number):
                if (len(df_apps) > index):
                    hbox:
                        # If the Locations where I am is the same as the Locations where the room is located
                        button:
                            xysize (120, 120)
                            has vbox xsize 75 spacing 0
                            frame:
                                xysize (95, 95)
                                background None

                                # App icon
                                imagebutton:
                                    align (0.5, 0.5)
                                    idle df_apps[index].icon
                                    # selected (True if cur_room and cur_room.id == room.id else False)
                                    # sensitive not room.isDisabled(flags)
                                    focus_mask True
                                    at smartphone_app

                            # # App name
                            # text app.name:
                            #     size 20
                            #     drop_shadow [(2, 2)]
                            #     align (0.5, 0.5)
                            #     line_leading 0
                            #     line_spacing -2
                elif (fraction > 0):
                    # empty_hole
                    hbox:
                        text ""

    key 'K_ESCAPE' action Hide('smartphone')
    key 'mouseup_3' action Hide('smartphone')
