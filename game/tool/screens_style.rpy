define gui.lateralframescroll_ysize = 850
define gui.little_text_size = 18
define gui.normal_text_size = 24
define gui.big_normal_text_size = 28
define gui.hour_text_size = 60

style menu_vscroll is vscrollbar:
    xsize 7
    unscrollable 'hide'

init:
    transform smartphone_close_button:
        xanchor 25
        size (75, 75)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.2)
    transform smartphone_app:
        xanchor 25
        size (75, 75)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.2)
    transform smartphone_contact_icon:
        size (100, 100)
