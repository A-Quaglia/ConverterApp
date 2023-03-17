import tkinter as tk
from tkinter import ttk

import converter as cnv

def converter_cmd():
    input_unit = input_units.get().lower()
    output_unit = output_units.get().lower()
    input = float(_input.get())

    # print(str(cnv.converter(input, input_unit, output_unit)))
    # print(input, input_unit, output_unit)
    _output.set(str(cnv.converter(input, input_unit, output_unit)))



root = tk.Tk()
root.title('Temperature Converter')

mainframe = ttk.Frame(root, padding=(5,5,5,5) )
mainframe.grid(row=0, column=0, sticky='NESW')

input_frame = ttk.LabelFrame(mainframe, text='INPUT')
input_frame.grid(row=0, column=0)

output_frame = ttk.LabelFrame(mainframe, text='OUTPUT')
output_frame.grid(row=0, column=1)

_input = tk.StringVar()
_output = tk.StringVar()

temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']

input_entry = ttk.Entry(input_frame, font=('Arial', 18), width=10, textvariable=_input)
input_entry.grid(row=0, column=0, sticky='NESW', padx=5)

input_units =  tk.StringVar()
input_list = ttk.Combobox(input_frame, textvariable=input_units, height=6, values=temp_units, state='readonly')
input_list.current(1)
input_list.grid(row=1, column=0, padx=5, pady=5)

output_label = ttk.Entry(output_frame, font=('Arial', 18), width=10, textvariable=_output)
output_label.grid(row=0, column=0, sticky='NESW', padx=5)

output_units =  tk.StringVar()
output_list = ttk.Combobox(output_frame, textvariable=output_units, height=6, values=temp_units, state='readonly')
output_list.current(0)
output_list.grid(row=1, column=0, padx=5, pady=5)


calculate_btn = ttk.Button(
    mainframe, text='Convert', command=converter_cmd, width=40)
calculate_btn.grid(row=1, column=0, columnspan=2)

root.bind("<Return>", lambda event: converter_cmd())

root.mainloop()
