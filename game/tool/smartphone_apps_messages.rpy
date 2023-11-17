init python:
    from pythonpackages.sdtmb.message import Message
    from pythonpackages.sdtmb.messages import Messages
    from pythonpackages.sdtmb.message_content import MessageContent

define messageTest = MessageContent(text = "Hello Hello Hello Hello Hello Hello Hello Hello")
define messageTest2 = MessageContent(text = "Hello")
default messages_selected = None

define messagesMc_list = [
    Message(
        character = a,
        chatId = a,
        message_content = messageTest,
        time_description = "day 1",
    ),
    Message(
        character = mc,
        chatId = a,
        message_content = messageTest,
        time_description = "day 1",
    ),
    Message(
        character = mc,
        chatId = a,
        message_content = messageTest,
        time_description = "day 1",
    ),
    Message(
        character = mc,
        chatId = a,
        message_content = messageTest,
        time_description = "day 1",
    ),
    Message(
        character = mc,
        chatId = a,
        message_content = messageTest,
        time_description = "day 1",
    ),
    Message(
        character = mc,
        chatId = a,
        message_content = messageTest,
        time_description = "day 1",
    ),
    Message(
        character = mc,
        chatId = a,
        message_content = messageTest,
        time_description = "day 1",
    ),
    Message(
        character = mc,
        chatId = a,
        message_content = messageTest,
        time_description = "day 2",
    ),
    Message(
        character = a,
        chatId = a,
        message_content = messageTest2,
        time_description = "day 2",
    ),
]

screen smartphone_app_messages():

    image "/interface/app_screen/smartphone_app_messages.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)
    
    use messages_list(contacts, mc)

screen messages_list(contacts, smartphone_character):

    viewport mousewheel True draggable True id 'messages_list':
        align (0.5, 0.5)
        xysize (gui.smartphone_width-60, gui.smartphone_height-350)
        spacing 10
        has vbox # should always be added at the end to avoid problems
        if messages_selected:
            use smartphone_app_messages_character(messages_selected, mc)
        else:
            for contact in contacts:
                $ ms = Messages(chatId = contact.character, messages = messagesMc_list)
                if not contact.is_hidden(flags) and ms.have_message:
                    use contacts_item(contact.icon, contact.name
                    [
                        SetVariable('messages_selected', ms.messages),
                        SetVariable('smartphone_back_label', "smartphone_app_messages_go_back"),
                    ],
                    ms.last_message.text
                    )
    # scroll bar
    vbar value YScrollValue('messages_list') style 'menu_vscroll'

screen smartphone_app_messages_character(dialogue, smartphone_character):
    style_prefix None

    $ previous_d_who = None
    $ previous_time = None
    for id_d, d in enumerate(dialogue):
        if d.character == smartphone_character:
            $ message_frame = "/interface/messages/phone_send_frame.webp"
        else:
            $ message_frame = "/interface/messages/phone_received_frame.webp"

        if previous_time != d.time_description:
            $ previous_time = d.time_description
            vbox:
                xalign 0.5
                text d.time_description:
                    color "#000"

        hbox:
            if d.character == smartphone_character:
                xsize gui.smartphone_width-60
            spacing 10
            if d.character == smartphone_character:
                box_reverse True

            #If this is the first message of the character, show an icon
            if previous_d_who != d.character:
                add d.icon

            vbox:
                yalign 1.0
                if d.character == smartphone_character:
                    xalign 1.0
                else:
                    xalign 0.0
                # if d.character != smartphone_character and previous_d_who != d.character:
                #     text d.character

                frame:
                    padding (20,20)

                    background Frame(message_frame, 23,23,23,23)
                    xsize 350

                    text d.text:
                        pos (0,0)
                        xsize 350
                        color "#000"
                        slow_cps False

                        if d.character == smartphone_character :
                            text_align 1.0

                        # id d.what_id
        $ previous_d_who = d.character

label smartphone_app_messages_go_back:
    $ messages_selected = None
    call screen smartphone
    return
