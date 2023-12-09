default current_tv_channel = None 
default current_tv_image = None 

screen tv(home_screen, background, my_align, my_size):

    ## Avoid predicting this screen, as it can be very large.
    predict False

    modal True
    style_prefix "game_menu"

    if current_tv_channel:
        image current_tv_channel.image:
            align my_align
            size my_size
        if current_tv_channel.label_name:
            use expression current_tv_channel.label_name
    else:
        image home_screen:
            align my_align
            size my_size

    image background:
        size (config.screen_width, config.screen_height)

    use tv_remote_control((0.9, 0.9))

screen tv_remote_control(my_align = (0, 0)):
    frame:
        background None
        align my_align
        xsize 200
        ysize 600
        image "/stmb_interface/remote_control.webp":
            size (200, 600)
        image "gui triangular_button":
            size (32, 32)
            align (0.9, 0.14)
        image "gui triangular_button":
            size (32, 32)
            align (0.1, 0.13)
            rotate (180)
        # button for closure
        imagebutton:
            align (0.21, 0.775)
            idle '/stmb_interface/button/shutdown.webp'
            action [
                Hide('tv'),
            ]
            focus_mask True
            at tv_remote_control_litled_button
