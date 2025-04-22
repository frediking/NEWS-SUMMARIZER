This Python-based NLP News Summarizer using Tkinter for the GUI and NLTK, Newspaper3k, and TextBlob for natural language processing. It allows users to enter a news article URL, fetches the content, and provides the following:

 • Title of the article
 
 • Author(s)
 
 • Publication Date
 
 • Summary of the article
 
 • Sentiment Analysis of the article


# News Summarizer  

## 📌 Project Description  
The **News Summarizer** is a Python-based GUI application that fetches and summarizes news articles from a given URL. It utilizesextBlob for natural to extract the article's title, author(s), publication date, a concise summary, and sentiment analysis.  

### 🔥 Features  
- Extracts Title – Displays the article's title.  
-News Summarizer using Tkin– Lists the authors of the article.  
- Summarizer using Tkinter for th– Shows when the article was published.  
-marizer using Tkinter for– Provides a concise summary using NLP techniques.  
-ng Tkinter for the GUI and NLTK, – Analyzes the tone of the article (positive, negative, or neutral).  
- GUI and NLTK, Newspape– Built with Tkinter for easy interaction.  

## 🛠️ Technologies Used  
-UI and NLTK, 
- Tkinter (GUI framework)  
-ython-base(Natural Language Processing)  
-P News Summarizer(Article scraping and NLP)  
- NLP News Summ(Sentiment analysis)  

## 🚀 Installation and Setup  
### 1️⃣ Install Dependencies  
Ensure you havend TextBlob for installed. Then, install the required libraries:  
```bash
pip install tkinter nltk newspaper3k textblob

For first-time users, download the required NLTK resources:

import nltk
nltk.download('punkt_tab')
```
## 2️⃣ Clone the Repository

git clone https://github.com/frediking/NEWS-SUMMARIZER.git

## 3️⃣ Run the Application

python tk.py

## 📸 Screenshots

![news-summarizerSS](https://github.com/user-attachments/assets/4479bc79-5ce3-40f3-bc38-4f5364995e2c)


## 📜 How It Works
 1. Enter a **news article** URL in the input field.
 2. Click the **Summarize** button.
 3. The application will fetch and process the article.
 4. Outputs include:
 • **Title**
 • **Author(s)**
 • **Publication Date**
 • **Summary**
 • **Sentiment Analysis Result**

## ⚡ Example Usage

Sample URLs:

1. https://www.bbc.com/news/world-europe-60506682  
2. https://www.aljazeera.com/news/2025/2/18/philippine-vp-dutertes-backers-ask-supreme-court-to-throw-out-impeachment

The application extracts and displays the relevant information.

## 🤖 Future Improvements
 • Allow users to paste text manually instead of only URLs.
 • Provide multilingual support for summarization.
 • Implement an export feature to save summaries as text files.

## 🤝 Contributing

Feel free to fork this repository, create a new branch, and submit a pull request with improvements!

## 📝 License

This project is licensed under the MIT License.
