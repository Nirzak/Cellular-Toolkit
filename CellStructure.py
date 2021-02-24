from tkinter import *
import tkinter.ttk as ttk
from models.CellStructures import CellStructures

def CalcCell(Frame):

    def centerWindow(width, height=200):
        # get screen width and height
        screenWidth = Frame.winfo_screenwidth()
        screenHeight = Frame.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screenHeight / 2) + (-100)
        y = (screenHeight / 2) - (height / 2)
        Frame.geometry('%dx%d+%d+%d' % (width, height, x, y))

    centerWindow(700, 600)

    #Input Variables are here
    areaSize = StringVar()
    totalTraffic = StringVar()
    cellRadius = StringVar()
    selectedCell = StringVar()
    selectedCellValue = IntVar(value=1)
    freqReuse = StringVar()

     # labels
    labelsfont = ('Times New Roman', 14)

     # text field
    textFieldFont = ('Times New Roman', 15, 'bold')

    # Heading
    labelHeading = Label(Frame,
                         text='Cellular Toolkit',
                         font="-family {Century Gothic} -size 20 -weight bold",
                         background="#1DBC60",
                         foreground="#ffffff"
                         )

    # Area Size to Cover
    labelAreaSize = Label(Frame,
                          text='Area Size to Cover (in km)',
                          font=labelsfont,
                          foreground="black")

    AreaSizeEntry = Entry(Frame,
                              width=16,
                              textvariable=areaSize,
                              justify=CENTER,
                              relief='flat',
                              foreground='#F56954',
                              font=textFieldFont)

    AreaSizeEntry.focus_force()

    # Total Traffic Channels
    labelTotalTraffic = Label(Frame,
                              text='Total Traffic Channels',
                              font=labelsfont,
                              foreground="black")

    TotalTrafficEntry = Entry(Frame,
                                  width=16,
                                  textvariable=totalTraffic,
                                  justify=CENTER,
                                  foreground='#F56954',
                                  relief='flat',
                                  font=textFieldFont)

    TotalTrafficEntry.focus_force()

    # Radius of Each Cell
    labelCellRadius = Label(Frame,
                                text='Radius of Each Cell',
                                font=labelsfont,
                                foreground="black")

    CellRadiusEntry = Entry(Frame,
                                    width=16,
                                    textvariable=cellRadius,
                                    justify=CENTER,
                                    relief='flat',
                                    foreground='#F56954',
                                    font=textFieldFont)
    CellRadiusEntry.focus_force()
    # Frequency Re-Use Factor
    labelFreqReuse = Label(Frame,
                            text='Frequency ReUse Factor',
                            font=labelsfont,
                            foreground="black")

    FreqReuseEntry = Entry(Frame,
                                width=16,
                                textvariable=freqReuse,
                                justify=CENTER,
                                relief='flat',
                                foreground='#F56954',
                                font=textFieldFont)
    # Option menu of type of city
    labelCellType = Label(Frame,
                      text='Select the type of Cell',
                      font=labelsfont,
                      foreground="black")

    cellOptions = ['Macro', 'Micro']


    def cellSelected(event):
        selectedCellValue.set(1 if selectedCell.get() == 'Macro' else 2)

    selectedCell.set(cellOptions[0])
    cellTypeOptionsMenu = OptionMenu(Frame,
                                     selectedCell,
                                     *cellOptions,
                                     command=cellSelected)
    cellTypeOptionsMenu.config(width=15)

    def getOutput():
        Output = CellStructures(
            totalArea=float(areaSize.get()),
            totalTrafficChannels=int(totalTraffic.get()),
            radiusOfCell=float(cellRadius.get()),
            frequencyReuseFactor=int(freqReuse.get()),
        )
        ttk.Label(Frame,
                  text="Number of cells required: " +
                       str(Output.numberOfCells),
                  font=textFieldFont,
                  foreground="black").grid(column=1, row=10, padx=20, pady=20)
        ttk.Label(Frame,
                  text="Number of channels per cell: " +
                       str(Output.numberOfChannelsPerCell),
                  font=textFieldFont,
                  foreground="black").grid(column=1, row=11, padx=20, pady=20)
        ttk.Label(Frame,
                  text="Total channel capacity: " +
                       str(Output.totalCapacity),
                  font=textFieldFont,
                  foreground="black").grid(column=1, row=12, padx=20, pady=20)
        ttk.Label(Frame,
                  text="Total number of possible concurrent call: " +
                       str(Output.totalNumberOfPossibleConcurrentCall),
                  font=textFieldFont,
                  foreground="black").grid(column=1, row=13, padx=20, pady=20)

    myButton3 = Button(Frame, text='Get Output',
                      command=getOutput, fg='white', bg='#F56954', relief='flat', font=labelsfont)

    labels = [labelHeading, labelAreaSize, labelTotalTraffic,
              labelCellRadius, labelFreqReuse, labelCellType, myButton3]

    fields = [AreaSizeEntry, TotalTrafficEntry,
              CellRadiusEntry, FreqReuseEntry, cellTypeOptionsMenu]


    for i in range(7):
        labels[i].grid(row=i, column=1, sticky='W', padx=20, pady=10)

    for i in range(5):
        fields[i].grid(row=i + 1, column=2)