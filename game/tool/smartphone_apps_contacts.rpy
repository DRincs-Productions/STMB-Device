init python:
    from pythonpackages.sdtmb.contact import Contact

define contacts = [
    Contact(character=a),
    Contact(character=an),
]

screen smartphone_app_contacts():

    image "/interface/app_screen/smartphone_app_instagram.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)
    
    use contacts_list(contacts)


screen contacts_list(contacts):

    viewport mousewheel True draggable True id 'contacts_list':
        align (0.5, 0.5)
        xysize (gui.smartphone_width-60, gui.smartphone_height-300)
        spacing 10
        has vbox # should always be added at the end to avoid problems
        for contact in contacts:
            if not contact.is_hidden(flags):
                use contacts_item(contact.icon, contact.character)
    # scroll bar
    vbar value YScrollValue('contacts_list') style 'menu_vscroll'

screen messages_list(contacts):

    viewport mousewheel True draggable True id 'messages_list':
        align (0.5, 0.5)
        xysize (gui.smartphone_width-60, gui.smartphone_height-300)
        spacing 10
        has vbox # should always be added at the end to avoid problems
        for contact in contacts:
            if not contact.is_hidden(flags):
                use contacts_item(contact.icon, contact.character, "contact.sms")
    # scroll bar
    vbar value YScrollValue('messages_list') style 'menu_vscroll'

screen contacts_item(icon, name, sms = None):

    hbox:
        spacing 10
        imagebutton:
            idle icon
            at smartphone_contact_icon
        vbox:
            align (0.5, 0.5)
            text name:
                size gui.big_normal_text_size
                color '#000000'
            if sms:
                text sms:
                    size gui.normal_text_size
                    color '#000000'
