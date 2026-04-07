# 🎥 Vid2Article AI

Transform any YouTube video into a beautifully formatted, insightful, and downloadable PDF article in seconds. Powered by Python, Streamlit, and Google's Gemini AI.

## ✨ Features

* **Instant Extraction:** Automatically pulls closed-caption transcripts from YouTube videos using the `youtube-transcript-api`.
* **AI-Powered Writing:** Leverages Google's Gemini AI to synthesize raw, messy transcripts into structured, engaging articles with clear headings and bullet points.
* **Bulletproof PDF Generation:** Uses a heavily customized implementation of `fpdf2` that features automatic text-wrapping, Unicode sanitization, and a robust safety net to prevent PDF rendering crashes from weird AI text outputs.
* **Custom Typography:** Supports `DejaVuSans.ttf` for beautiful, modern PDF layouts (with an automatic fallback to standard Helvetica if the font file is missing).
* **Modern UI:** Built with Streamlit, featuring custom CSS gradient buttons, dynamic status dropdowns, and clean expanders for text previewing.

## 🛠️ Project Structure

This project is modularly designed for easy maintenance and scaling:

* `app.py`: The main Streamlit web application and user interface.
* `ai_utils.py`: Handles the connection and prompting for the Google Gemini API.
* `youtube_utils.py`: Manages video ID extraction and transcript fetching.
* `pdf_utils.py`: Contains the custom `ArticlePDF` class, markdown stripping, Unicode sanitization, and crash-proof PDF generation logic.
* `requirements.txt`: Lists all necessary Python dependencies.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your machine. You will also need a free **Google Gemini API Key**, which you can get from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Installation
Clone this repository to your local machine and install the required dependencies:

```bash
git clone [https://github.com/YOUR_USERNAME/youtube-to-article-ai.git](https://github.com/YOUR_USERNAME/youtube-to-article-ai.git)
cd youtube-to-article-ai
pip install -r requirements.txt
