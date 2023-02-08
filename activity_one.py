import tkinter as tk

# Create the window
window = tk.Tk()
window.title("Activity One")
window.geometry("200x200")

#make the window have a background color
window.configure(background="blue")



name = tk.Label(text="Name: ")
name.pack()
name_textbox = tk.Entry()
name_textbox.pack()
number = tk.Label(text="Number: ")
number.pack()
number_textbox = tk.Entry()
number_textbox.pack()


name.configure(background="orange")
number.configure(background="orange")


name.place(x=10, y=10)
name_textbox.place(x=60, y=10)
number.place(x=10, y=40)
number_textbox.place(x=70, y=40)







# Run the main window loop
window.mainloop()

