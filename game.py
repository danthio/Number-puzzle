import tkinter as tk
import math
import random
from PIL import Image,ImageTk

def check():
	global game,state


	ar=[[1,2,3,4,5],
	   [6,7,8,9,10],
	   [11,12,13,14,15],
	   [16,17,18,19,20],
	   [21,22,23,24,0]]

	if game==ar:

		state="gameover"


images=[]

def create_rectangle(can,x1, y1, x2, y2, **kwargs):
	global images
	if 'alpha' in kwargs:
		alpha = int(kwargs.pop('alpha') * 255)
		fill = kwargs.pop('fill')
		fill = root.winfo_rgb(fill) + (alpha,)
		image = Image.new('RGBA', (x2-x1, y2-y1), fill)
		images.append(ImageTk.PhotoImage(image))
		can.create_image(x1, y1, image=images[-1], anchor='nw')
	





def main():
	global can,state,game,quit

	can.delete("all")






	can.create_rectangle(70-1,70-1,500-70,500-70,fill="darkgreen",outline="darkgreen")




	def draw_box(x,y,s,n):

		can.create_rectangle(x,y, x+s,y+s,fill="#57f76d",outline="darkgreen")

		can.create_text(x+s/2,y+s/2,text=str(n),font=("FreeMono",25))





	y=70
	for y_ in range(5):
		x=70
		for x_ in range(5):

			if not game[y_][x_]==0:

				draw_box(x,y,70.8,game[y_][x_])



			x+=72

		y+=72



	if state=="gameover":
	
		create_rectangle(can,0, 0, 500, 500, fill='#000000', alpha=.5)

		can.create_text(250,250,text="Win!!",font=("FreeMono",40),fill="#ffffff")



	quit=ImageTk.PhotoImage(file="data/quit.png")

	can.create_image(500-10-30,10,image=quit,anchor="nw")


def initialize():

	global game


	game=[[0,0,0,0,0],
		  [0,0,0,0,0],
		  [0,0,0,0,0],
		  [0,0,0,0,0],
		  [0,0,0,0,0]]

	ar=[]

	xx=random.randint(0,4)
	yy=random.randint(0,4)

	def random_no(a):

		while 1:
			
			n=random.randint(1,24)

			try:

				v=a.index(n)
			except:
				return n



		


	for y_ in range(5):

		for x_ in range(5):

			if y_==yy and x_==xx:
				game[y_][x_]=0
				continue


			n=random_no(ar)
			ar.append(n)




			game[y_][x_]=n





	return game





def intro():

	global can,state

	state="intro"


	can.delete("all")


	can.create_oval(250-30-15,250-15, 250-30-15+30,250+15,fill="#57f76d",outline="#57f76d")
	can.create_rectangle(250-30,250-15, 250+30,250+15,fill="#57f76d",outline="#57f76d")
	can.create_oval(250+30-15,250-15, 250+30-15+30,250+15,fill="#57f76d",outline="#57f76d")
	can.create_text(250,250,text="PLAY",font=("FreeMono",14),fill="#000000")




def commands(e):


	global state,can,game

	if state=="gameover":

		cx,cy=500-10-15,10+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			state="intro"
			intro()

	elif state=="game":

		for y in range(5):

			for x in range(5):

				if game[y][x]==0:
					void=[y,x]

		if 70<=e.x<=500-70:
			if 70<=e.y<=500-70:


				x=int((e.x-70)/72)
				y=int((e.y-70)/72)

				

				if [y,x]==void:
					return


				if [y+1,x]==void or [y-1,x]==void or [y,x+1]==void or [y,x-1]==void:


					n=game[y][x]

					game[y][x]=0

					game[void[0]][void[1]]=n

					check()
					main()
					
				return

		cx,cy=500-10-15,10+15

		r=math.sqrt((cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			state="intro"
			intro()

	elif state=="intro":

		if 250-30<=e.x<=250+30 and 250-15<=e.y<=250+15:

			state="game"
			initialize()
			main()
			return


		cx,cy=250-30,250

		r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			state="game"
			initialize()
			main()
			return


		cx,cy=250+30,250

		r=math.sqrt( (cx-e.x)**2+(cy-e.y)**2)

		if r<=15:
			state="game"
			initialize()
			main()
			return




state=""
game=[]
quit=0

root=tk.Tk()
root.geometry("500x500+50+50")
root.title("Number Puzzle")

can=tk.Canvas(bg="#000000",relief="flat",highlightthickness=0,border=0,width=500,height=500)
can.place(in_=root,x=0,y=0)
can.bind("<Button-1>",commands)


intro()

root.mainloop()