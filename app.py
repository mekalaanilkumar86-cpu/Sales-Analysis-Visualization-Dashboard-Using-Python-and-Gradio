
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import gradio as gr

data=pd.read_excel(r"C:\Users\Admin\Downloads\YEAR SALES.xlsx")
sales=data["Sales (INR)"]
profit=data["Profit (INR)"]
month=data["Month"]

def sales_visualisation(choice):
    if choice== "LINECHART":
        plt.figure(figsize=(8,6))
        plt.plot(sales,color="orange",marker="o",label="SALES",linewidth=3)
        plt.xticks(range(len(month)),month,rotation=45)
        plt.ylabel("PROFITS",fontweight="bold")
        plt.legend()
        plt.grid()
        plt.xlabel("SALES",fontweight="bold")
        plt.title("SALES & PROFITS",fontweight="bold")
        plt.show()

    elif choice == "BARCHART":
        plt.bar(range(len(sales)),sales,edgecolor="black")
        plt.xticks(range(len(month)),month,fontweight="bold",rotation=45)
        plt.xlabel("MONTHS",fontweight="bold")
        plt.ylabel("SALES(₹)",fontweight="bold")
        plt.title("SALES OF THE MONTHS",fontweight="bold")
        plt.grid(True)
        plt.show()
    
    elif choice == "PIECHART":
        plt.pie(profit,labels=month,autopct="%1.1f%%",shadow=True)
        plt.title("PROFITS OF THE MONTHS IN (%)",fontweight="bold")
        plt.show()

    elif choice == "STACKED BAR CHART":
        plt.bar(month, sales,label='Sales', color='skyblue')
        plt.bar(month,profit,label='Profit', color='orange', bottom=sales)
        plt.title('Sales and Profit Comparison by Month')
        plt.xticks(rotation=45)
        plt.xlabel('Month')
        plt.ylabel('Sales ($)')
        plt.legend()

    plt.tight_layout()
    return plt.gcf()

app=gr.Interface(
    fn=sales_visualisation,
    inputs=gr.Dropdown(
        ["LINECHART","BARCHART","PIECHART","STACKED BAR CHART"]
    ),
    outputs=gr.Plot(label="SALES VISUALISATION"),
    title="SALES ANALYSIS DASHBOARD",
    description="Select a graph to visualise sales data"
)

app.launch()
