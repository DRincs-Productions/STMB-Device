init python:
    from pythonpackages.sdtmb.message import Message
    from pythonpackages.sdtmb.messages import Messages
    from pythonpackages.sdtmb.message_content import MessageContent

define messageAlice = MessageContent(text = "Hello")

define messages_list = [
    Message(
        character = a,
        message_content = messageAlice,
        day = 1,
    ),
]

screen smartphone_app_messages():

    image "/interface/app_screen/smartphone_app_messages.webp":
        align (0.5, 0.5)
        size (gui.smartphone_width-40, gui.smartphone_height-40)
    
    use messages_list(contacts)

screen messages_list(contacts):

    viewport mousewheel True draggable True id 'messages_list':
        align (0.5, 0.5)
        xysize (gui.smartphone_width-60, gui.smartphone_height-350)
        spacing 10
        has vbox # should always be added at the end to avoid problems
        for contact in contacts:
            $ ms = Messages(character = contact.character, messages = messages_list)
            if not contact.is_hidden(flags) and ms.have_message:
                use contacts_item(contact.icon, contact.name, ms.last_message.text)
    # scroll bar
    vbar value YScrollValue('messages_list') style 'menu_vscroll'
