cat << 'EOF' > README.md
# 🎥 Vid2Article AI

**Transform any YouTube video into a beautifully formatted, insightful, and downloadable PDF article in seconds.**

Powered by **Python**, **Streamlit**, and **Google's Gemini AI**, this tool bridges the gap between video content and written knowledge.

---

## ✨ Features

* **Instant Extraction:** Automatically pulls closed-caption transcripts from YouTube videos using the \`youtube-transcript-api\`.
* **AI-Powered Writing:** Leverages **Google Gemini 1.5 Pro/Flash** to synthesize raw, messy transcripts into structured, engaging articles with clear headings and bullet points.
* **Bulletproof PDF Generation:** Uses a customized \`fpdf2\` implementation featuring automatic text-wrapping and Unicode sanitization to prevent crashes from special characters.
* **Custom Typography:** Supports \`DejaVuSans.ttf\` for modern PDF layouts (with an automatic fallback to standard Helvetica).
* **Modern UI:** A sleek Streamlit interface with gradient buttons, dynamic status indicators, and clean expanders for text previews.

---

## 🛠️ Project Structure

The project is built with a modular architecture for easy maintenance:

| File | Description |
| :--- | :--- |
| \`app.py\` | The main Streamlit entry point and UI logic. |
| \`ai_utils.py\` | Manages the connection, system instructions, and prompting for Gemini AI. |
| \`youtube_utils.py\` | Handles URL parsing, video ID extraction, and transcript retrieval. |
| \`pdf_utils.py\` | Contains the \`ArticlePDF\` class for markdown-to-PDF conversion. |
| \`requirements.txt\` | List of all Python dependencies. |

---

## 🚀 Getting Started

### 1. Prerequisites
* **Python 3.8+**
* A **Google Gemini API Key**. You can get one for free at [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Installation
Clone the repository and install the dependencies:

\`\`\`bash
git clone https://github.com/Siva-pa/youtube-to-article-ai.git
cd youtube-to-article-ai
pip install -r requirements.txt
\`\`\`

### 3. Run the App
\`\`\`bash
streamlit run app.py
\`\`\`

---

## 📖 How It Works

1.  **Input:** Paste a YouTube URL into the dashboard.
2.  **Fetch:** The system extracts the transcript (supporting multiple languages).
3.  **Process:** The AI analyzes the transcript, removes "filler" words, and organizes the core message into a professional article format.
4.  **Export:** Download the result as a clean, formatted PDF.

---

## 🤝 Contributing

Contributions make the open-source community an amazing place to learn and create. 
1. **Fork** the Project
2. **Create** your Feature Branch (\`git checkout -b feature/AmazingFeature\`)
3. **Commit** your Changes (\`git commit -m 'Add some AmazingFeature'\`)
4. **Push** to the Branch (\`git push origin feature/AmazingFeature\`)
5. **Open** a Pull Request

---

### 📄 License
Distributed under the MIT License. See \`LICENSE\` for more information.

> **Note:** This project is for educational purposes. Ensure you comply with YouTube's Terms of Service regarding transcript usage.

EOF

echo "README.md has been successfully enhanced!"
