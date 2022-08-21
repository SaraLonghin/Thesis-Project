#The tool replicates the "plotnet" function of the NeuralNetTools R package.
#As basis for plotting nodes and connections and find right positioning it has been used the code at https://gist.github.com/craffel/2d727968c3aaebd10359

import matplotlib.pyplot as plt

def draw_neural_net(layer_sizes, weights, color='lightblue', color_pos_weights='black', color_neg_weights='grey', x_names=None, y_names=None, node_text=False, epoch=None, pruned=False, transparency=0.5, fontsize=20, fontsize_node=15, figsize=(50, 50), save_file=None):
    '''
        
************************************* 
    Originally required parameters: *
*************************************     
        - ax : matplotlib.axes.AxesSubplot
            The axes on which to plot the cartoon (get e.g. by plt.gca())
        - left : float
            The center of the leftmost node(s) will be placed here
        - right : float
            The center of the rightmost node(s) will be placed here
        - bottom : float
            The center of the bottommost node(s) will be placed here
        - top : float
            The center of the topmost node(s) will be placed here
        - layer_sizes : list of int
            List of layer sizes, including input and output dimensionality

********************
   Parameters now: *
********************
       - layer_sizes --> structure of the network. List (int) of layer sizes, including input and output dimensionality
       
       - weights --> list of network's parameters
       
       - color (optional) --> color of nodes fill. Default is 'lightlue'
       
       - color_pos_weights (optional) --> color of positive connections. Default is 'black'
       
       - color_neg_weights (optional) --> color of negative connections. Default is 'grey'
       
       - x_names (optional) --> names of input variables. Deafult "I1..n" , n= number of input nodes nodes
       
       - y_names (optional) --> names of output variables. Deafult "O1..n" , n= number of output nodes
       
       - node_text (optional) --> plot labels or not. Default is False 
         - Use of node_text is discouraged for big networks.
       
       - epoch (optional) --> number of iteration, used as plot's title. 
       
       - pruned (optional) --> show pruned connection. Default is False.
       
       - transparency (optional) --> set transparency of connections. Range is (0,1), where 0 is max transparency. Default is 0.5
         - Use of high transparency is discouraged without changing color_pos_weights and/or color_neg_weights. 
       
       - fontsize (optional) --> fontsize of layers labels and title. Default is 20 
         - fontsize has to be adjusted depending on network size 
        
       - fontsize_node (optional) --> fontsize of nodes labels. Default is 15
         
       - figsize --> parameters of figsize by Matplotlib to set image size. Default is (50,50)
         - figsize has to be adjusted depending on network size.
         
       - save_file (optional) --> save in the specified name and format.
********   
Usage: *
******** 
 >>> draw_neural_net([20,15,20],weights_list)            
   '''

    left = 0.1
    right = 0.9
    bottom = 0.1
    top = 0.9
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)

    fig = plt.figure(figsize=figsize)
    ax = fig.gca()
    ax.axis('off')
    
    if epoch != None:
        plt.title('Epoch' + str(epoch), fontsize=50)
    else:
        None

    def do_linewidth(x):
        if x > 0.0:
            linewidth = 10*x
            return linewidth

    def do_linestyle(x):
        if x == 0.0:
            linestyle = '--'
            return linestyle
        else:
            linestyle = '-'
            return linestyle

    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        if n == 0:
            plt.text(n*h_spacing+0.08, layer_top +
                     0.05, 'Input Layer', fontsize=fontsize)
        elif n == n_layers - 1:
            plt.text(n*h_spacing+0.08, layer_top +
                     v_spacing, 'Output Layer', fontsize=fontsize)
        else:
            plt.text(n*h_spacing+0.08, layer_top +
                     v_spacing, 'Hidden Layer', fontsize=fontsize)
        for m in range(layer_size):
            circle = plt.Circle((n*h_spacing + left, layer_top - m*(v_spacing + 0.0001)), v_spacing/2.5,
                                color=color, ec='k', clip_on=False, zorder=4, fill=True)

            # add input(x_names) and output(y_names) labels
            if node_text == True:
                if n == 0:
                    if x_names:
                        plt.text(left-0.03, layer_top - m*v_spacing,
                                 str(x_names[m]), fontsize=fontsize_node)
                    else:
                       plt.text(left-0.03, layer_top - m*v_spacing,
                                r'$I_{'+str(m+1)+'}$', fontsize=fontsize_node)

                elif n == n_layers - 1:
                    if y_names:
                        plt.text(n*h_spacing + left+0.02, layer_top -
                                 m*v_spacing, str(y_names[m]), fontsize=fontsize_node)
                    else:
                        plt.text(n*h_spacing + left + 0.02, layer_top -
                                 m*v_spacing, r'$O_{'+str(m+1)+'}$', fontsize=fontsize_node)
                else:
                    plt.text(n*h_spacing + left + 0.02, layer_top -
                             m*v_spacing, r'$H_{'+str(m+1)+'}$', fontsize=fontsize_node)
            else:
                None

            ax.add_patch(circle)
    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                weight = weights[n][m, o]

                #plot magnitude of connection weights shown through the width of the line
                abs_weight = abs(weight)
                linewidth = do_linewidth(abs_weight)

                linestyle = do_linestyle(weight)

                #plot different colors based on sign of the weight and wether it is 0 weight
                if weight > 0:
                    color = color_pos_weights

                    line_pos = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                          [layer_top_a - m*(v_spacing + 0.0001), layer_top_b - o*(v_spacing + 0.0001)], linestyle=linestyle, linewidth=linewidth, c=color, clip_on=False, alpha=transparency)
                    ax.add_artist(line_pos)

                elif weight < 0:
                    color = color_neg_weights

                    line_neg = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                          [layer_top_a - m*(v_spacing + 0.0001), layer_top_b - o*(v_spacing + 0.0001)], linestyle=linestyle, linewidth=linewidth, c=color, clip_on=False, alpha=transparency)
                    ax.add_artist(line_neg)

                else:
                    if pruned == True:
                        color = 'lightblue'

                        line_pruned = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                                 [layer_top_a - m*(v_spacing + 0.0001), layer_top_b - o*(v_spacing + 0.0001)], linestyle=linestyle, linewidth=1.5, c=color, clip_on=False)
                        ax.add_artist(line_pruned)

                    else:
                        None

            #Custom legend for linewidth
            legend_elements = [plt.Line2D([0], [0], color='black', lw=1, label='weight between (0.0, 0,2]'),
                               plt.Line2D([0], [0], color='black', lw=3,
                                          label='weight between (0.2, 0,4]'),
                               plt.Line2D([0], [0], color='black', lw=5,
                                          label='weight between (0.4, 0,6]'),
                               plt.Line2D([0], [0], color='black', lw=7,
                                          label='weight between (0.6, 0,8]'),
                               plt.Line2D([0], [0], color='black', lw=9, label='weight > 0,8')]

            #Custom legend for connections' color
            legend_colors = [plt.Line2D([0], [0], color=color_pos_weights, lw=5, label='positive connection'),
                             plt.Line2D([0], [0], color=color_neg_weights, lw=5, label='negative connection'), ]

            leg1 = ax.legend(handles=legend_elements,
                             loc='upper left', fontsize=20)

            ax.legend(handles=legend_colors,
                      loc='upper right', fontsize=30)

            ax.add_artist(leg1)
    #save plot
    if save_file != None:
        fig.savefig(save_file, bbox_inches='tight', pad_inches=0)
    else:
        plt.savefig('nn' + str(epoch) + '.svg',
                    bbox_inches='tight', pad_inches=0)
