import os
import random
from tkinter import *
import tkinter
import PIL.Image
import PIL.ImageTk

tk = tkinter

num_lines = 0
name_num = 0
names_list: list = [" "]
win_width = 800
win_height = 600
randomized_list:list

score=0

class Main:
    print("Test Print")

    def thewindow():
        global num_lines,name_num, names_list, randomized_list
        window = Tk()
        window.config(width=win_width,
                      height=win_height)

        # Country Reading
        def addcountries(choice):
            if (choice == "reg1"):
                names_file = "regions/reg1.txt"  # Asia
            elif (choice == "reg2"):
                names_file = "regions/reg2.txt"  # Europe
            elif (choice == "reg3"):
                names_file = "regions/reg3.txt"  # Americas
            elif (choice == "reg4"):
                names_file = "regions/reg4.txt"  # Africa
            elif (choice == "reg5"):
                names_file = "regions/reg5.txt"  # Oceania
            elif (choice == "reg6"):
                names_file = "regions/reg6.txt"  # World
            else:
                print("Invalid region code")
                return

            global num_lines, names_list
            opened_file = open(names_file, "r")
            names_list += opened_file.readlines()

            reopened_file = open(names_file, "r")
            name_num = int(sum(1 for line in reopened_file))
            num_lines += name_num

        # Country Reading

        # Choosing a region
        def list_countries(region, number,lownumber, highnumber):
            choice_order = ["", "End"]
            choice_order[0] = region
            order_length = len(choice_order)

            choicelist: list = [""]
            choose_loop = 0
            while choose_loop != order_length:
                print("Region input:")
                print(choice_order[choose_loop])
                choice = choice_order[choose_loop]
                print(choose_loop)
                print(order_length)

                if choice not in choicelist:
                    choicelist.append(choice)
                    if (choice != "End"):
                        addcountries(choice)
                        choose_loop += 1
                    elif (choice == "End"):
                        choose_loop += 1
                else:
                    print("Already given")
                # Choosing a region

                # Prints number of countries
                print("Number of lines read:\t", num_lines)
                print("Number of listed names:\t", len(names_list))
                # Prints number of countries

                # Lists countries and their assigned code
                z = 0
                while z != len(names_list):
                    print(z, ";", names_list[z])
                    z += 1
            # Lists countries and their assigned code

            # Prints final numbers
            print("Number of lines read:\t", num_lines)
            print("Number of listed names:\t", len(names_list))
            # Prints final numbers

            # Randomizes country codes
            global randomized_list
            randomized_list = random.sample(range(lownumber, highnumber), number)

            y = 0
            while y != number:
                print(randomized_list[y], ";", names_list[randomized_list[y]])
                y += 1

            # Randomizes country codes

            # z = 0
            # while z != len(names_list):
            #    print(z, ";", names_list[z])
            #    z += 1

        # Call Main Window
        def mainwindow():
            tframeheight = int((win_height/3)*2)
            title_frame = Frame(width=win_width,
                                height=tframeheight)
            title_label = Label(master=title_frame,
                                text="World Geography Quiz",
                                font=("Ubuntu", 50)
                                )
            title_label.place(x=(win_width / 2),
                              y=tframeheight / 2,
                              anchor=CENTER)

            bframeheight = int(win_height/3)
            button_frame = Frame(width=win_width,
                                 height=bframeheight)

            button_start = Button(master=button_frame,
                                  width=7,
                                  height=2,
                                  borderwidth=1,
                                  image="",
                                  text="Start",
                                  font=("Ubuntu", 30),
                                  command=lambda:[destroymain(),
                                                  selectwindow()]
                                  )
            button_start.place(x=win_width / 2,
                               y=bframeheight / 2,
                               anchor=CENTER)

            title_frame.pack()
            button_frame.pack()
            # Destroy Main Window
            def destroymain():
                title_frame.destroy()
                button_frame.destroy()

                # Call Selector Window
        def selectwindow():

            def destroyselect():
                select_frame.destroy()


            v_Picture = PIL.Image.open("onePix.png", "r")
            onePix = PIL.ImageTk.PhotoImage(v_Picture)

            select_frame = Frame(width=win_width,
                                 height=win_height)
            sel_button1 = Button(master=select_frame, text="Europe", image=onePix,
                                 width=200, height=210, compound="c",
                                 command=lambda:[destroyselect(),
                                                 choice_1(),
                                                 quizWin()]).grid(column=0, row=0)
            sel_label1 = Label(master=select_frame,
                               text=" ", image=onePix,
                                 width=200, height=20, compound="c").grid(column=0, row=1)
            sel_button2 = Button(master=select_frame,
                                 text="Asia", image=onePix,
                                 width=200, height=210, compound="c",
                                 command=lambda:[destroyselect(),
                                                 choice_2(),
                                                 quizWin()]).grid(column=1, row=0)
            sel_label2 = Label(master=select_frame,
                               text=" ", image=onePix,
                                 width=200, height=20, compound="c").grid(column=1, row=1)
            sel_button3 = Button(master=select_frame,
                                 text="Americas", image=onePix,
                                 width=200, height=210, compound="c",
                                 command=lambda:[destroyselect(),
                                                 choice_3(),
                                                 quizWin()]).grid(column=2, row=0)
            sel_label3 = Label(master=select_frame,
                               text=" ", image=onePix,
                                 width=200, height=20, compound="c").grid(column=2, row=1)
            sel_button4 = Button(master=select_frame,
                                 text="Africa", image=onePix,
                                 width=200, height=210, compound="c",
                                 command=lambda:[destroyselect(),
                                                 choice_4(),
                                                 quizWin()]).grid(column=0, row=2)
            sel_label4 = Label(master=select_frame,
                               text=" ", image=onePix,
                                 width=200, height=20, compound="c").grid(column=0, row=3)
            sel_button5 = Button(master=select_frame,
                                 text="World", image=onePix,
                                 width=200, height=210, compound="c",
                                 command=lambda:[destroyselect(),
                                                 choice_6(),
                                                 quizWin()]).grid(column=1, row=2)
            sel_label5 = Label(master=select_frame,
                               text=" ", image=onePix,
                                 width=200, height=20, compound="c").grid(column=1, row=3)
            sel_button6 = Button(master=select_frame,
                                 text="Oceania", image=onePix,
                                 width=200, height=210, compound="c",
                                 command=lambda:[destroyselect(),
                                                 choice_5(),
                                                 quizWin()]).grid(column=2, row=2)
            sel_label6 = Label(master=select_frame,
                               text=" ", image=onePix,
                                 width=200, height=20, compound="c").grid(column=2, row=3)

            select_frame.pack()
            select_frame.mainloop()
            # Call Selector Window
            # Destroy Main Window
            # Call Main Window

        def choice_1():#Europe
            send_choice = "reg6"
            list_countries(send_choice, 20, 49, 92)
        def choice_2():#Asia
            send_choice = "reg6"
            list_countries(send_choice, 20, 1, 48)
        def choice_3():#Americas
            send_choice = "reg6"
            list_countries(send_choice, 15, 93, 127)
        def choice_4():#Africa
            send_choice = "reg6"
            list_countries(send_choice, 15, 128, 181)
        def choice_5():#Oceania
            send_choice = "reg6"
            list_countries(send_choice, 5, 182, 195)
        def choice_6():#World
            send_choice = "reg6"
            list_countries(send_choice, 20, 1, 195)

        def quizWin():
            global randomized_list, loop
            listSize = len(randomized_list)

            loop = 0

            def makeWin(i):

                def destroyQuiz():
                    global loop
                    quiz_frame.destroy()
                    loop = loop + 1
                    if loop != listSize:
                        makeWin(loop)
                    else:
                        scoreWin()

                def compare():
                    global score
                    filename = open("regions/reg6.txt", "r")
                    namelist = filename.readlines()
                    cname = []
                    cname = namelist[country-1]
                    cname = cname.split(';')
                    print(cname)
                    if ansEntry.get() in cname:
                        score=score+1
                        print("Valid")
                    else:
                        print("Invalid")


                global randomized_list
                print(randomized_list)

                v_Picture = PIL.Image.open("onePix.png", "r")
                onePix = PIL.ImageTk.PhotoImage(v_Picture)

                quiz_frame = Frame(width=win_width,
                                     height=0)
                quiz_frame.grid(column=0, row=0)

                country = randomized_list[i]
                print(country)
                imgName = "map/" + str(country) + ".jpg"
                print(imgName)
                imgT= PIL.Image.open(imgName, "r")
                resize=imgT.resize((800,400))
                img = PIL.ImageTk.PhotoImage(resize, master=quiz_frame)
                map = Label(master=quiz_frame, text="", image=img, width=800, height=400)
                map.grid(column=0, row=0)
                #map.image = img

                ansEntry = Entry(master=quiz_frame, text="",width = 80)
                ansEntry.grid(column=0, row=1)

                enter = Button(master=quiz_frame, text="Enter", width=30,
                                 command=lambda:[compare(), destroyQuiz()])
                enter.grid(column=0, row=2)

                #quiz_frame.pack()
                quiz_frame.mainloop()

            makeWin(loop)

        def scoreWin():
            global score
            print(score)

            def restartProg():
                os.execl(sys.executable, sys.executable, *sys.argv)

            scoreFrame = Frame(width=win_width, height=win_height)
            fillFrame = Frame(width=win_height, height=150)
            fillFrame.pack()

            text="You got " + str(score) + " out of " + str(len(randomized_list))
            scoreText = Label(text=text, font=('Ubuntu', 60))
            scoreText.pack()
            restart = Button(text="Restart", command=lambda:[restartProg()])
            restart.pack()

            scoreFrame.pack()

        mainwindow()

        window.mainloop()

    thewindow()


