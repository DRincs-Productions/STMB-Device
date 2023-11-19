init:
    transform smartphone_close_button:
        xanchor 25
        size (75, 75)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.2)
    transform smartphone_app(icon_size):
        xanchor 25
        size (icon_size, icon_size)
        on idle:
            matrixcolor BrightnessMatrix(0)
        on hover:
            matrixcolor BrightnessMatrix(0.2)
    transform smartphone_contact_icon:
        size (100, 100)
