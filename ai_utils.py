import google.generativeai as genai

def generate_article(transcript, api_key):
    """Uses Gemini API to rewrite the raw transcript into a structured article."""
    try:
        genai.configure(api_key=api_key)
        
        # FIXED: Updated to the newer, supported Gemini 2.5 Flash model
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        prompt = f"""
        You are an expert content writer. I am going to give you a raw transcript from a YouTube video.
        Your task is to transform this transcript into a highly engaging, insightful, and well-structured article.
        
        CRITICAL FORMATTING RULES:
        1. Start the article with a single catchy title using exactly one hash tag (e.g., # This is the Title).
        2. Use exactly two hash tags for major section headings (e.g., ## Introduction).
        3. Use exactly three hash tags for smaller subheadings (e.g., ### Key Details).
        4. Use standard bullet points (-) for lists.
        5. Do not put asterisks (**) around the headings, only use them to bold important words within regular paragraphs.
        6. Ensure the article is engaging, informative, and easy to read, with a good flow between sections.
        7. Do not include any content that is not directly derived from the transcript. Focus on clarity and value for the reader.
        8. Do not add any additional commentary or information that is not present in the transcript. Your job is to rewrite and structure the existing content, not to create new content.
        9. Ensure that the final output is in markdown format, adhering strictly to the formatting rules above.
        10. The article should be concise and to the point, avoiding unnecessary fluff while still being engaging.
        11. Do not include any disclaimers or notes about the AI generation process in the final article.
        12. The article should be suitable for publication on a blog or website, providing clear value to readers who are interested in the video's topic.
        13. The tone of the article should be professional yet approachable, making complex topics easy to understand for a general audience.
        14. Ensure that the article is free of grammatical errors and typos, and that it reads smoothly.
        15. if the transcripts contains any bash commands, code snippets, or technical instructions, please provide copy paste ready code blocks in the markdown output, using triple backticks (```) for formatting.

        Transcript:
        {transcript}
        """
        response = model.generate_content(prompt)
        return response.text, None
    except Exception as e:
        return None, str(e)