import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer

model = torch.load(r'C:\supports\phraser.pt')
tokenizer = T5Tokenizer.from_pretrained('t5-base')

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print ("device ",device)
model = model.to(device)

def twistIt(sentence,ret):
    text =  "paraphrase: " + sentence + " </s>"
    max_len = 256
    encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
    input_ids, attention_masks = encoding["input_ids"].to(device), encoding["attention_mask"].to(device)


    beam_outputs = model.generate(
        input_ids=input_ids, attention_mask=attention_masks,
        do_sample=True,
        max_length=256,
        top_k=120,
        top_p=0.70,
        early_stopping=True,
        num_return_sequences=ret # Number of sentences to return
    )
    phrases = ""
    for i,line in enumerate(beam_outputs):
    	paraphrase = tokenizer.decode(line,skip_special_tokens=True,clean_up_tokenization_spaces=True)
    	phrases += (f"{i+1}. {paraphrase}"+"\n\n")
    return phrases
