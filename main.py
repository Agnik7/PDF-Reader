from extract_text.extract import ExtractText
from reader.speech import Speech
from delete_files.delete import Delete
import textwrap

if __name__ == "__main__":
    pdf_file_name = "sample.pdf"
    text_extract = ExtractText()
    extracted_text = text_extract.extract(pdf_file_name)
    wrap_width = 80
    wrapped_text = textwrap.fill(extracted_text, wrap_width)
    print("============= Text successfully extracted!! ====================")
    voice = Speech()
    print("============= Generating the speech now... ====================")
    voice.speech(wrapped_text)    
    delete = Delete()
    delete.delete_file("output.mp3")

    
