import fitz  # PyMuPDF
from gtts import gTTS
import os
from pydub import AudioSegment

def pdf_to_text(pdf_path):
    """Extract text from a PDF file."""
    text = ""
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        page_text = page.get_text()
        if page_text:
            text += page_text + "\n"  # Add a newline after each page's text for better separation

    return text

def text_to_speech(text, output_audio_path):
    """Convert text to speech and save it as an audio file."""
    # Handle cases where the text is too long for gTTS
    # gTTS has a limit on the length of text that can be processed
    # Split the text into smaller chunks if necessary
    max_length = 5000  # gTTS text length limit (approximate, adjust as needed)
    chunks = [text[i:i+max_length] for i in range(0, len(text), max_length)]
    
    # Create audio files for each chunk and concatenate them
    audio_files = []
    for idx, chunk in enumerate(chunks):
        chunk_audio_path = f"temp_chunk_{idx}.mp3"
        tts = gTTS(text=chunk, lang='en')
        tts.save(chunk_audio_path)
        audio_files.append(chunk_audio_path)
    
    # Concatenate audio files using a library like pydub
    from pydub import AudioSegment
    combined = AudioSegment.empty()
    for audio_file in audio_files:
        audio = AudioSegment.from_mp3(audio_file)
        combined += audio
    
    # Export the final combined audio
    combined.export(output_audio_path, format='mp3')
    
    # Clean up temporary audio files
    for audio_file in audio_files:
        os.remove(audio_file)

def main(pdf_path, output_audio_path):
    """Main function to convert PDF to speech."""
    # Extract text from the PDF
    text = pdf_to_text(pdf_path)
    
    # Convert text to speech and save it to an audio file
    text_to_speech(text, output_audio_path)
    print(f"Audio saved to {output_audio_path}")

if __name__ == "__main__":
    # Path to the PDF file in the same directory as the script
    pdf_path = 'WPR 6.pdf'
    
    # Path to the output audio file
    output_audio_path = 'output.mp3'
    
    # Run the main function
    main(pdf_path, output_audio_path)
