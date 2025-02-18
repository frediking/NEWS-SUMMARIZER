import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article
# nltk.download('punkt_tab')
# url = 'https://www.bbc.com/news/world-europe-60506682'

def summarize():
    url = utext.get("1.0", "end").strip()

    # Create an instance of Article instead of overwriting the class name
    article = Article(url) 

    article.download()
    article.parse()
    article.nlp()

    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', tk.END)
    title.insert('1.0', article.title)

    author.delete('1.0', tk.END)
    author.insert('1.0', article.authors)

    publication.delete('1.0', tk.END)
    # Convert publish_date to string, or use an empty string if None
    pub_date = str(article.publish_date) if article.publish_date is not None else ""
    publication.insert('1.0', pub_date)

    summary.delete('1.0', tk.END)
    summary.insert('1.0', article.summary)

    # Use actual article.text instead of a string literal.
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', tk.END)
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

    print(f'Title: {article.title}')
    print(f'Authors: {article.authors}')
    print(f'Publication Date: {article.publish_date}')
    print(f'Summary: {article.summary}')

    

root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')


tlabel = tk.Label(root, text='News Summarizer', font=('Helvetica', 24))
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text='Author', font=('Helvetica', 12))
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text='Publishing Date', font=('Helvetica', 12))
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text='Summary', font=('Helvetica', 12))
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis', font=('Helvetica', 12))
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text='URL', font=('Helvetica', 12))
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text='Summarize', command=summarize)
btn.pack()

root.mainloop()