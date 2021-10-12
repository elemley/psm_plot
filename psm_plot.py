from math import *
import sympy as sympy
import numpy as np
import matplotlib.pyplot as plt

"""
UCO PSM Plotting Library

Form of functions are:

xxyyzzPlot###

xxyyzz = Plot type (Line, Scatter, etc...)

Multiple types are meant to be series on a single plot... arguments are in this same order

### =

first digit = # of rows
second digit = # of cols
third digit = # of series per plot

Arguments are in row, then column order

"""
def Function2HistPlot111(x,f,f_param_1,f_param_2,probabilities,bins,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    # plt.xlim(min(x),max(x))
    # plt.ylim(min(y), max(y))
    n, bins, patches = plt.hist(probabilities,bins,normed=True)
    y_fit = line_plot2(x, f, f_param_1, f_param_2)
    plt.plot(x, y_fit, c='r', linestyle="-", linewidth=2.0, label=ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()

def Function0HistPlot111(x,f,probabilities,bins,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    # plt.xlim(min(x),max(x))
    # plt.ylim(min(y), max(y))
    n, bins, patches = plt.hist(probabilities,bins,normed=True)
    y_fit = line_plot0(x, f)
    plt.plot(x, y_fit, c='r', linestyle="-", linewidth=2.0, label=ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()




def FunctionHistPlot111(x,f,f_param_1,probabilities,bins,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    # plt.xlim(min(x),max(x))
    # plt.ylim(min(y), max(y))
    n, bins, patches = plt.hist(probabilities,bins,normed=True)
    y_fit = line_plot1(x, f, f_param_1)
    plt.plot(x, y_fit, c='r', linestyle="-", linewidth=2.0, label=ylabel)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()



def Function2Plot111(x,f,f_param_1,f_param_2,xlabel,ylabel,title,filename):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # plot function
    y_fit = line_plot2(x, f,f_param_1,f_param_2)
    plt.plot(x, y_fit, c='r', linestyle="-", linewidth=2.0, label=ylabel)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def FunctionPlot111(x,f,f_param_1,xlabel,ylabel,title,filename):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # plot function
    y_fit = line_plot1(x, f,f_param_1)
    plt.plot(x, y_fit, c='r', linestyle="-", linewidth=2.0, label=ylabel)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def Function0Plot111(x,f,xlabel,ylabel,title,filename):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    # plot function
    y_fit = line_plot0(x, f)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y_fit), max(y_fit))
    plt.plot(x, y_fit, c='r', linestyle="-", linewidth=2.0, label=ylabel)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.grid(True)
    plt.show()




def HistPlot111(x,bins,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    # plt.xlim(min(x),max(x))
    # plt.ylim(min(y), max(y))
    n, bins, patches = plt.hist(x,bins,normed=True)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.show()





def LinePlot111(x,y,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    #plt.xlim(min(x),max(x))
    #plt.ylim(min(y), max(y))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y)
    plt.savefig(filename)
    plt.show()

def ScatterPlot111(x,y,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    plt.ylim(min(y), max(y))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.scatter(x,y)
    plt.savefig(filename)
    plt.show()

def TwoLineColorsPlot111(x,y1,y1label,y2,y2label,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    plt.ylim(ymin, ymax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',label=y1label)
    plt.plot(x, y2, c='b', label=y2label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def ThreeLineColorsPlot111(x,y1,y1label,y2,y2label,y3,y3label, xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',linestyle="-",label=y1label)
    plt.plot(x, y2, c='b', linestyle="--", label=y2label)
    plt.plot(x, y3, c='g', linestyle=":", label=y3label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def FourLineColorsPlot111(x,y1,y1label,y2,y2label,y3,y3label, y4, y4label, xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',linestyle="-",label=y1label)
    plt.plot(x, y2, c='b', linestyle="--", label=y2label)
    plt.plot(x, y3, c='g', linestyle=":", label=y3label)
    plt.plot(x, y4, c='k', linestyle="-", label=y4label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def FiveLineColorsPlot111(x,y1,y1label,y2,y2label,y3,y3label, y4, y4label, y5,y5label, xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    plt.plot(x,y1,c='r',linestyle="-",label=y1label)
    plt.plot(x, y2, c='b', linestyle="--", label=y2label)
    plt.plot(x, y3, c='g', linestyle=":", label=y3label)
    plt.plot(x, y4, c='k', linestyle="-", label=y4label)
    plt.plot(x, y5, c='m', linestyle="--", label=y5label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()


def TwoScatterColorsPlot111(x1, y1, y1label, x2, y2, y2label, xlabel, ylabel, title, filename):
    fig1 = plt.figure()
    # plt.xlim(min(x),max(x))
    # plt.ylim(min(y), max(y))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.scatter(x1, y1,label=y1label)
    plt.scatter(x2, y2,label=y2label)
    plt.legend(loc=0)
    plt.savefig(filename)
    plt.show()



def TwoDictLinePlot111(x,y1,y2,datakeys1,datakeys2,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    line_colors = ['b', 'g', 'r','c','m','y','k']
    line_styles = ['-',':','-.','--']
    linestyle_counter=0
    color_counter = 0
    for i, list_item in enumerate(datakeys1):
        list_item2=datakeys2[i]
        plt.plot(x[list_item],y1[list_item],c=line_colors[color_counter],linestyle='-',label=list_item)
        linestyle_counter += 1
        plt.plot(x[list_item], y2[list_item2], c=line_colors[color_counter], linestyle='--',label=list_item2)
        color_counter += 1
        if color_counter >= len(line_colors):
            color_counter = 0

    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()



def DictLinePlot111(x,y,datakeys,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.title(title)
    line_colors = ['b', 'g', 'r','c','m','y','k']
    line_styles = ['-',':','-.','--']
    linestyle_counter=0
    color_counter = 0
    loop_counter = 0
    for list_item in datakeys:
        plt.plot(x[list_item],y[list_item],c=line_colors[color_counter],linestyle=line_styles[linestyle_counter],label=list_item)
        if color_counter >= len(line_colors):
            linestyle_counter += 1
            color_counter = 0
        else:
            color_counter += 1
        loop_counter+=1

    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def Lin_Regress_FunctionScatterPlot111(x,xlabel,y_func,y_func_label,y_data,y_data_label,title,filename):
    fig1 = plt.figure()
    """plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    """
    plt.xlabel(xlabel)
    plt.ylabel(y_data_label)
    plt.title(title)
    plt.savefig(filename)
    #plot scatter
    plt.scatter(x,y_data,label=y_data_label)
    #plot function
    x_fit,y_fit,r2 = y_func(x,y_data,100)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", label=y_func_label+ " r^2 = " + str(round(r2,2)))
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()

def FunctionRootPlot111(x,xlabel,y_func,y_func_label,root_data,root_data_label,title,filename):
    fig1 = plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(y_func_label)
    plt.title(title)
    plt.savefig(filename)
    plt.grid(color='b',linestyle='--')

    #plot scatter
    #plt.scatter(x,y_data,label=y_data_label,s=0.5)
    #plot function
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    """
    xmin = min(x_fit)
    xmax = max(x_fit)
    ymin = min(y_fit)
    ymax = max(y_fit)
    delta_y = ymax - ymin
    """

    for i in range(0, len(root_data)):
        i_string = str(i+1)
        display_string = "$x_"+i_string+"$"
        circle = plt.text(root_data[i], 0.0, display_string, fontsize=14)
        #plt.gca().add_patch(circle)
        

    plt.legend(loc=0)
    plt.axis('auto')
    plt.savefig(filename)
    plt.show()

def FunctionRootPlot311(x,xlabel,y_func,y_func_label,root_data,root_data_label,title,filename,a_b):
    fig1 = plt.figure()
    
    labels = ['$a_1$','$b_1$','$a_2$','$b_2$','$a_3$','$b_3$']
    
    #plot function
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
        
    ax1 = plt.subplot(311)
    #plt.xlim(min(x),max(x))
    #plt.ylim(min(y1), max(y1))
    #plt.ylabel(y_func_label)
    plt.title(title)
    plt.grid(color='b',linestyle='--')
    circle = plt.text(a_b[0], 0.0, labels[0],fontsize=14)
    circle = plt.text(a_b[1], 0.0, labels[1], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    #plt.plot(x,y1)

    ax2 = plt.subplot(312,sharex=ax1)
    #plt.ylim(min(y2), max(y2))
    #plt.ylabel(y_func_label)
    plt.grid(color='b',linestyle='--')
    circle = plt.text(a_b[2], 0.0, labels[2],fontsize=14)
    circle = plt.text(a_b[3], 0.0, labels[3],fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    #plt.plot(x, y2)
    
    ax3 = plt.subplot(313,sharex=ax1)
    #plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    #plt.ylabel(ylabel)
    plt.grid(color='b',linestyle='--')
    circle = plt.text(a_b[4], 0.0, labels[4],fontsize=14)
    circle = plt.text(a_b[5], 0.0, labels[5],fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    #plt.plot(x, y3)

    plt.legend(loc=0)
    plt.axis('auto')
    plt.savefig(filename)
    plt.show()

def FunctionRootPlot411(x,xlabel,y_func,y_func_label,root_data,root_data_label,title,filename,a_b):
    fig1 = plt.figure()
    
    labels = ['$a_1$','$b_1$','$a_2$','$b_2$','$a_3$','$b_3$','$a_4$','$b_4$']
    
    #plot function
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
        
    ax1 = plt.subplot(411)
    plt.title(title)
    plt.grid(color='b',linestyle='--')
    circle = plt.text(a_b[0], 0.0, labels[0],fontsize=14)
    circle = plt.text(a_b[1], 0.0, labels[1], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    # getting current axes 
    a = plt.gca() 
    # set visibility of x-axis as False 
    xax = a.axes.get_xaxis() 
    xax = xax.set_visible(False) 
    

    ax2 = plt.subplot(412,sharex=ax1)
    plt.grid(color='b',linestyle='--')
    circle = plt.text(a_b[2], 0.0, labels[2],fontsize=14)
    circle = plt.text(a_b[3], 0.0, labels[3],fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    # getting current axes 
    a = plt.gca() 
    # set visibility of x-axis as False 
    xax = a.axes.get_xaxis() 
    xax = xax.set_visible(False) 
    
    ax3 = plt.subplot(413,sharex=ax1)
    #plt.xlabel(xlabel)
    plt.grid(color='b',linestyle='--')
    circle = plt.text(a_b[4], 0.0, labels[4],fontsize=14)
    circle = plt.text(a_b[5], 0.0, labels[5],fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    # getting current axes 
    a = plt.gca() 
    # set visibility of x-axis as False 
    xax = a.axes.get_xaxis() 
    xax = xax.set_visible(False) 
   
    ax4 = plt.subplot(414,sharex=ax1)
    plt.xlabel(xlabel)
    plt.grid(color='b',linestyle='--')
    circle = plt.text(a_b[6], 0.0, labels[6],fontsize=14)
    circle = plt.text(a_b[7], 0.0, labels[7],fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)

    plt.legend(loc=0)
    plt.axis('auto')
    plt.savefig(filename)
    plt.show()

def FunctionRootPlot411_regula_falsa(x,xlabel,y_func,y_func_label,root_data,root_data_label,title,filename,a_b):
    fig1 = plt.figure()
    
    labels = ['$a_1$','$b_1$','$a_2$','$b_2$','$a_3$','$b_3$','$a_4$','$b_4$']
    root_labels = ['$ x_{root_1}$','$x_{root_2}$','$x_{root_3}$','$x_{root_4}$']
    #plot function
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
    
        
    ax1 = plt.subplot(411)
    plt.title(title)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[0],a_b[1]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[0], 0.0, labels[0],fontsize=14)
    circle = plt.text(a_b[1], -4.0, labels[1], fontsize=14)
    circle = plt.text(root_data[2], -4.0, root_labels[0], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    # getting current axes 
    a = plt.gca() 
    # set visibility of x-axis as False 
    xax = a.axes.get_xaxis() 
    xax = xax.set_visible(False) 
    

    ax2 = plt.subplot(412,sharex=ax1)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[2],a_b[3]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[2], 0.0, labels[2],fontsize=14)
    circle = plt.text(a_b[3], 0.0, labels[3],fontsize=14)
    circle = plt.text(root_data[3], -4.0, root_labels[1], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    # getting current axes 
    a = plt.gca() 
    # set visibility of x-axis as False 
    xax = a.axes.get_xaxis() 
    xax = xax.set_visible(False) 
    
    ax3 = plt.subplot(413,sharex=ax1)
    #plt.xlabel(xlabel)
    plt.grid(color='b',linestyle='--')    
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[4],a_b[5]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[4], 0.0, labels[4],fontsize=14)
    circle = plt.text(a_b[5], 0.0, labels[5],fontsize=14)
    circle = plt.text(root_data[4], -4.0, root_labels[2], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    # getting current axes 
    a = plt.gca() 
    # set visibility of x-axis as False 
    xax = a.axes.get_xaxis() 
    xax = xax.set_visible(False) 
   
    ax4 = plt.subplot(414,sharex=ax1)
    plt.xlabel(xlabel)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[6],a_b[7]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[6], 0.0, labels[6],fontsize=14)
    circle = plt.text(a_b[7], 0.0, labels[7],fontsize=14)
    circle = plt.text(root_data[5], -4.0, root_labels[3], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)

    #plt.legend(loc=0)
    plt.axis('auto')
    plt.savefig(filename)
    plt.show()

def FunctionRootPlot141_regula_falsa(x,xlabel,y_func,y_func_label,root_data,root_data_label,title,filename,a_b):
    fig1 = plt.figure()
    
    labels = ['$a_1$','$b_1$','$a_2$','$b_2$','$a_3$','$b_3$','$a_4$','$b_4$']
    root_labels = ['$ x_{root_1}$','$x_{root_2}$','$x_{root_3}$','$x_{root_4}$']
    #plot function
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
    
        
    ax1 = plt.subplot(141)
    plt.title(title)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[0],a_b[1]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[0], 0.0, labels[0],fontsize=14)
    circle = plt.text(a_b[1], -4.0, labels[1], fontsize=14)
    circle = plt.text(root_data[2], -1.0, root_labels[0], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    plt.xlabel(xlabel)
    plt.ylabel(y_func_label)
    #plt.legend(loc=0)
    plt.axis('auto')
    

    ax2 = plt.subplot(142)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[2],a_b[3]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[2], 0.0, labels[2],fontsize=14)
    circle = plt.text(a_b[3], 0.0, labels[3],fontsize=14)
    circle = plt.text(root_data[3], -1.0, root_labels[1], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    plt.xlabel(xlabel)
    plt.ylabel(y_func_label)
    plt.legend(loc=0)
    plt.axis('auto')

    
    ax3 = plt.subplot(143)
    #plt.xlabel(xlabel)
    plt.grid(color='b',linestyle='--')    
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[4],a_b[5]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[4], 0.0, labels[4],fontsize=14)
    circle = plt.text(a_b[5], 0.0, labels[5],fontsize=14)
    circle = plt.text(root_data[4], -1.0, root_labels[2], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    plt.xlabel(xlabel)
    plt.ylabel(y_func_label)
    plt.legend(loc=0)
    plt.axis('auto')

    
    ax4 = plt.subplot(144)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-0.5*abs(min(y_fit)), max(y_fit)+0.5*abs(max(y_fit)))
    xrg = [a_b[6],a_b[7]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[6], 0.0, labels[6],fontsize=14)
    circle = plt.text(a_b[7], 0.0, labels[7],fontsize=14)
    circle = plt.text(root_data[5], -1.0, root_labels[3], fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    
    plt.xlabel(xlabel)
    plt.ylabel(y_func_label)
    plt.legend(loc=0)
    plt.axis('auto')

    
    plt.savefig(filename)
    plt.show()


def FunctionRootPlot111_regula_falsa(x,xlabel,y_func,y_func_label,root_data,root_data_label,title,filename,a_b,iteration):
    fig1 = plt.figure()
    iter_str = f'{str(iteration)}'
    a_label = '$a_'+iter_str+'$'
    b_label = '$b_'+iter_str+'$'
    x_root_label_1 = '$x_'
    x_root_label_2 = '{root_'
    x_root_label_end = '}$'
    x_root_label = x_root_label_1 + x_root_label_2 +iter_str+x_root_label_end
    #s = ['$a_1$'_1,'$b_1$','$a_2$','$b_2$','$a_3$','$b_3$','$a_4$','$b_4$']
    #root_labels = ['$x_{root_1}$','$x_{root_2}$','$x_{root_3}$','$x_{root_4}$']
    #plot function
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
    
    y_percent = 0.2
    x_percent = 0.05
    y_offset = y_percent*(max(y_fit)-min(y_fit))
    x_offset = x_percent*(max(x_fit)-min(x_fit))
    plt.title(title)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-y_offset, max(y_fit)+y_offset)
    xrg = [a_b[2*(iteration-1)],a_b[2*(iteration-1)+1]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    #print(abs(root_data[iteration+1] - xrg[0]),abs(root_data[iteration+1] - xrg[1]),x_offset)
    if abs(root_data[iteration+1] - xrg[1]) < x_offset or abs(root_data[iteration+1] - xrg[0]) < x_offset:
        root_y_offset = y_offset
    else:
        root_y_offset = -y_offset/4
    plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    circle = plt.text(a_b[2*(iteration-1)], yrg[0]-y_offset/4, a_label,fontsize=14)
    circle = plt.text(a_b[2*(iteration-1)+1], yrg[1]-y_offset/4, b_label, fontsize=14)
    circle = plt.text(root_data[iteration+1], root_y_offset, x_root_label, fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    plt.xlabel(xlabel)
    plt.ylabel(y_func_label)
    plt.grid(color='b',linestyle='--')
    plt.legend(loc=0)
    plt.axis('auto')
    plt.savefig(filename)
    plt.show()

    
def FunctionRootPlot111_newton_raphson(x,xlabel,y_func,y_func_label,root_data,root_data_label,title,filename,iteration):
    fig1 = plt.figure()
    iter_str_i = f'{str(iteration)}'
    iter_str_i_plus_1 = f'{str(iteration+1)}'
    xi_label = '$x_'+iter_str_i+'$'
    xi_plus_1_label = '$x_'+iter_str_i_plus_1+'$'
    fi_label = '$f('+xi_label+')$'
    fi_plus_1_label = '$f('+xi_plus_1_label+')$'
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
    
    y_percent = 0.2
    x_percent = 0.05
    y_offset = y_percent*(max(y_fit)-min(y_fit))
    x_offset = x_percent*(max(x_fit)-min(x_fit))
    plt.title(title)
    plt.grid(color='b',linestyle='--')
    plt.ylim(min(y_fit)-y_offset, max(y_fit)+y_offset)
    xi = root_data[iteration-1]
    xi_plus_1 = root_data[iteration]
    fxi = y_func(xi)
    fxi_plus_1= y_func(xi_plus_1)
    dx = xi_plus_1 - xi
    dy = -fxi
    """
    xrg = [a_b[2*(iteration-1)],a_b[2*(iteration-1)+1]]
    yrg = [y_func(xrg[0]),y_func(xrg[1])]
    if abs(root_data[iteration+1] - xrg[1]) < x_offset or abs(root_data[iteration+1] - xrg[0]) < x_offset:
        root_y_offset = y_offset
    else:
        root_y_offset = -y_offset/4
    """
    plt.arrow(xi,fxi,dx,dy,color='g',width=.05)
    #plt.plot(xrg,yrg,c='g', linestyle='--',linewidth=2.0)
    #circle = plt.text(a_b[2*(iteration-1)], yrg[0]-y_offset/4, a_label,fontsize=14)
    #circle = plt.text(a_b[2*(iteration-1)+1], yrg[1]-y_offset/4, b_label, fontsize=14)
    #circle = plt.text(root_data[iteration+1], root_y_offset, x_root_label, fontsize=14)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    plt.xlabel(xlabel)
    plt.ylabel(y_func_label)
    plt.grid(color='b',linestyle='--')
    plt.legend(loc=0)
    plt.axis('auto')
    plt.savefig(filename)
    plt.show()


def FunctionScatterPlot111(x,xlabel,y_func,y_func_label,y_data,y_data_label,title,filename):
    fig1 = plt.figure()
    """plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    """
    plt.xlabel(xlabel)
    plt.ylabel(y_data_label)
    plt.title(title)
    plt.savefig(filename)
    #plot scatter
    plt.scatter(x,y_data,label=y_data_label,s=0.5)
    #plot function
    n=200
    x_fit,y_fit = line_plot(x,y_func,n)
    plt.plot(x_fit, y_fit, c='r', linestyle="-", linewidth=2.0, label=y_func_label)
    plt.savefig(filename)
    plt.legend(loc=0)
    plt.show()



def LineScatterPlot111(x,y1,y2,xlabel,ylabel,title,filename):
    fig1 = plt.figure()
    plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    plt.ylim(ymin, ymax)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.plot(x,y1)
    plt.scatter(x,y2)
    plt.savefig(filename)
    plt.show()


def LinePlot211(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(211)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(212,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    plt.savefig(filename)
    plt.show()

def LinePlot121(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(121)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(122,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    plt.savefig(filename)
    plt.show()



def LinePlot311(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(311)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(312,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.ylabel(y2label)
    plt.plot(x, y2)

    ax3 = plt.subplot(313,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.plot(x, y3)

    plt.savefig(filename)
    plt.show()

def LinePlot131(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(131)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.plot(x,y1)

    ax2 = plt.subplot(132,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.plot(x, y2)

    ax3 = plt.subplot(133,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.plot(x, y3)
    plt.savefig(filename)
    plt.show()





def ScatterPlot211(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(211)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(212,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    plt.savefig(filename)
    plt.show()

def ScatterPlot121(x,y1,y2,xlabel,y1label,y2label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(121)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(122,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    plt.savefig(filename)
    plt.show()



def ScatterPlot311(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(311)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(312,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    ax3 = plt.subplot(313,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.scatter(x, y3)

    plt.savefig(filename)
    plt.show()

def ScatterPlot131(x,y1,y2,y3,xlabel,y1label,y2label,y3label,title,filename):
    fig1 = plt.figure()
    #ax1 = fig1.add_subplot(3,1,1)
    #ax2 = fig1.add_subplot(3, 1, 2)
    #ax3 = fig1.add_subplot(3, 1, 3)

    ax1 = plt.subplot(131)
    plt.xlim(min(x),max(x))
    plt.ylim(min(y1), max(y1))
    plt.xlabel(xlabel)
    plt.ylabel(y1label)
    plt.title(title)
    plt.scatter(x,y1)

    ax2 = plt.subplot(132,sharex=ax1)
    plt.ylim(min(y2), max(y2))
    plt.xlabel(xlabel)
    plt.ylabel(y2label)
    plt.scatter(x, y2)

    ax3 = plt.subplot(133,sharex=ax1)
    plt.ylim(min(y3), max(y3))
    plt.xlabel(xlabel)
    plt.ylabel(y3label)
    plt.scatter(x, y3)
    plt.savefig(filename)
    plt.show()



def line_plot(x,f1,n):
    x_start = float(min(x))
    x_end = float(max(x))
    x_fit = [x_start]
    dx = (x_end-x_start)/float(n)
    y_fit = [f1(x_start)]
    for i in range(1,n):
        x_curr = x_start+i*dx
        x_fit.append(x_curr)
        y_fit.append(f1(x_curr))

    return (x_fit, y_fit)

def line_plot1(x,f1,param_1):
    y = []
    for xval in x:
        y.append(f1(xval,param_1))

    return (y)


def line_plot0(x,f1):
    y = []
    for xval in x:
        y.append(f1(xval))

    return (y)


def line_plot2(x,f1,param_1,param_2):
    #y = [f1(x[0],param_1,param_2)]
    y = []
    for xval in x:
        y.append(f1(xval,param_1,param_2))

    return (y)





"""
    plt.xlim(min(x),max(x))
    if min(y1)<min(y2):
        ymin = min(y1)
    else:
        ymin = min(y2)
    if max(y1) > max(y2):
        ymax = max(y1)
    else:
        ymax = max(y2)
    plt.ylim(ymin, ymax)
    """