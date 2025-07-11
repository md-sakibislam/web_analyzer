import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from textblob import TextBlob
from langdetect import detect
import streamlit as st


def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except Exception as e:
        return f"Error fetching {url}: {e}"


def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.title.string.strip() if soup.title else 'No title found'

    meta_desc = 'No description found'
    if soup.find("meta", attrs={"name": "description"}):
        meta_desc = soup.find("meta", attrs={"name": "description"}).get("content", "").strip()

    text = soup.get_text(separator=' ', strip=True)

    links = [a.get('href') for a in soup.find_all('a', href=True)]

    return title, meta_desc, text, links


def analyze_text(text):
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = len(words)
    top_words = Counter(words).most_common(10)
    return word_count, top_words


def detect_language(text):
    try:
        return detect(text)
    except Exception:
        return "Could not detect language"


def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity, blob.sentiment.subjectivity


def main():
    st.set_page_config(page_title="Web Page Analyzer", layout="centered")
    st.title("🌐 Web Page Analyzer & Text Extractor")

    url = st.text_input("Enter a URL to analyze:")

    if st.button("Analyze") and url:
        html = fetch_webpage(url)

        if html.startswith("Error"):
            st.error(html)
            return

        title, meta_desc, text, links = parse_html(html)
        word_count, top_words = analyze_text(text)
        language = detect_language(text)
        polarity, subjectivity = analyze_sentiment(text)

        st.subheader("📋 Page Information")
        st.write(f"**Title:** {title}")
        st.write(f"**Meta Description:** {meta_desc}")
        st.write(f"**Language:** {language}")
        st.write(f"**Sentiment Polarity:** {polarity:.2f}")
        st.write(f"**Sentiment Subjectivity:** {subjectivity:.2f}")
        st.write(f"**Total Word Count:** {word_count}")

        st.subheader("📊 Top 10 Words")
        for word, freq in top_words:
            st.write(f"- {word}: {freq}")

        st.subheader("🔗 Links Found")
        st.write(f"Total Links: {len(links)}")
        for link in links:
            st.write(link)


if __name__ == '__main__':
    main()
