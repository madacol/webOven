from matplotlib import pyplot as plt

def graphJson(readings):
    data={}

    for reading in readings:
        # Initialize data structure if necessary
        if not data.__contains__(reading["name"]):
            data[reading["name"]] = {
                "input":    [],
                "setpoint": [],
                "output":   []
            }
        # Fill data
        data[reading["name"]]["input"].append(      float(reading['data']['Input']) )
        data[reading["name"]]["setpoint"].append(   float(reading['data']['Setpoint']) )
        data[reading["name"]]["output"].append(     float(reading['data']['Output']) )


    ######## NOT FINISHED - DOBULE AXIS
    # fig = plt.figure()
    # ax1 = fig.add_subplot(111)
    # ax1.plot(x, y1)
    # ax1.set_ylabel('y1')

    # ax2 = ax1.twinx()
    # ax2.plot(x, y2, 'r-')
    # ax2.set_ylabel('y2', color='r')
    # for tl in ax2.get_yticklabels():
    #     tl.set_color('r')

    # plt.savefig('images/two-scales-5.png')
    ########


    y=data['PID_top']['input']
    x=[x/60 for x in range(len(y))]
    plt.plot(x,y)
    plt.savefig("/tmp/ArduinoOven_graph.png")
    plt.clf()  #Flush data

    # Generate array of tuple for plotting multiple lines
    # array_tuples=[ [ data['PID_top']['output'][i], data['PID_top']['input'][i] ] for i in range(len(data['PID_top']['output'])) ]
    # plt.plot(array_tuples)
    # plt.show()

    # import numpy as np

    # import pdb; pdb.set_trace()