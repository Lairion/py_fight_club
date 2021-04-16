from browser import document, alert

def hello(event):
    alert("Hello")

def add_event_to_class(class_name, event):
    for class_elem in document.getElementsByClassName(class_name):
        class_elem.bind("click", event)

add_event_to_class("hello", hello)
