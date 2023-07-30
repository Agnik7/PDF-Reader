import PyPDF2

class ExtractText:
    def extract(self,PATH):
        """
        Extracts the text from the PDF file provided

        Args: 
            PATH (string): Path of the pdf file
        
        Returns:
            text (string): The text extracted from the PDF. 
        """
        
        try:
            with open(PATH, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                if len(pdf_reader.pages) <= 0:
                    return "No pages found in the PDF."

                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()

                return text
        except FileNotFoundError:
            return "File not found."
        except PyPDF2.utils.PdfReadError:
            return "Error reading the PDF file."
