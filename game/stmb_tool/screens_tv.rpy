default current_tv_channel = None 
default current_tv_image = None 

screen tv(home_screen, background, my_align, my_size):

    tag menu

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

    use tv_remote_control

screen tv_remote_control():
    image "/stmb_interface/remote_control.webp":
        size (250, 600)
    image "gui triangular_button":
        size (32, 32)
        align (0.09, 0.31)
    image "gui triangular_button":
        size (32, 32)
        align (0.024, 0.31)
        rotate (180)
