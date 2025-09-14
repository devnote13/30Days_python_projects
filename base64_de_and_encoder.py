import base64

ask = input('What you want to do encode or decode:')
if ask == 'decode':
#user input
    base64_string = input('Enter a Base64 sting to decode:')
#this tells it to use ascii 
    base64_bytes = base64_string.encode("utf-8")
# this takes the base64_string then decode it
    sample_string_bytes = base64.b64decode(base64_bytes)
#this tells it to use ascii to decode
    decode = sample_string_bytes.decode("utf-8")
#this is the main answer
    print(f"Decoded string: {decode}")
if ask == 'encode':
    sample_string = input("Enter a word or anything to encode:")
    sample_string_bytes = sample_string.encode("utf-8")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("utf-8")
    print(f"Encoded string: {base64_string}")