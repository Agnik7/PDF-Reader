from extract_text.extract import ExtractText
from reader.speech import Speech
from delete_files.delete import Delete


if __name__ == "__main__":
    pdf_file_name = "sample.pdf"
    text_extract = ExtractText()
    extracted_text = text_extract.extract(pdf_file_name)
    print("============= Text successfully extracted!! ====================")
    voice = Speech()
    print("============= Generating the speech now... ====================")
    voice.speech(extracted_text)    
    delete = Delete()
    delete.delete_file("output.mp3")

    
