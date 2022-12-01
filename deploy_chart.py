import matplotlib.pyplot as plt

def generate_bar_chart(labels,values,title,base):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.xlabel(base)
    plt.ylabel(title)
    plt.xticks(rotation='vertical')
    plt.show()
    
def generate_pie_chart(labels,values,title,base):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()
    
