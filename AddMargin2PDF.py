import os
import PyPDF2

def add_margins_to_pdf(input_path, output_path, left, right, top, bottom):
    with open(input_path, 'rb') as infile:
        reader = PyPDF2.PdfReader(infile)
        writer = PyPDF2.PdfWriter()
        
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page.mediabox.upper_right = (
                page.mediabox.right + right,
                page.mediabox.top + top
            )
            page.mediabox.lower_left = (
                page.mediabox.left - left,
                page.mediabox.bottom - bottom
            )
            writer.add_page(page)
        
        with open(output_path, 'wb') as outfile:
            writer.write(outfile)

if __name__ == "__main__":
    
    #specify margins here
    left_margin = 0*72 
    right_margin = 3*72
    top_margin = 0*72
    bottom_margin = 3*72
    
    #specify your own paths here
    input_directory = r"C:\Users\gaur\Desktop\pdfmargin\original"
    output_directory = r"C:\Users\gaur\Desktop\pdfmargin\modified"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Process all PDF files in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.pdf'):
            input_pdf_path = os.path.join(input_directory, filename)
            output_pdf_path = os.path.join(output_directory, filename)
            add_margins_to_pdf(input_pdf_path, output_pdf_path, left_margin, right_margin, top_margin, bottom_margin)
            print(f"Modified {filename} and saved to {output_directory}!")

    print("All PDFs modified and saved successfully!")
