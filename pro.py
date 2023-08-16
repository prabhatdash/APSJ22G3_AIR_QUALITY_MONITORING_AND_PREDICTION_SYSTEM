import pandas as pd
import matplotlib.pyplot as plt
edf=pd.read_csv("aqi.csv")
print("Welcome to our system!!!")
print("Here you can monitor the quality of air bases on ten categories, that is PM2.5,NO,NO2,CO,SO2,O3,Benzene,Toluene,Xylene and AQI.")
print("The data can be monitored of ten different cities in India")
print("*"*46)
print("Please follow the following instructions")
print("*"*46)
print("Press 1 to see the highest value of any category")
print("Press 2 to see the lowest value of any category")
print("Press 3 to see the mean value of any category")
print("Press 4 to generate the graph of the average of any category of different cities")
print("*"*46)
r1=int(input("Enter your response:"))
# print(edf.to_markdown())
if r1==1:
    cat=input("Enter the Category:")
    print(edf[cat].max())
elif r1==2:
    cat1=input("Enter the Category:")
    print(edf[cat1].min())
elif r1==3:
    cat2=input("Enter the Category:")
    print(edf[cat2].mean())
elif r1==4:
    a1=input("Enter the category of which you want to see the average(PM2.5,NO,NO2,CO,SO2,O3,Benzene,Toluene,Xylene,AQI):")
    a=edf[edf['City']=='Ahmedabad'][a1].mean()
    b=edf[edf['City']=='Amaravati'][a1].mean()
    c=edf[edf['City']=='Amritsar'][a1].mean()
    d=edf[edf['City']=='Chandigarh'][a1].mean()
    e=edf[edf['City']=='Delhi'][a1].mean()
    f=edf[edf['City']=='Gurugram'][a1].mean()
    g=edf[edf['City']=='Hyderabad'][a1].mean()
    h=edf[edf['City']=='Kolkata'][a1].mean()
    i=edf[edf['City']=='Patna'][a1].mean()
    j=edf[edf['City']=='Visakhapatnam'][a1].mean()
    data=[a,b,c,d,e,f,g,h,i,j]
    h=["Ahmedabad","Amaravati","Amritsar","Chandigarh","Delhi","Gurugram","Hyderabad","Kolkata","Patna","Visakhapatnam"]
    plt.bar(h,data)
    plt.xlabel("States")
    plt.ylabel(a1)
    plt.show()
