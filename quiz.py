import tkinter
from tkinter import *
import random
import tkinter.font as font
questions = [
     "Which of the following is your first choice?",
     "Which of the following is your first choice?",
     "Suppose, You are fond of playing online CHESS, Which aspect among the following would you appreciate most? ",
     "Which of the following tasks appeals you most?",
     "Which of the following is your favorite topic?",
     "Which type of technology appeals you most?",
     "Which of the following situation appeals you most?",
     "Which of the following aspect of AMAZON company appeals you most?",
     "Which of the following is your favorite topic?",
     "Which of the following is your favorite device?",
 ]

answers_choice = [
     ["comparing prior weather with the current weather and then predicting future weather","Designing a BOT for the purpose of marketing a product","preventing a hacker from illegally extracting sensitive data of your company ","Creating a group chat WEB application","Curious to learn about approaches through which you can TEST the working of an application"],
     ["collecting information of previous year’s election results of your country and then guessing present winner","Programming a machine which can solve a problem rather than solving yourself","protecting your friend’s Facebook account in which suspicious activities are found","Creating WEB based Library Management System","Fixing the error in a newly developed Music player software"],
     ["Ability of interface of giving you statistical data of your WINNING, LOSING and DRAWING matches in the form of pie chart","its ability through which it can not only play moves against you, but can also beat you","ability of interface which ensures no 3rd person can interfere between a 2 players game","you are more fond of playing online chess in WEB browsers, rather than on smartphone app","you are curious to fix an error in which your interface hangs, whenever your opponent offers you a draw"],
     ["Comparing financial conditions of India and Pakistan through some statistical graphs and chart","Handling multiple CCTV cameras which can detect a suspicious person from some  unusual activities like standing on a place for long time without any movement etc.","Hacking your neighbor’s WIFI","converting android game “TEMPLE RUN” into a WEB application","detecting and fixing errors in a newly developed software called “ADOBE READER”"],
     ["Statistics","Designing Problem state space diagram","Topology","learning JAVASCRIPT","Software Testing Models"],
     ["Technology which analyzes purchase history of a customer and then represents it in the form of statistical data","An automated system which recommends videos to the user based on his previous searches","A technology which can trace the location of a criminal","A WEB browser which makes accessing information over internet easy and smooth","A software which determines whether a newly developed software is par to its SRS(Software requirement specification) or not "],
     ["You have to analyze the data of last year of AMAZON’s sales, so that present sales can be increased","A situation in which a robot like “SOPHIA” can interact with humans just like another human","Your friend’s online transaction failed, But still he lost his money , now you have to tackle the issue with your Cyber knowledge","You are making your own commercial website which also generates revenue","A customer got some problem with your company’s new software product that he recently bought, and now you have to fix that issue "],
     ["their ability to store, analyze and represent huge amount of customer’s requests	","()  their automated system through which they recommend various products based on customer’s interest and traces the location of product during delivery","their ability to secure large number of transactions happening daily","their WEB interface","their ability to deliver products as per the demands of a customer"],
     ["representing statistical data with graph","Solving Water- Jug problem","Routing and Internet protocol","Creating a WEB based game","Unit and integration testing"],
     ["A data analyzer and representation tool","Amazon’s ALEXA","An Antivirus software which protects and secure data","A user friendly website","A software which tests and fixes error in a newly developed application "],
 ]



graphh = [0,0,0,0,0] 

user_answer = []

indexes = []
def gen():
    global indexes
    while(len(indexes) < 10):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)
def graph():
    import matplotlib.pyplot as plt
    x=['Data Science','Machine Learning','Cyber Security','Mean Stack Developer','Software Methodology']
    plt.figure(figsize=(12,5))
    plt.bar(x,graphh)
    plt.title("Minor Recommendation Graph")
    plt.xlabel("Engineering Minors")
    plt.ylabel("Percent Recommendation")
    plt.show()

def showimage():
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    r5.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "Blue",
    )
    labelresulttext.pack()
    img = PhotoImage(file="great.png")
    labelimage.configure(image=img)
    labelimage.image = img
    labelresulttext.configure(text="Thanks for taking quiz !!")    
    button1=Button(root,text="Show Result",font="georgia 17 italic bold"
                   ,bg="light yellow",command=graph)
    button1.pack(pady=(60,100))
    


def calc():
    global indexes,user_answer,answers
    x = 0
    for i in indexes:
        if user_answer[x] == 0:
            graphh[0] += 10
        elif user_answer[x] == 1:
            graphh[1] += 10
        elif user_answer[x] == 2:
            graphh[2] += 10
        elif user_answer[x] == 3:
            graphh[3] += 10
        elif user_answer[x] == 4:
            graphh[4] += 10
        x += 1
    print(graphh)
    showimage()


ques=1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        r5['text'] = answers_choice[indexes[ques]][4]
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    





def startquiz():
    global lblQuestion,r1,r2,r3,r4,r5
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        wraplength=600,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
    
        text = answers_choice[indexes[0]][1],
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
         wraplength=600,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
         wraplength=600,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
         wraplength=600,
       command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)

    r5 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][4],
        font = ("Times", 12),
        value = 5,
        variable = radiovar,
         wraplength=1000,
        command = selected,
        background = "#ffffff",
    )
    r5.pack(pady=5)




def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root = tkinter.Tk()
root.title("Start your journey")
root.geometry("1000x1000")
root.config(background="#ffffff")
root.resizable(0,0)


img1 = PhotoImage(file="transparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background = "#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Find your interest",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="Frame.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
     border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This quiz contains 10 questions\nYou will get 40 seconds to solve a question\nOnce you select a radio button that will be a final choice\nhence think before you select",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()
