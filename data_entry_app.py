import tkinter as tk
from tkinter import ttk

# Create a dict to hold our variables
variables = dict()

root = tk.Tk()
root.title("ABQ Data Entry Application")
root.columnconfigure(0, weight=1)

# Application heading
ttk.Label(
    root,
    text="ABQ Data Entry Application",
    font=("TkDefaultFont", 16)
).grid()

# Data Record Form
drf = ttk.Frame(root)
drf.grid(padx=10, sticky=(tk.W + tk.E))
drf.columnconfigure(0, weight=1)    

    # Record Information Frame
r_info = ttk.LabelFrame(drf, text="Record Information")
r_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    r_info.columnconfigure(i, weight=1)

        # Date
variables['Date'] = tk.StringVar()
ttk.Label(r_info, text='Date').grid(row=0, column=0)
ttk.Entry(
    r_info,
    textvariable=variables['Date']
).grid(row=1, column=0, sticky=(tk.W + tk.E))

        # Time
time_values = ['8:00', '12:00', '16:00', '20:00']
variables['Time'] = tk.StringVar()
ttk.Label(r_info, text='Time').grid(row=0, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['Time'],
    values=time_values
).grid(row=1, column=1, sticky=(tk.W + tk.E))

        # Technician
variables['Technician'] = tk.StringVar()
ttk.Label(r_info, text='Technician').grid(row=0, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['Technician']
).grid(row=1, column=2, sticky=(tk.W + tk.E))

        # Lab
variables['Lab'] = tk.StringVar()
ttk.Label(r_info, text='Lab').grid(row=2, column=0)
labframe = ttk.Frame(r_info)
for lab in ('A', 'B', 'C'):
    ttk.Radiobutton(
        labframe,
        value=lab,
        text=lab,
        variable=variables['Lab']
    ).pack(side=tk.LEFT, expand=True)
labframe.grid(row=3, column=0, sticky=(tk.W + tk.E))

        # Plot
variables['Plot'] = tk.IntVar()
ttk.Label(r_info, text='Plot').grid(row=2, column=1)
ttk.Combobox(
    r_info,
    textvariable=variables['Plot'],
    values=list(range(1, 21))
).grid(row=3, column=1, sticky=(tk.W + tk.E))

        # Seed Sample
variables['Seed Sample'] = tk.StringVar()
ttk.Label(r_info, text='Seed Sample').grid(row=2, column=2)
ttk.Entry(
    r_info,
    textvariable=variables['Seed Sample']
).grid(row=3, column=2, sticky=(tk.W + tk.E))

    # Environment Information Frame
e_info = ttk.LabelFrame(drf, text="Environment Data") 
e_info.grid(sticky=tk.W + tk.E)
for i in range(3):
    e_info.columnconfigure(i, weight=1)
    
        # Humidity
variables["Humidity"] = tk.DoubleVar()
ttk.Label(e_info, text="Humidity (g/m3)").grid(row=0, column=0)        
ttk.Spinbox(
    e_info,
    textvariable=variables["Humidity"],
    from_=0.5,
    to=52.0,
    increment=0.01
).grid(row=1, column=0, sticky=(tk.W+tk.E))
        
        # Create the Light Field
variables["Light"] = tk.DoubleVar()
ttk.Label(e_info, text="Light (klx)").grid(row=0, column=1)
ttk.Spinbox(
    e_info,
    textvariable=variables["Light"],
    from_=0,
    to=100,
    increment=0.01
).grid(row=1, column=1, sticky=(tk.W + tk.E))

variables['Temperature'] = tk.DoubleVar()
ttk.Label(e_info, text="Temperature (C)").grid(row=0, column=2)
ttk.Spinbox(
    e_info,
    textvariable=variables['Temperature'],
    from_=4,
    to_=40, 
    increment=.01
).grid(row=1, column=2, sticky=(tk.W + tk.E))

variables['Equipment Fault'] = tk.BooleanVar(value=False)
ttk.Checkbutton(
    e_info,
    variable=variables['Equipment Fault'],
    text='Equipment Fault'
).grid(row=2, column=0, sticky=tk.W, pady=5)

# Plant Information Frame
p_info = ttk.LabelFrame(drf, text="Plant Data")
p_info.grid(sticky=(tk.W + tk.E))
for i in range(3):
    p_info.columnconfigure(i, weight=1)

# Plants
variables['Plants'] = tk.IntVar()
ttk.Label(p_info, text='Plants').grid(row=0, column=0)
ttk.Spinbox(
    p_info,
    textvariable=variables['Plants'],
    from_=0,
    to=20,
    increment=1
).grid(row=1, column=0, sticky=(tk.W + tk.E))

# Blossoms
variables['Blossoms'] = tk.IntVar()
ttk.Label(p_info, text='Blossoms').grid(row=0, column=1)
ttk.Spinbox(
    p_info,
    textvariable=variables['Blossoms'],
    from_=0,
    to=1000,
    increment=1
).grid(row=1, column=1, sticky=(tk.W + tk.E))

# Fruit
variables['Fruit'] = tk.IntVar()
ttk.Label(p_info, text='Fruit').grid(row=0, column=2)
ttk.Spinbox(
    p_info,
    textvariable=variables['Fruit'],
    from_=0,
    to=1000,
    increment=1
).grid(row=1, column=2, sticky=(tk.W + tk.E))

# Min Height
variables['Min Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Min Height (cm)').grid(row=2, column=0)
ttk.Spinbox(
    p_info,
    textvariable=variables['Min Height'],
    from_=0,
    to=1000, 
    increment=0.01
).grid(row=3, column=0, sticky=(tk.W + tk.E))

# Max Height
variables['Max Height'] = tk.DoubleVar()
ttk.Label(
    p_info,
    text='Max Height(cm)'
).grid(row=2, column=1)
ttk.Spinbox(
    p_info,
    textvariable=variables['Max Height'],
    from_=0,
    to=1000,
    increment=0.01
).grid(row=3, column=1, sticky=(tk.W + tk.E))
        
# Med Height
variables['Med Height'] = tk.DoubleVar()
ttk.Label(p_info, text='Median Height (cm)').grid(row=2, column=2)
ttk.Spinbox(
        p_info,
        textvariable=variables['Med Height'],
        from_=0,
        to=100,
        increment=0.01
        ).grid(row=3, column=2, sticky=(tk.W + tk.E))

# Notes Section
notes_inp = tk.Text(drf, widt=75, height=10)
notes_inp.grid(sticky=(tk.W + tk.E))

# Save and Reset Buttons
buttons = ttk.Frame(drf)
buttons.grid(sticky=tk.E + tk.E)
save_button = ttk.Button(buttons, text='Save')
save_button.pack(side=tk.RIGHT)

reset_button = ttk.Button(buttons, text='Reset')
reset_button.pack(side=tk.RIGHT)

root.mainloop()





























