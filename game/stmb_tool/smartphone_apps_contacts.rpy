init python:
    from pythonpackages.sdtmb.contact import Contact

define contacts = [
    Contact(character=a),
    Contact(character=an),
]

default contact_selected = None

screen smartphone_app_contacts():

    if contact_selected:
        image "/stmb_interface/app_screen/smartphone_app_contact.webp":
            align (0.5, 0.5)
            size (gui.smartphone_screen_width, gui.smartphone_screen_height)
        use contacts_show(contact_selected)
    else:
        image "/stmb_interface/app_screen/smartphone_app_contacts.webp":
            align (0.5, 0.5)
            size (gui.smartphone_screen_width, gui.smartphone_screen_height)
        use contacts_list(contacts)

screen contacts_list(contacts):

    viewport mousewheel True draggable True id 'contacts_list':
        align (0.5, 0.5)
        xysize (gui.smartphone_screen_contacts_width, gui.smartphone_height-350)
        spacing 10
        has vbox # should always be added at the end to avoid problems
        for contact in contacts:
            if not contact.is_hidden(flags):
                use contacts_item(contact.icon, contact.name,
                [
                    SetVariable('contact_selected', contact),
                    SetVariable('smartphone_back_label', "smartphone_app_contacts_go_back"),
                ])
    # scroll bar
    vbar value YScrollValue('contacts_list') style 'dr_menu_vscroll'

screen contacts_item(icon, name, my_action = None, sms = None):

    button:
        xsize gui.smartphone_screen_contacts_width
        if my_action:
            action my_action
        hbox:
            spacing 10
            imagebutton:
                idle icon
                at smartphone_contact_icon
            vbox:
                align (0.5, 0.5)
                text name:
                    size gui.dr_big_normal_text_size
                    color '#000000'
                if sms:
                    text sms:
                        size gui.dr_normal_text_size
                        color '#000000'

screen contacts_show(contact):
    vbox:
        align (0.5, 0.1)
        image contact.icon:
            size (300, 300)
        text contact.name:
            color "#000"
            align (0.5, 0.5)
            size 50

label smartphone_app_contacts_go_back:
    $ contact_selected = None
    $ smartphone_back_label = None
    call screen smartphone
    return
