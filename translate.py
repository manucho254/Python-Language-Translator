from tkinter import Tk, Button,END, Label, Text, StringVar, Frame
from googletrans import Translator
from tkinter import ttk
from tkinter.messagebox import showerror
import threading

class translated(Frame):
    def __init__(self, master):
        self.master = master
        self.master.title('Translate')
        self.labelTranslate = Label(self.master,  text='Translator', font='Helvetica, 20 bold',  bg='black', fg='white')
        self.labelTranslate.pack(side='top', fill='both')

        self.labelChooseLanguage = Label(self.master,  
                       text='Choose language', font='Helvetica, 15 bold', width=40,  bg='white', fg='black')
        self.labelChooseLanguage.place(x=260, y=41)
        
        self.textEntered = Text(self.master, width=40, font='italic, 14 bold', height=15)
        self.textEntered.place(x=40, y=110)
        self.textTranslated = Text(self.master, width=40, font='italic, 14 bold', height=15)
        self.textTranslated.place(x=520, y=110)

        default = StringVar()
        val = default.get()# get the value before being deleted by garbage collection

        self.defaults = ttk.Combobox(
            self.master, width=20, textvariable=val, state='readonly', font=('verdana', 10, 'bold'))

        self.defaults['values'] = ('English')

        self.defaults.place(x=190, y=80)
        self.defaults.current(0)

        #=============================================================#

        value = StringVar()
        keepValue = value.get() # get the value before being deleted by garbage collection

        self.chooseLangauge = ttk.Combobox(
            self.master, width=20, textvariable=keepValue, state='readonly', font=('verdana', 10, 'bold'))

        #========instert all the language values to our combobox============
        self.chooseLangauge['values'] = (
            'Afrikaans','Albanian','Arabic',
            'Armenian',' Azerbaijani','Basque','Belarusian','Bengali',
            'Bosnian','Bulgarian',' Catalan','Cebuano','Chichewa','Chinese','Corsican',
            'Croatian','Czech','Danish','Dutch','English','Esperanto','Estonian','Filipino',
            'Finnish','French','Frisian','Galician','Georgian','German','Greek','Gujarati',
            'Haitian Creole','Hausa','Hawaiian','Hebrew','Hindi','Hmong','Hungarian','Icelandic',
            'Igbo','Indonesian','Irish','Italian','Japanese','Javanese','Kannada','Kazakh','Khmer',
            'Kinyarwanda','Korean','Kurdish','Kyrgyz','Lao','Latin','Latvian','Lithuanian',
            'Luxembourgish','Macedonian','Malagasy','Malay','Malayalam','Maltese','Maori','Marathi',
            'Mongolian','Myanmar','Nepali','Norwegian''Odia','Pashto','Persian','Polish','Portuguese','Punjabi',
            'Romanian','Russian','Samoan','Scots Gaelic','Serbian','Sesotho','Shona','Sindhi',
            'Sinhala','Slovak','Slovenian','Somali','Spanish','Sundanese','Swahili','Swedish','Tajik',
            'Tamil','Tatar','Telugu','Thai','Turkish','Turkmen','Ukrainian','Urdu','Uyghur','Uzbek',
            'Vietnamese','Welsh','Xhosa''Yiddish','Yoruba','Zulu',)

        self.chooseLangauge.place(x=610, y=80)
        self.chooseLangauge.current(19)

        translated = Translator()
       
       # =========clear all the textboxes =========#
        def clear():
            self.textEntered.delete(1.0, END)
            self.textTranslated.delete(1.0, END)

       #=====main function to translate the languages====
        def getAndTranslate():
            try:
                lang = self.chooseLangauge.get() # get the language value from combobox
                enteredText = self.textEntered.get(1.0, END)
                translations = translated.translate(enteredText, dest=lang)
                self.textTranslated.delete(1.0, END)
                self.textTranslated.insert(END, translations.text.title())
            except:
                showerror('Error', 'try again')

        #=====threading the function to prevent the gui from freezing========#
        def threaded():
            runs = threading.Thread(target=getAndTranslate)
            runs.start()


        self.buttonTranslate = Button(self.master, text='Translate', bd=3, 
                   bg='black', fg='white', font=('Helvetica', 15 ), width=10, command=threaded)
        self.buttonTranslate.place(x=350, y=450)

        self.buttonClear = Button(self.master, text='clear', bd=3,
                     bg='black', fg='white', width=10, font=('Helvetica', 15 ), command=clear)
        self.buttonClear.place(x=530, y=450)

def main():
    root = Tk()
    ui = translated(root)
    root.geometry('1000x500+200+100')
    root.mainloop()

if __name__ == '__main__':
    main()