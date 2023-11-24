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

    image background

# screen TV_remote_control(channel_list):
