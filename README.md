# 🌐 Web Page Analyzer & Text Extractor

A Streamlit-based web app that fetches and analyzes any webpage.  
It extracts the page title, meta description, visible text content, and all hyperlinks.  
The app also detects the language of the text, performs word frequency analysis, and runs sentiment analysis on the extracted text.


## 🚀 Features

- Fetches and decodes HTML content from any public URL
- Extracts:
  - Page Title
  - Meta Description
  - All Hyperlinks
  - Visible Text Content
- Performs:
  - Language Detection (using `langdetect`)
  - Word Frequency Analysis (top 10 words)
  - Sentiment Analysis (polarity and subjectivity with `TextBlob`)
- Interactive user interface built with Streamlit


## 📦 Installation

1. Clone the repo:
   git clone https://github.com/md-sakibislam/web_analyzer.git
   cd web_analyzer

2. Install dependencies:
   pip install -r requirements.txt
   python -m textblob.download_corpora

## 🎯 Usage

Run the Streamlit app:

streamlit run web_analyzer.py

Enter a URL in the input box and click **Analyze**.
The app will display the extracted information and analysis results.

## 🛠 Tech Stack

* Python 3
* [Streamlit](https://streamlit.io/)
* [Requests](https://docs.python-requests.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
* [TextBlob](https://textblob.readthedocs.io/)
* [langdetect](https://pypi.org/project/langdetect/)


## 📁 Project Structure

web-page-analyzer/
├── web_analyzer.py        # Main Streamlit application script
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation


## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.


## 📄 License

Copyright (c) 2025 MD. Sakib Islam

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


## 📞 Contact

Your Name — MD. Sakib Islam | md-sakibislam@users.noreply.github.com

Project Link: https://github.com/md-sakibislam/web_analyzer


