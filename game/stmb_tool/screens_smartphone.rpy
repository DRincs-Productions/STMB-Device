default smartphone_current_app = None 
default smartphone_back_label = None 

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
            idle '/stmb_interface/button/home.webp'
            action [
                Function(go_to_home, smartphone_back_list),
                SetVariable('smartphone_current_app', None),
            ]
            focus_mask True
            at smartphone_nav_button

        use expression smartphone_current_app.label_name
    if is_back_list_empty(smartphone_back_list):
        # button for go to home
        imagebutton:
            align (0.67, 0.4)
            idle '/stmb_interface/button/back.webp'
            action [
                Function(go_to_back, smartphone_back_list),
            ]
            focus_mask True
            at smartphone_nav_button

    image "/stmb_interface/smartphone.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width, gui.smartphone_height)

    # button for closure
    imagebutton:
        align (0.67, 0.18)
        idle '/stmb_interface/button/shutdown.webp'
        action [
            Hide('smartphone'),
        ]
        focus_mask True
        at smartphone_nav_button

screen smartphone_home():

    image "/stmb_interface/smartphone_background00.webp":
        align (0.5, 0.5)
        size (gui.smartphone_screen_width, gui.smartphone_screen_height)

    # taskbar_apps
    hbox:
        align (0.49, 0.95)

        for app in taskbar_apps:
            use smartphone_app_button(app, space = gui.smartphone_app_icon_space_taskbar)


    vpgrid mousewheel True draggable True id 'smartphone_home':
        xysize (gui.smartphone_screen_with_space_width, gui.smartphone_screen_app_height)
        align (0.5, 0.5)
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
                        use smartphone_app_button(df_apps[index], space = gui.smartphone_app_icon_space)

                elif (fraction > 0):
                    # empty_hole
                    hbox:
                        text ""
    # scroll bar
    vbar value YScrollValue('smartphone_home') style 'dr_menu_vscroll'

    key 'K_ESCAPE' action Hide('smartphone')
    key 'mouseup_3' action Hide('smartphone')


screen smartphone_app_button(app, space = 0):
    frame:
        xysize (gui.smartphone_app_icon_size + space, gui.smartphone_app_icon_size + space)
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
            at smartphone_app(gui.smartphone_app_icon_size)
