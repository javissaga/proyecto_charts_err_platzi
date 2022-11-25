import matplotlib.pyplot as plt

def generate_bar_chart(labels,values,title,base):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.xlabel(base)
    plt.ylabel(title)
    plt.xticks(rotation='vertical')
    plt.show()
    
def generate_pie_chart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()
    
if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 500, 300]
    generate_bar_chart(labels,values)
    #generate_pie_chart(labels,values)