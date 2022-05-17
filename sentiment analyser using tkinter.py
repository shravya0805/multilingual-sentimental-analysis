from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from tkinter import *



def sentiment():

	sentence = textarea.get("1.0", "end")
	sen = SentimentIntensityAnalyzer()
	sent_dict = sen.polarity_scores(sentence)
	string = str(sent_dict['neg']*100) + "% Negative"
	negativeField.insert(10, string)
	string = str(sent_dict['neu']*100) + "% Neutral"
	neutralField.insert(10, string)
	string = str(sent_dict['pos']*100) +"% Positive"
	positiveField.insert(10, string)
	if sent_dict['compound'] >= 0.05 :
		string = "Positive"
	elif sent_dict['compound'] <= - 0.05 :
		string = "Negative"
	else :
		string = "Neutral"
	overallField.insert(10, string)
		
def clear() :

	negativeField.delete(0, END)
	neutralField.delete(0, END)
	positiveField.delete(0, END)
	overallField.delete(0, END)

	textarea.delete(1.0, END)

if __name__ == "__main__" :
	
	gui = Tk()
	gui['background']='DarkSeaGreen3'
	gui.title("Sentiment Detector")
	gui.geometry("250x400")
	enterText = Label(gui, text = "Enter Your Sentence",bg = 'DarkSeaGreen3')
	textarea = Text(gui, height = 5, width = 25, font = "lucida 13")
	check = Button(gui, text = "Check Sentiment", fg = "Black",bg = 'SlateGray3', command = sentiment)
	negative = Label(gui, text = "negativity in sentence: ",bg = 'DarkSeaGreen3')
	neutral = Label(gui, text = "Neutrality in sentence: ",bg = 'DarkSeaGreen3')
	positive = Label(gui, text = "positivity in senetnce: ",bg = 'DarkSeaGreen3')
	overall = Label(gui, text = "Sentence Overall Rated As: ",bg = 'DarkSeaGreen3')
	negativeField = Entry(gui)
	neutralField = Entry(gui)
	positiveField = Entry(gui)
	overallField = Entry(gui)
	clear = Button(gui, text = "Clear", fg = "Black",bg = 'SlateGray3', command = clear)
	Exit = Button(gui, text = "Exit", fg = "Black",bg = 'SlateGray3', command = exit)
	enterText.grid(row = 0, column = 2)
	textarea.grid(row = 1, column = 2, padx = 10, sticky = W)
	check.grid(row = 2, column = 2)
	negative.grid(row = 3, column = 2)
	negativeField.grid(row = 4, column = 2)	
	neutral.grid(row = 5, column = 2)
	neutralField.grid(row = 6, column = 2)	
	positive.grid(row = 7, column = 2)
	positiveField.grid(row = 8, column = 2)	
	overall.grid(row = 9, column = 2)
	overallField.grid(row = 10, column = 2)	
	clear.grid(row = 11, column = 2)
	Exit.grid(row = 12, column = 2)
	gui.mainloop()
	

