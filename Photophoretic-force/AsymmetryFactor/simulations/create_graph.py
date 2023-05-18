import matplotlib.pyplot as plt
import matplotlib as mpl

colors = ['g', 'r', 'b', 'k', 'c', 'm', 'y']
line = ['','-.','--','.']

def plot_graphic(results_to_plot,
                 x_values,
                 x_label,
                 y_label,
                 title,
                 legend,
                 color_to_plot=None,
                 image_size_x = 7,
                 image_size_y = 5,
                 font_size = 12.5,
                 ):

    plt.figure(figsize=[image_size_x, image_size_y])

    if color_to_plot == None:
        aux_color = 0
        aux_line = 0

        for i in range(len(results_to_plot)):
            if aux_color == len(colors): aux_color = 0
            if aux_line == len(line): aux_line = 0
            color_line = colors[aux_color]+line[aux_line]
            
            plt.plot(x_values, results_to_plot[i], color_line, label=legend[i])
            
            aux_color = aux_color+1
            aux_line = aux_line+1

    else:
        for i in range(len(results_to_plot)):
                plt.plot(x_values, results_to_plot[i], color_to_plot[i], label=legend[i])

   
    mpl.rcParams['font.size'] = font_size
   
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.legend(loc='best')
    # plt.show()
    plt.savefig(f'./outputs/graphics/{title}.png', bbox_inches='tight')



def plot_graphic_complex(results_to_plot,
                 x_values,
                 x_label,
                 y_label,
                 title,
                 legend,
                 color_to_plot=None,
                 text = None,
                 image_size_x = 7,
                 image_size_y = 5,
                 font_size = 12.5,
                 ):

    plt.figure(figsize=[image_size_x, image_size_y])

    
    if color_to_plot == None:
        aux_color = 0
        aux_line = 0

        for i in range(len(results_to_plot)):
            if aux_color == len(colors): aux_color = 0
            if aux_line == len(line): aux_line = 0
            color_line = colors[aux_color]+line[aux_line]
            
            plt.plot(x_values, results_to_plot[i], color_line, label=legend[i])
            
            aux_color = aux_color+1
            aux_line = aux_line+1

    else:
        for i in range(len(results_to_plot)):
                plt.plot(x_values, results_to_plot[i], color_to_plot[i], label=legend[i])

    if text != None:
        for i in text:
            plt.text(i["x_loc"], i["y_loc"], i["message"])
    

    mpl.rcParams['font.size'] = font_size
   
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.legend(bbox_to_anchor=(0.5, 1.15), loc='upper center', borderaxespad=0, ncol=3)
    # plt.show()
    plt.savefig(f'./outputs/graphics/{title}.png', bbox_inches='tight')
