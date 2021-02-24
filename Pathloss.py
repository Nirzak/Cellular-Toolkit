from tkinter import *
import tkinter.ttk as ttk
from models.OkumaraHata import OkumaraHataModel

#Second Window Function
def CalcPathLoss(Frame):
    def centerWindow(width, height=200):
        # get screen width and height
        screenWidth = Frame.winfo_screenwidth()
        screenHeight = Frame.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screenHeight / 2) + (-100)
        y = (screenHeight / 2) - (height / 2)
        Frame.geometry('%dx%d+%d+%d' % (width, height, x, y))


    centerWindow(700, 600)


    # Input Variables are here
    carrierFreq = StringVar()
    antennaheight1 = StringVar()
    antennaheight2 = StringVar()
    propagationDistance = StringVar()
    selectedCity = StringVar()
    selectedArea = StringVar()
    selectedCityValue = IntVar(value=1)
    selectedAreaValue = IntVar(value=1)

     # labels
    labelsfont = ('Times New Roman', 14)

     # text filed
    textFieldFont = ('Times New Roman', 15, 'bold')

    # Heading
    labelHeading = Label(Frame,
                     text='Cellular Toolkit',
                     font="-family {Century Gothic} -size 20 -weight bold",
                     background="#1DBC60",
                     foreground="#ffffff"
                     )

    # carrier frequency
    labelCarrierFrequency = Label(Frame,
                              text='Value of carrier frequency (in range 150-1500MHz)        :',
                              font=labelsfont,
                              foreground="black")

    carrierFrequencyField = Entry(Frame, width=16, textvariable=carrierFreq,
                                  justify=CENTER,
                                  relief='flat',
                                  foreground='#F56954',
                                  font=textFieldFont)

    carrierFrequencyField.focus_force()

    # height of transmitter antenna
    labelantennaheightT = Label(Frame,
                            text='Height of transmitter antenna(in range 30 - 300 meter)    :',
                            font=labelsfont,
                            foreground="black")

    antennaheightFieldT = Entry(Frame,
                                width=16,
                                textvariable=antennaheight1,
                                justify=CENTER,
                                relief='flat',
                                foreground='#F56954',
                                font=textFieldFont)

    antennaheightFieldT.focus_force()

    # height of receiver antenna
    labelAntennaheightR = Label(Frame,
                            text='Height of receiver antenna (in range 1 - 10 meter)           :',
                            font=labelsfont,
                            foreground="black")

    antennaheightFieldR = Entry(Frame,
                                width=16,
                                textvariable=antennaheight2,
                                justify=CENTER,
                                relief='flat',
                                foreground='#F56954',
                                font=textFieldFont)
    antennaheightFieldR.focus_force()

    # Propagation distance
    labelPropagationDistance = Label(Frame,
                                     text='Propagation distance between antennas (1 - 20 in km) :',
                                     font=labelsfont,
                                     foreground="black")

    propagationDistanceField = Entry(Frame,
                                     width=16,
                                     textvariable=propagationDistance,
                                     justify=CENTER,
                                     relief='flat',
                                     foreground='#F56954',
                                     font=textFieldFont)

    propagationDistanceField.focus_force()

     # Option menu of type of city
    labelCityType = Label(Frame,
                      text='Select the type of city',
                      font=labelsfont,
                      foreground="black")

    cityOptions = ['Small/Medium', 'Large']


    def citySelected(event):
        selectedCityValue.set(1 if selectedCity.get() == 'Small/Medium' else 2)

    selectedCity.set(cityOptions[0])
    cityTypeOptionsMenu = OptionMenu(Frame,
                                     selectedCity,
                                     *cityOptions,
                                     command=citySelected)
    cityTypeOptionsMenu.config(width=15)

    # Option menu of type of area
    labelAreaType = Label(Frame,
                          text='Select the type of area',
                          font=labelsfont,
                          foreground="black")

    areaOptions = ['Urban/Suburban', 'Open area']


    def areaSelected(event):
        selectedAreaValue.set(1 if selectedArea.get() == 'Urban/Suburban' else 2)


    selectedArea.set(areaOptions[0])

    areaTypeOptionsMenu = OptionMenu(Frame,
                                     selectedArea,
                                     *areaOptions,
                                     command=areaSelected)
    areaTypeOptionsMenu.config(width=15)


    def getPathLoss():
        okumara_hata_model = OkumaraHataModel(
            carrierFrequency=int(carrierFreq.get()),
            heightTransmitter=int(antennaheight1.get()),
            heightReceiver=int(antennaheight2.get()),
            linkDistance=int(propagationDistance.get()),
            city=selectedCityValue.get(),
            area=selectedAreaValue.get())

        ttk.Label(Frame,
                  text="Path loss (in dB):" +
                       str(okumara_hata_model.pathLoss) + 'dB',
                  font=textFieldFont,
                  foreground="black").grid(column=1, row=12, padx=20, pady=20)


    myButton = Button(Frame, text='Get Path Loss',
                      command=getPathLoss, fg='white', bg='#F56954', relief='flat', font=labelsfont)

    labels = [labelHeading, labelCarrierFrequency, labelantennaheightT,
              labelAntennaheightR, labelPropagationDistance, labelCityType, labelAreaType, myButton]

    fields = [carrierFrequencyField, antennaheightFieldT,
              antennaheightFieldR, propagationDistanceField, cityTypeOptionsMenu, areaTypeOptionsMenu]


    for i in range(8):
        labels[i].grid(row=i, column=1, sticky='W', padx=20, pady=10)

    for i in range(6):
        fields[i].grid(row=i + 1, column=2)