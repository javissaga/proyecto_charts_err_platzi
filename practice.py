import matplotlib.pyplot as plt

def run():
    # Define Data
    '''
    x = [1, 2, 3, 4]
    ax1 = plt.subplot()
    ax1.set_xticks(x)
    ax1.set_yticks(x)

    # plot bar chart

    plt.bar(x,[2,3,4,12])

    # Define tick labels

    ax1.set_xticklabels(["A","B","C","D"]) 
    ax1.set_yticklabels([1, 2, 3, 4])

    plt.show()'''
    
def valuelabel(weight,students):
    for i in range(len(weight)):
        plt.text(i,students[i],students[i], ha = 'center',
                 bbox = dict(facecolor = 'cyan', alpha =0.8))
        
# Main function
  
if __name__ == '__main__':
    
    # Define data
    weight = ["35 Kg", "40 Kg", "43 Kg", "48 Kg", "65 Kg", "72    Kg"]
    students = [15, 12, 3, 5, 1, 2]
      
    # Plot bar chart
    plt.bar(weight, students, color= 'orange')
      
    # Call function
    valuelabel(weight, students)       
     
    # Define labels
    plt.xlabel("Weight of the students")
    plt.ylabel("Number of students")
      
    # Display plot
    plt.show()

if __name__ == '__main__':
    run()