from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import utils

def infer(rules):
    tokenizer = AutoTokenizer.from_pretrained("./tst-summarization")
    model = AutoModelForSeq2SeqLM.from_pretrained("./tst-summarization")
    #the rules variable is from the Processapp
    encoded_input = tokenizer("order: " + rules, return_tensors="pt").input_ids
    # encoded_input = tokenizer(text, return_tensors='pt')
    outputs = model.generate(encoded_input, max_length=200)
    decode = tokenizer.decode(outputs[0], skip_special_tokens=True)
    expression = utils.s_express_to_json(decode)
    return expression