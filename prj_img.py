try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys
import os

pytesseract.pytesseract.tesseract_cmd=r'Tesseract-OCR\tesseract'   #input directory


if __name__ == "__main__":

    if(len(sys.argv) != 2):
        print("Pass filename to process")
    else:
        file_to_process = sys.argv[1]
        print("*************************************")
        print("Printing file contents of " + file_to_process)
        print("*************************************")
        
        scanned_text = pytesseract.image_to_string(Image.open(file_to_process))
            

        out_directory ='swetha_works' #in mama sent code it was output
        out_file = input("Enter output file name...")
        output_file_path_and_name = os.path.join(out_directory, out_file+".txt")

        out_file = open(output_file_path_and_name, "w+")
        out_file.write(scanned_text)
        out_file.seek(0,0)
        print(out_file.read())
        out_file.close()
            















        
