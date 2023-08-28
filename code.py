from cProfile import label
import random
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
def responses(input):
    input = input.lower()
    greetings = ['hello','hi','hey']
    feelings = ['whats up','how are you']
    name = ['what is your name']
    helping = ['can you help me','i need lelp']
    bye = ['goodbye','bye','see you']
    anger = ['you do not help me','i can not find what i want']
    thanking = ['thank you','you really help me']
    shopping = ['i want to buy something']
    food = ['i am hungry','what can i eat']
    entertainment = ['i feel bored','what can i do now','i want to feel happy']
    
    
    if input in greetings:
        output = random.choice (greetings)
    elif input in feelings:
        output = 'i do not have feelings but thank you'
    elif input in helping:
        output = 'Sure, i really want to help you'    
    elif input in bye:
        output = random.choice(bye)    
    elif input in anger:
        output = 'can you rephrase what do you want'  
    elif input in thanking:
        output = 'you are welcome'   
    elif input in name:
        output = 'i am neutral!'   
    elif input in shopping:
        output = "you can shop online if you need anything"     
    elif input in food:
        output = 'you can make a sandwich'  
    elif input in entertainment:
        output = random.choice(['you can see a movie','you can call your friends'])      
    else:
        output = "sorry i don't understand you"    
    return output
 
x_place = 30
y_place = 40
def messages():
     global x_place 
     global y_place
     inputs = input.get()
     output = responses(inputs)
     inputs = 'YOU: '+ inputs
     input_show = StringVar()
     input_show.set(inputs)
     a= Label(window, textvariable=input_show, bg='white', fg='firebrick', font='Arial 17 bold').place(x= x_place,y= y_place)
     output = 'BOT: '+ output
     output_show = StringVar()
     output_show.set(output)
     b= Label(window, textvariable=output_show,justify='center' ,bg='white', fg='blue', font='Arial 17 bold').place(x= x_place+100,y= y_place+40)
     y_place += 80
     if y_place > 480:
         y_place = 40
         
window = tk.Tk(className='CHAT BOT')
window.geometry('680x600')
window.configure(bg='lightpink')   
input = StringVar()
get_input = tk.Entry(window, fg='firebrick' , bg='white',textvariable=input,width=33 , font='Arial 20 bold').place(x=15,y=517)
images = Image.open(r'c:\Users\H&M\Downloads\icons8-send-64.png')
resized =images.resize((50,50))
send_image = ImageTk.PhotoImage(resized)
input_button = tk.Button(window, text='SEND', bg='firebrick', fg='white',image=send_image, compound='right',command=messages ,font='Arial 16 bold', width=120).place(x=530,y=511)

window.mainloop()
