
#DSC 510
#Assignment 2.1
#date: 03/17/2020
#name: Harsimar Mangat
#Description: Program that asks for Company Name, Fiber Length and then prints out receipt detailing Cost, Company Name, & Fiber Optic Lenght







cost=.87
print("Welcome to Assignment #2")
name = input("What is your company name?\n")
fiber=float(input("How much fiber optic cable needs to be installed?\n"))
install=fiber*cost
print("Receipt for: {n}\nFiber Length {f}ft\nInstallation Cost ${i}".format(n=name,f=fiber,i=install))