import pandas as pd
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
import os
import re
from tqdm import tqdm
import pandas as pd

folder_path = r"data/raw/Test/"
output_path = r"data/processed/Test/"
remove_text = 'Rationalised 2023-24'

folderbar = tqdm(os.listdir(folder_path))
process_log = pd.DataFrame(columns=["filename", "status", "error_message"])

for foldername in folderbar :
    # print("_"*100)
    output_folder = output_path + foldername + '/'
    folderbar.set_description(foldername)
    # print("Output path: " + output_folder)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    filebar = tqdm(os.listdir(folder_path+foldername))
    for filename in filebar:
        filebar.set_description(desc=filename)
        file_path = folder_path+foldername + '/' + filename
        text_file_name = output_folder + filename.replace("pdf","txt")
        # print("Output file: " + text_file_name)
        reader = extract_pages(file_path)
        final_text = ""
        try:
            for page_layout in reader:
                for element in page_layout:
                    if isinstance(element, LTTextContainer):
                        final_text += element.get_text()
            final_text = final_text.replace("\n\n", " ")
            final_text = final_text.replace(remove_text, "")
            output_file = open(text_file_name,"wb")
            output_file.write(final_text.encode('utf-8'))
            output_file.close()
            process_log.loc[len(process_log)] = [filename, "success", ""]
        except Exception as e:
            process_log.loc[len(process_log)] = [filename, "failed", str(e)]

# Output the not_processe
process_log.to_csv(r'logs/process_log_test.csv', index=False)
        