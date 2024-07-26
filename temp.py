import tkinter as tk
bg_color='#9db2bf'
radio_fg_color='#068da9'
result_color='red2'

root=tk.Tk()
root.title("Temperature converter")
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='DodgerBlue2')

# Function define for conversion
def convert():
    temperature = float(entry.get())
    if var.get()==1:
        converted_temp=(temperature * 9/5) + 32
        result_label.config(text=f'Result :  {converted_temp : .2f} ℉')
    
    elif var.get()==2:
        converted_temp=(temperature - 32) * 5/9 
        result_label.config(text=f'Result :  {converted_temp : .2f} ℃')

main_label=tk.Label(root,text='Temperature Converter',font=('Rockwell', 20 ,'bold'),bg='DodgerBlue2',fg='gray21')
main_label.pack(pady=20)

entry_label=tk.Label(root,text='Enter Temperature',font=('Comic Sans MS',16,'bold'),bg='DodgerBlue2')
entry_label.pack()

# Entry section
entry=tk.Entry(root,font=('Rockwell',14))
entry.pack(pady=15)

var=tk.IntVar()

frame=tk.Frame(root,bg='DodgerBlue2')
frame.pack(pady=15)

# Button for conversion
c_to_f = tk.Radiobutton(frame,text='Celsius to Fahrenheit',variable=var,value=1,font=('Andy Bold',14), bg='DodgerBlue2', activebackground= 'DodgerBlue2', activeforeground= radio_fg_color)
c_to_f.grid(row=0,column=0)

f_to_c = tk.Radiobutton(frame,text='Fahrenheit to Celsius',variable=var,value=2,font=('Andy Bold',14), bg='DodgerBlue2', activebackground= 'DodgerBlue2', activeforeground= radio_fg_color)
f_to_c.grid(row=1,column=0)

convert_button=tk.Button(root,text='Convert',font=('MOORE MARY',15),bg='LightPink1',command=convert)
convert_button.pack()
 
result_label=tk.Label(root,text='',font=('Frutiger',16),bg='DodgerBlue2',fg=result_color)
result_label.pack(pady=14)

root.mainloop()