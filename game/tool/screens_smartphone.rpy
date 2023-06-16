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
        # button for go to home
        imagebutton:
            align (0.67, 0.3)
            idle '/interface/button/home.webp'
            action [
                SetVariable('smartphone_current_app', None)
            ]
            focus_mask True
            at smartphone_close_button

        use expression smartphone_current_app.label_name

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

screen smartphone_home():

    image "/interface/smartphone_background00.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)

    # taskbar_apps
    hbox:
        align (0.49, 0.95)

        for app in taskbar_apps:
            use smartphone_app_button(app)


    vpgrid mousewheel True draggable True id 'smartphone_home':
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
                        use smartphone_app_button(df_apps[index], space = 20)

                elif (fraction > 0):
                    # empty_hole
                    hbox:
                        text ""
    # scroll bar
    vbar value YScrollValue('smartphone_home') style 'menu_vscroll'

    key 'K_ESCAPE' action Hide('smartphone')
    key 'mouseup_3' action Hide('smartphone')


screen smartphone_app_button(app, space = 0):
    button:
        xysize (100 + space, 100 + space)
        has vbox xsize 75 spacing 0
        frame:
            xysize (85 + space, 85 + space)
            background None

            # App icon
            imagebutton:
                align (0.5, 0.5)
                idle app.icon
                focus_mask True
                if app.label_name:
                    action [
                        SetVariable('smartphone_current_app', app)
                    ]
                at smartphone_app

        # # App name
        # text app.name:
        #     size 20
        #     drop_shadow [(2, 2)]
        #     align (0.5, 0.5)
        #     line_leading 0
        #     line_spacing -2
