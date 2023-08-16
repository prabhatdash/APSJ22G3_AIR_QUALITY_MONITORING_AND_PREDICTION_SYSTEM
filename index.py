import connector as con
import matplotlib.pyplot as plt
import pandas as pd
import auth
def registration():
    print("ENTER YOUR NAME")
    name=input()
    print("ENTER EMAIL ID")
    email=input()
    query="insert into registration (name,email) values" +"('"+name+"','"+email+"');"
    con.cursor.execute(query)
    con.dbc.commit()
    print("User has been successfully registered!!!!")
    login()



def login():
    print("ENTER THE USER ID TO LOGIN: ")
    user_id = input()
    fetch_query = "select * from registration;"
    con.cursor.execute(fetch_query)
    count = 0
    for i in con.cursor:
        if user_id == i[2]:
            count = count + 1
            print("Please wait we are sending the OTP to the given ID........")
            auth.auth(user_id)

    if count == 0:
        print("User not registered")
        registration()
    else:
        print("User Registered")
    import pro
    print("Do you eant to go back?")
    print("type Yes to go back")
    print("type No to end")
    user_input = input()
    if user_input=="Yes":
        back()
    elif user_input=="No":
        exit()

def dashboard():
    edf = pd.read_csv("aqi.csv")
    print("*" * 46)
    print("Please follow the following instructions")
    print("*" * 46)
    print("Press 1 to see the highest value of any category")
    print("Press 2 to see the lowest value of any category")
    print("Press 3 to see the mean value of any category")
    print("Press 4 to generate the graph of the average of any category of different cities")
    print("*" * 46)
    r1 = int(input("Enter your response:"))
    # print(edf.to_markdown())
    if r1 == 1:
        cat = input("Enter the Category:")
        print(edf[cat].max())
    if r1 == 2:
        cat1 = input("Enter the Category:")
        print(edf[cat1].min())
    if r1 == 3:
        cat2 = input("Enter the Category:")
        print(edf[cat2].mean())
    if r1 == 4:
        a1 = input(
            "Enter the category of which you want to see the average(PM2.5,NO,NO2,CO,SO2,O3,Benzene,Toluene,Xylene,AQI):")
        a = edf[edf['City'] == 'Ahmedabad'][a1].mean()
        b = edf[edf['City'] == 'Amaravati'][a1].mean()
        c = edf[edf['City'] == 'Amritsar'][a1].mean()
        d = edf[edf['City'] == 'Chandigarh'][a1].mean()
        e = edf[edf['City'] == 'Delhi'][a1].mean()
        f = edf[edf['City'] == 'Gurugram'][a1].mean()
        g = edf[edf['City'] == 'Hyderabad'][a1].mean()
        h = edf[edf['City'] == 'Kolkata'][a1].mean()
        i = edf[edf['City'] == 'Patna'][a1].mean()
        j = edf[edf['City'] == 'Visakhapatnam'][a1].mean()
        data = [a, b, c, d, e, f, g, h, i, j]
        h = ["Ahmedabad", "Amaravati", "Amritsar", "Chandigarh", "Delhi", "Gurugram", "Hyderabad", "Kolkata", "Patna",
             "Visakhapatnam"]
        plt.bar(h, data)
        plt.xlabel("States")
        plt.ylabel(a1)
        plt.show()
        dashboard()
print("*"*46)
print("Welcome to Air quality monitoring and ptrediction sysytem")
print("*"*46)
print("SELECT THE OPTION TO BEGIN !")
print("Press 1 to Login")
print("Press 2 to Register")

user_input=int(input())

if user_input==1:
    login()
elif user_input==2:
    registration()
