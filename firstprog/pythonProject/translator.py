from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to handle translation
def change(text='type', src='English', dest='Hindi'):
    try:
        trans = Translator()
        trans1 = trans.translate(text, src=src.lower(), dest=dest.lower())
        return trans1.text
    except Exception as e:
        return "Error: Translation service failed."

# Function to fetch and display the translated text
def data():
    s = comb_sor.get()
    d = comb_des.get()
    masg = sor_txt.get(1.0, END).strip()
    if masg:
        translated_text = change(text=masg, src=s, dest=d)
        des_txt.delete(1.0, END)
        des_txt.insert(END, translated_text)
    else:
        des_txt.delete(1.0, END)
        des_txt.insert(END, "Please enter some text to translate.")

# GUI setup
root = Tk()
root.title('Translator')
root.geometry('500x700')
root.config(bg='light green')

# Title Label
lab_txt = Label(root, text='Translator', font=('times new roman', 40, 'bold'), bg='light green')
lab_txt.place(x=100, y=40, width=300, height=50)

# Source Text Label
lab_txt = Label(root, text='Source Text', font=('times new roman', 20, 'bold'), bg='light green')
lab_txt.place(x=100, y=100, width=300, height=25)

# Source Text Box
sor_txt = Text(root, font=('times new roman', 20, 'bold'), wrap=WORD)
sor_txt.place(x=10, y=130, width=480, height=150)

# Language selection
list_text = list(LANGUAGES.values())

# Source Language Combobox
comb_sor = ttk.Combobox(root, value=list_text)
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set('English')

# Translate Button
Button_change = Button(root, text='Translate', relief=RAISED, command=data)
Button_change.place(x=170, y=300, height=40, width=150)

# Destination Language Combobox
comb_des = ttk.Combobox(root, value=list_text)
comb_des.place(x=330, y=300, height=40, width=150)
comb_des.set('Hindi')

# Destination Text Label
lab_txt = Label(root, text='Destination Text', font=('times new roman', 20, 'bold'), bg='light green')
lab_txt.place(x=100, y=360, width=300, height=20)

# Destination Text Box
des_txt = Text(root, font=('times new roman', 20, 'bold'), wrap=WORD)
des_txt.place(x=10, y=400, width=480, height=150)

# Start the main event loop
root.mainloop()



#pip install googletrans==4.0.0-rc1





