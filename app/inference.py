from transformers import AutoModelForSeq2SeqLM, AutoTokenizer  # Import necessary modules from the Transformers library.
import utils  # Import a custom module named 'utils'.

def infer(rules):
    # Create a tokenizer for sequence-to-sequence models and load it from the specified directory.
    tokenizer = AutoTokenizer.from_pretrained("./tst-summarization")
    
    # Create a sequence-to-sequence model and load it from the specified directory.
    model = AutoModelForSeq2SeqLM.from_pretrained("./tst-summarization")
    
    # Prepare the input for the model. Concatenate "order: " with the provided 'rules'.
    encoded_input = tokenizer("order: " + rules, return_tensors="pt").input_ids
    
    # Generate a summary using the model based on the encoded input.
    outputs = model.generate(encoded_input, max_length=200)
    
    # Decode the generated output, skipping special tokens.
    decode = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Convert the decoded output into a JSON expression using a custom 's_express_to_json' function from the 'utils' module.
    expression = utils.s_express_to_json(decode)
    
    return expression  # Return the generated JSON expression.