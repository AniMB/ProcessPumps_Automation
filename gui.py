def data_entry():
    # this created the GUI and returns the entries
    
# Author: Animish Murthy
# Date: 18/05/23
    import tkinter

    window=tkinter.Tk()
    window.title("Data entry")
    
    # create a canvas widget and configure it
    canvas = tkinter.Canvas(window)
    canvas.pack(side='left', fill="both", expand=True)
    canvas.grid_columnconfigure(0, weight=1)
    # create a frame and add some widgets to it
    frame = tkinter.Frame(canvas)


    # add the frame to the canvas
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # create a scrollbar and link it to the canvas
    scrollbar = tkinter.Scrollbar(window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # pack the scrollbar into the window
    scrollbar.pack(side="right", fill="y")

    # configure the canvas to resize with the window
    window.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    frame.pack()




#Project info 
    project_frame=tkinter.LabelFrame(frame,text="PROJECT INFO")
    project_frame.grid(row=0, column=0,sticky='ew')
# Author: Animish Murthy
# Date: 18/05/23
    type_label=tkinter.Label(project_frame, text='Type')
    type_label.grid(row=0, column=0)
    type=tkinter.Entry(project_frame)
    type.grid(row=0, column=1)

    sl_no_label=tkinter.Label(project_frame, text='Sl. No')
    sl_no_label.grid(row=2, column=0)
    sl_no=tkinter.Entry(project_frame)
    sl_no.grid(row=2, column=1)

    model_label=tkinter.Label(project_frame, text='Model')
    model_label.grid(row=3, column=0)
    model=tkinter.Entry(project_frame)
    model.grid(row=3, column=1)

    impeller_label=tkinter.Label(project_frame, text='Impeller Diameter')
    impeller_label.grid(row=4, column=0)
    impeller=tkinter.Entry(project_frame)
    impeller.grid(row=4, column=1)

    mechSeal_label=tkinter.Label(project_frame, text='Mechanical Seal')
    mechSeal_label.grid(row=5, column=0)
    mechSeal=tkinter.Entry(project_frame)
    mechSeal.grid(row=5, column=1)

    special_label=tkinter.Label(project_frame, text='Special Features')
    special_label.grid(row=7, column=0)
    special=tkinter.Entry(project_frame)
    special.grid(row=7, column=1)
    
    #provided the padding
    for widget in project_frame.winfo_children():    
        widget.grid_configure( pady=1)


#SET values
    initial_frame=tkinter.LabelFrame(frame, text="Initial pump operating Values")
    initial_frame.grid(row=1, column=0,sticky='ew')
    
# Author: Animish Murthy
# Date: 18/05/23

    def on_validate(val, label):              #checks if any value is entered or not. If ot, it will make the field red and beep
        
        if val.strip() == "":
            initial_frame.bell()  # produces a beep sound to alert the user
            label.configure(foreground='red')
            return False
        else:
            label.configure(foreground='black')
            return True
       
        def validate_integer(val,label):          # checks if the values are pure integers or not
            if val.isdigit() or (val.startswith('-') and val[1:].isdigit()):
                return True
            else:
                label.configure(foreground='blue')
                return False
            
    guageHeight_label=tkinter.Label(initial_frame, text='Guage Distance')
    guageHeight_label.grid(row=0, column=0)
    guageHeight=tkinter.Entry(initial_frame, validate="focusout", validatecommand=(initial_frame.register(lambda val: on_validate(val, guageHeight_label)), '%P'))
    guageHeight.grid(row=0, column=1)

   
    capacity_label=tkinter.Label(initial_frame, text=' Capacity')
    capacity_label.grid(row=1, column=0)
    capacity=tkinter.Entry(initial_frame, validate="focusout", validatecommand=(initial_frame.register(lambda val: on_validate(val, capacity_label)), '%P'))
    capacity.grid(row=1, column=1)

    Liquid_label=tkinter.Label(initial_frame, text='Liquid')
    Liquid_label.grid(row=2, column=0)
    Liquid=tkinter.Entry(initial_frame)
    Liquid.grid(row=2, column=1)

    Density_label=tkinter.Label(initial_frame, text='Density')
    Density_label.grid(row=3, column=0)
    Density=tkinter.Entry(initial_frame)
    Density.grid(row=3, column=1)

    effi_label=tkinter.Label(initial_frame, text='pump efficiency at duty point ')
    effi_label.grid(row=4, column=0)
    effi=tkinter.Entry(initial_frame, validate="focusout", validatecommand=(initial_frame.register(lambda val: on_validate(val, effi_label)), '%P'))
    effi.grid(row=4, column=1)

    temp_label=tkinter.Label(initial_frame, text='Temperature')
    temp_label.grid(row=5, column=0)
    temp=tkinter.Entry(initial_frame)
    temp.grid(row=5, column=1)

    bkw_label=tkinter.Label(initial_frame, text='BKW of Water')
    bkw_label.grid(row=6, column=0)
    bkw=tkinter.Entry(initial_frame, validate="focusout", validatecommand=(initial_frame.register(lambda val: on_validate(val, bkw_label)), '%P'))
    bkw.grid(row=6, column=1)

    motor_details_label=tkinter.Label(initial_frame, text='Motor: KW/HP/RPM')
    motor_details_label.grid(row=7, column=0)
    motor_details=tkinter.Entry(initial_frame, validate="focusout", validatecommand=(initial_frame.register(lambda val: on_validate(val, motor_details_label)), '%P'))
    motor_details.grid(row=7, column=1)

    head_label=tkinter.Label(initial_frame, text='Head')
    head_label.grid(row=8, column=0)
    head=tkinter.Entry(initial_frame, validate="focusout", validatecommand=(initial_frame.register(lambda val: on_validate(val, head_label)), '%P'))
    head.grid(row=8, column=1)
    
    #provided padding
    for widget in initial_frame.winfo_children():    
        widget.grid_configure( pady=1)


        
   #Testing motor details
    motor_frame=tkinter.LabelFrame(frame, text="Testing motor Values")
    motor_frame.grid(row=2, column=0, sticky='ew')
    
# Author: Animish Murthy
# Date: 18/05/23

    make_label=tkinter.Label(motor_frame, text='Make')
    make_label.grid(row=0, column=0)
    make=tkinter.Entry(motor_frame)
    make.grid(row=0, column=1)

    motor_slno_label=tkinter.Label(motor_frame, text='Motor Sl.no')
    motor_slno_label.grid(row=1, column=0)
    motor_slno=tkinter.Entry(motor_frame)
    motor_slno.grid(row=1, column=1)


    frameSize_label=tkinter.Label(motor_frame, text='FrameSize')
    frameSize_label.grid(row=2, column=0)
    frameSize=tkinter.Entry(motor_frame)
    frameSize.grid(row=2, column=1)

    rpm_label=tkinter.Label(motor_frame, text='Rpm')
    rpm_label.grid(row=3, column=0)
    rpm=tkinter.Entry(motor_frame)
    rpm.grid(row=3, column=1)

    ratedAmp_label=tkinter.Label(motor_frame, text='Rated Current')
    ratedAmp_label.grid(row=4, column=0)
    ratedAmp=tkinter.Entry(motor_frame)
    ratedAmp.grid(row=4, column=1)

    motorEffi_label=tkinter.Label(motor_frame, text='Motor Efficiency')
    motorEffi_label.grid(row=5, column=0)
    motorEffi=tkinter.Entry(motor_frame)
    motorEffi.grid(row=5, column=1)


    proj_nameLabel=tkinter.Label(motor_frame, text='Name of Customer')
    proj_nameLabel.grid(row=6, column=0)
    proj_name=tkinter.Entry(motor_frame)
    proj_name.grid(row=6, column=1)

    
    def check_entry():                            # checks if any entry is present on pressing the confirm button
        projectName = proj_name.get()
        if projectName == '':
            return None
        else:
            window.title(f"Data Entry for {projectName}")
            
    confirm_button = tkinter.Button(motor_frame, text="Confirm", command=check_entry, padx=1)
    confirm_button.grid(row=6, column=2)

    customer_WO_label=tkinter.Label(motor_frame, text='W.O.No.')
    customer_WO_label.grid(row=7, column=0)
    customer_WO=tkinter.Entry(motor_frame)
    customer_WO.grid(row=7, column=1)

    #provides padding
    for widget in motor_frame.winfo_children():    
        widget.grid_configure( pady=1)
        
    
    
   # this part can be made usable if required. Howver some changes must be made to the code   
    #RPM input                     
    '''rpm_frame=tkinter.LabelFrame(frame, text="RPM values")
    rpm_frame.grid(row=4, column=0,sticky='ew')

    rpm1_lab=tkinter.Label(rpm_frame, text=" RPM 1")
    rpm1_lab.grid(row=0, column=0)
    rpm1=tkinter.Entry(rpm_frame)
    rpm1.grid(row=1, column=0)

    rpm2_lab=tkinter.Label(rpm_frame, text='RPM 2')
    rpm2_lab.grid(row=0, column=1)
    rpm2=tkinter.Entry(rpm_frame)
    rpm2.grid(row=1, column=1 )

    rpm3_lab=tkinter.Label(rpm_frame, text='RPM 3')
    rpm3_lab.grid(row=0, column=2)
    rpm3=tkinter.Entry(rpm_frame)
    rpm3.grid(row=1, column=2)

    rpm4_lab=tkinter.Label(rpm_frame, text='RPM 4')
    rpm4_lab.grid(row=2, column=0)
    rpm4=tkinter.Entry(rpm_frame)
    rpm4.grid(row=3, column=0)

    rpm5_lab=tkinter.Label(rpm_frame, text='RPM 5')
    rpm5_lab.grid(row=2, column=1 )
    rpm5=tkinter.Entry(rpm_frame)
    rpm5.grid(row=3, column=1 )
    for widget in rpm_frame.winfo_children():    
        widget.grid_configure( pady=1)'''
        
        
        
#Additional  values
    additional_frame=tkinter.LabelFrame(frame, text="Initial Values")
    additional_frame.grid(row=4, column=0,sticky='ew')
    
# Author: Animish Murthy
# Date: 18/05/23  

    vibx_label=tkinter.Label(additional_frame,text='Vibration X')
    vibx_label.grid(row=0,column=0)
    vibx=tkinter.Entry(additional_frame)
    vibx.grid(row=0, column=1)
    
    viby_label=tkinter.Label(additional_frame,text='Vibration Y')
    viby_label.grid(row=1,column=0)
    viby=tkinter.Entry(additional_frame)
    viby.grid(row=1, column=1)
    
    vibz_label=tkinter.Label(additional_frame,text='Vibration Z')
    vibz_label.grid(row=2,column=0)
    vibz=tkinter.Entry(additional_frame)
    vibz.grid(row=2, column=1)
    # Add the vibraion values here and in funcion 'enter_data'


    def integer(value):               # returns only integer values
        try:
                integer_value = int(value)
                return integer_value
        except ValueError:
            print("Invalid integer")

    #Enters Data into system
    def enter_data():
        type_=type.get()
        sl_no_=sl_no.get() 
        model_=model.get()
        impeller_=impeller.get()
        mechSeal_=mechSeal.get()
        special_=special.get()
        guageHeight_=guageHeight.get()
        integer(guageHeight_)
        capacity_=capacity.get()
        integer(capacity_)
        Liquid_=Liquid.get()
        Density_=Density.get()
        integer(Density_)
        effi_=effi.get()
        integer(effi_)
        temp_=temp.get()
        integer(temp_)
        bkw_=bkw.get()
        head_=head.get()
        motor_details_=motor_details.get()
        make_=make.get()
        motor_slno_=motor_slno.get()
        frameSize_=frameSize.get()
        rpm_=rpm.get()
        integer(rpm_)
        ratedAmp_=ratedAmp.get()
        motorEffi_=motorEffi.get()
        integer(motorEffi_)
        projectName = proj_name.get()
        customer_WO_=customer_WO.get()
        vibx_=vibx.get()
        viby_=viby.get()
        vibz_=vibz.get()
        
        # this code can be used if RPM is in picture and the values shoulb be added to the dictionary
        '''rpm1_=rpm1.get()           
        rpm2_=rpm2.get()
        rpm3_=rpm3.get()
        rpm4_=rpm4.get()
        rpm5_=rpm5.get()'''
        
        
        
        
        dictionary = {
        'type_':type_,
        'sl_no_': sl_no_,
        'model_': model_,
        'impeller_': impeller_,
        'mechSeal_': mechSeal_,
        'special_': special_,
        'guageHeight_': guageHeight_,
        'capacity_': capacity_,
        'Liquid_': Liquid_,
        'Density_': Density_,
        'effi_': effi_,
        'temp_': temp_,
        'bkw_': bkw_,
        'head_': head_,
        'motor_details_': motor_details_,
        'make_': make_,
        'motor_slno_': motor_slno_,
        'frameSize_': frameSize_,
        'rpm_': rpm_,
        'ratedAmp_': ratedAmp_,
        'motorEffi_': motorEffi_,
        'Customer_Name_': projectName,
        'customer_WO_': customer_WO_,
        'vibx_': vibx_,
        'viby_': viby_,
        'vibz_': vibz_
        }

        
      return dictionary
      
    def exit_call():                                   #enters data into functiona and then ends the function
        enter_data()
        window.quit()
        
        
# Author: Animish Murthy
# Date: 18/05/23
     
    #the button that executes  it all
    data_entry_button=tkinter.Button(frame, text="Enter data into System", command=exit_call)
    data_entry_button.grid(row=5, column=0,  pady=10, sticky='news')
    
    window.mainloop()
    return enter_data()
    
# Author: Animish Murthy
# Date: 18/05/23


#                                        _                                               _
#                                       / \         \"""\		    /"""/       / \
# 				       /   \         \   \		   /   /       /   \
#                                     /     \         \   \		  /   /       /     \
#                                    /   _   \         \   \ 	         /   /       /   _   \
#                                   /   / \   \         \   \           /   /	    /   / \   \
#                                  /   /   \   \         \   \         /   /       /   /   \   \ 
#                                 /   /     \   \         \   \       /   /   	  /   /     \   \
#                                /    """""""    \         \   \     /   /       /    """""""    \ 
#                               /                 \	    \   \   /   /       /                 \
#                              /    /"""""""""\    \	     \   \ /   /       /    /""""""""""\   \
#                             /    /           \    \ 	      \   V   /	      /    /		\   \
#                            /    /             \    \         \     /       /    /		 \   \
#                            """""               """""          """""        """""                """"  



