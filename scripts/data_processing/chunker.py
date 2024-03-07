from chunkipy import TextChunker, TokenEstimator
from transformers import AutoTokenizer
import pandas as pd
from tqdm import tqdm
import os


class BertTokenEstimator(TokenEstimator):
    def __init__(self):
        self.bert_tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

    def estimate_tokens(self, text):
        return len(self.bert_tokenizer.encode(text))
    

#looping through the files and storing the data

data_pd = pd.DataFrame(columns = ['text', 'label', 'file_name', 'chunk_id'])

bert_token_estimator = BertTokenEstimator()

text_chunker = TextChunker(256, tokens=True, token_estimator=BertTokenEstimator(), overlap_percent=0.3)

folder_path = r"data/processed/Test/"

folderbar = tqdm(os.listdir(folder_path))

for foldername in folderbar:
    folderbar.set_description(foldername)
    filebar = tqdm(os.listdir(folder_path+foldername))
    for filename in filebar:
        filebar.set_description(desc=filename)
        file_path = folder_path+foldername + '/' + filename
        with open(file_path, 'r') as file:
            text = file.read()
        chunks = text_chunker.chunk(text)
        for i, chunk in enumerate(chunks):
            data_pd.loc[len(data_pd)] = [chunk, foldername, filename, hash(chunk)]

data_pd.to_csv(r'data/chunked_Test_final.csv', index=True, escapechar='\\')

