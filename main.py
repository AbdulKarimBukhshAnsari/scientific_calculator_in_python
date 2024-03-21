from tkinter import *
from PIL import ImageTk,Image
import math as m
def close():
    root.destroy()
def clr():
    ent.delete(0,"end")
def back():
    last=len(ent.get())
    ent.delete(last-1)
def press(input):
    length=len(ent.get())
    ent.insert(length,input)
def add(a,b):
    return float(a)+float(b)
def sub(a,b):
    return float(a)-float(b)
def mult(a,b):
    return float(a)*float(b)
def div(a,b):
    return float(a)/float(b)
def expression_break(sign,expression):
    values=expression.split(sign,1)
    return values

def scientific(expression):

    sci=expression_break("(",expression)
    if sci[0]=="tan":
        result=m.tan(m.radians(float(sci[1])))
    elif sci[0]=="sin":
        result=m.sin(m.radians(float(sci[1])))
    elif sci[0]=="cos":
        result=m.cos(m.radians(float(sci[1])))
    elif sci[0]=="ln":
        result=m.log(float(sci[1]))
    elif sci[0]=="log":
        result=m.log10(float(sci[1]))
    elif sci[0]=="√":
        result=m.sqrt(float(sci[1]))
    elif sci[0]=="deg":
        result=m.degrees(float(sci[1]))
    elif sci[0]=="rad":
        result=m.radians(float(sci[1]))
    elif sci[0]=="fac":
        result=m.factorial(int(sci[1]))
    return result
def equal():
    expression=ent.get()
    clr()
    try:
        if expression.find("(")>0:
            result=scientific(expression)
        elif expression.find("power") >0:
            sci=expression_break("power",expression)
            result =m.pow(float(sci[0]),float(sci[1]))
        elif expression.find("mod") >0:
            sci=expression_break("mod",expression)
            result =m.remainder(float(sci[0]),float(sci[1]))
        elif expression.find("x") >0:
            sci=expression_break("x",expression)
            result =mult(float(sci[0]),float(sci[1]))
        elif expression.find("/") >0:
            sci=expression_break("/",expression)
            result =div(float(sci[0]),float(sci[1]))
        elif expression.find("+") >0:
            first=expression.find("+")
            second=expression.find("+",(first+1),(first+5))
            if  first>second:
                sci=expression_break("+",expression)
                result=add(sci[0],sci[1])
            else:
                result=add(expression[0:second],expression[second+1:])
        elif expression.rindex("-")>0:
            sign=expression.rindex("-")
            result=sub(expression[0:sign],expression[sign+1:])
        ent.insert(0,result)
    except Exception as e:
        ent.insert(0,e)




root =Tk()
root.title("Scientific Calculator")

root.geometry("383x605+470+20")
root.resizable(False,False)
root["bg"]="gray11"
ent_variable=StringVar()
ent=Entry(root,textvariable=ent_variable,bg="gray20",fg="White",border=0,font=("Bahnschrift SemiBold",26,"bold"))
ent.grid(columnspan=4,ipady=15)
font=("Calibari",18,"bold")
b_tan=Button(root,text="tan",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("tan("))
b_tan.grid(row=1,column=0,sticky=E+W,ipady=5)
b_sin=Button(root,text="sin",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("sin("))
b_sin.grid(row=1,column=1,sticky=E+W,ipady=5)
b_cos=Button(root,text="cos",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("cos("))
b_cos.grid(row=1,column=2,sticky=E+W,ipady=5)
b_sqrt=Button(root,text="√",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("√("))
b_sqrt.grid(row=1,column=3,sticky=E+W,ipady=5)
b_log=Button(root,text="log",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("log("))
b_log.grid(row=2,column=0,sticky=E+W,ipady=5)
b_ln=Button(root,text="ln()",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("ln("))
b_ln.grid(row=2,column=1,sticky=E+W,ipady=5)
b_deg=Button(root,text="deg",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("deg("))
b_deg.grid(row=2,column=2,sticky=E+W,ipady=5)
b_rad=Button(root,text="rad",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("rad("))
b_rad.grid(row=2,column=3,sticky=E+W,ipady=5)
b_fac=Button(root,text="fac",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("fac("))
b_fac.grid(row=3,column=0,sticky=E+W,ipady=5)
b_pow=Button(root,text="pow",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("power"))
b_pow.grid(row=3,column=1,sticky=E+W,ipady=5)
b_rem=Button(root,text="mod",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press("mod"))
b_rem.grid(row=3,column=2,sticky=E+W,ipady=5)
b_pie=Button(root,text="π",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid",command=lambda:press(3.141592))
b_pie.grid(row=3,column=3,sticky=E+W,ipady=5)
b_left=Button(root,text="(",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid")
b_left.grid(row=4,column=0,sticky=E+W,ipady=5)
b_right=Button(root,text=")",bg="darkorange",fg="gray11",font=font,borderwidth=1,relief="solid")
b_right.grid(row=4,column=1,sticky=E+W,ipady=5)
b_del=Button(root,text="del",bg="gray5",fg="darkorange",font=font,borderwidth=1,relief="solid",command=back)
b_del.grid(row=4,column=2,sticky=E+W,ipady=5)
b_clr=Button(root,text="AC",bg="gray5",fg="darkorange",font=font,borderwidth=1,relief="solid",command=clr)
b_clr.grid(row=4,column=3,sticky=E+W,ipady=5)
b_plus=Button(root,text="+",bg="gray9",fg="darkorange3",font=font,borderwidth=1,relief="solid",command=lambda:press("+"))
b_plus.grid(row=5,column=3,sticky=E+W,ipady=5)
b_7=Button(root,text="7",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(7))
b_7.grid(row=5,column=0,sticky=E+W,ipady=5)
b_8=Button(root,text="8",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(8))
b_8.grid(row=5,column=1,sticky=E+W,ipady=5)
b_9=Button(root,text="9",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(9))
b_9.grid(row=5,column=2,sticky=E+W,ipady=5)
b_minus=Button(root,text="--",bg="gray9",fg="darkorange3",font=font,borderwidth=1,relief="solid",command=lambda:press("-"))
b_minus.grid(row=6,column=3,sticky=E+W,ipady=5)
b_4=Button(root,text="4",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(4))
b_4.grid(row=6,column=0,sticky=E+W,ipady=5)
b_5=Button(root,text="5",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(5))
b_5.grid(row=6,column=1,sticky=E+W,ipady=5)
b_6=Button(root,text="6",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(6))
b_6.grid(row=6,column=2,sticky=E+W,ipady=5)
b_1=Button(root,text="1",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(1))
b_1.grid(row=7,column=0,sticky=E+W,ipady=5)
b_2=Button(root,text="2",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(2))
b_2.grid(row=7,column=1,sticky=E+W,ipady=5)
b_3=Button(root,text="3",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(3))
b_3.grid(row=7,column=2,sticky=E+W,ipady=5)
b_mult=Button(root,text="x",bg="gray9",fg="darkorange3",font=font,borderwidth=1,relief="solid",command=lambda:press("x"))
b_mult.grid(row=7,column=3,sticky=E+W,ipady=5)
b_div=Button(root,text="/",bg="gray9",fg="darkorange3",font=font,borderwidth=1,relief="solid",command=lambda:press("/"))
b_div.grid(row=8,column=3,sticky=E+W,ipady=5)
b_point=Button(root,text=".",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press("."))
b_point.grid(row=8,column=0,sticky=E+W,ipady=5)
b_0=Button(root,text="0",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(0))
b_0.grid(row=8,column=1,sticky=E+W,ipady=5)
b_e=Button(root,text="e",bg="gray11",fg="darkorange",font=font,borderwidth=1,relief="solid",command=lambda:press(2.71828))
b_e.grid(row=8,column=2,sticky=E+W,ipady=5)
b_equal=Button(root,text="=",bg="darkorange3",fg="gray5",font=font,borderwidth=1,relief="solid",command=equal)
b_equal.grid(row=9,column=0,columnspan=3,sticky=E+W,ipady=5)
b_close=Button(root,text="close",bg="gray5",fg="darkorange",font=font,borderwidth=1,relief="solid",command=close)
b_close.grid(row=9,column=3,sticky=E+W,ipady=5)

