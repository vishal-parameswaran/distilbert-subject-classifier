import pandas as pd

question_answer_dataset = pd.read_csv(r'data/processed/subjects-questions.csv')

chunked_dataset = pd.read_csv(r'data/processed/chunked_final.csv')

chunked_dataset.rename(columns={'Unnamed: 0':'index'}, inplace=True)
chunked_dataset.drop(columns=['index'], inplace=True)
chunked_dataset.set_index('chunk_id', inplace=True)
chunked_dataset.reset_index(inplace=True)

question_answer_dataset.rename(columns={'eng':'text','Subject':'label'}, inplace=True)
question_answer_dataset['file_name'] = 'subjects-questions.csv'
question_answer_dataset['chunk_id'] = question_answer_dataset['text'].apply(lambda x: hash(x))
question_answer_dataset.set_index('chunk_id', inplace=True)
question_answer_dataset.reset_index(inplace=True)
question_answer_dataset['label'] = question_answer_dataset['label'].apply(lambda x: x.lower())

merged_dataset = pd.concat([chunked_dataset,question_answer_dataset, ], axis=0)
merged_dataset.to_csv(r'data/final/final_dataset.csv', index=False, encoding='utf-8',escapechar='\\')