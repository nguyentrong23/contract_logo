from pdf2image import convert_from_path
import os
import shutil
import time
def convert_pdf_to_png(pdf_path, output_folder,folder_name):
    images = convert_from_path(pdf_path)
    match_folder = output_folder + "\\" + folder_name
    if os.path.exists(match_folder) and os.path.isdir(match_folder):
        shutil.rmtree(match_folder)
    os.makedirs(match_folder)
    for i,image in enumerate(images):
        image.save(f"{match_folder}/page_{i+1}.png", "PNG")

def object(path):
    if os.path.isdir(path):
        pdf_files = [f for f in os.listdir(path) if f.endswith('.pdf')]
        # print(pdf_files)
        for pdf_file in pdf_files:
            path4conv = path+"\\"+pdf_file
            pdf_file = os.path.splitext(pdf_file)[0]
            convert_pdf_to_png(path4conv,path,pdf_file)

# Đường dẫn đến file PDF và thư mục đầu ra

pdf_path = r"C:\Users\HPR\OneDrive\data\logo\NORTHRUP"

t1 = time.time()
object(pdf_path)
t2 = time.time()
# print(t2- t1)
# Gọi hàm chuyển đổi
# convert_pdf_to_png(pdf_path, output_folder)