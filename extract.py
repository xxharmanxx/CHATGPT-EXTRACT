import re

def extract_session_tokens(input_text):
    # Define the pattern for extracting the session token
    pattern = re.compile(r'__Secure-next-auth\.session-token=([^;]+)')

    # Find all matches in the input text
    matches = pattern.findall(input_text)

    return matches

def main():
    # Read input from the file
    with open('C:/Users/harma/OneDrive/Desktop/Pay_request[1].txt', 'r') as file:
        input_text = file.read()


    # Extract session tokens
    session_tokens = extract_session_tokens(input_text)

    # Print session tokens
    print("Session Tokens:")
    for token in session_tokens:
        print(token)

    # Store session tokens in another file
    with open('output.txt', 'w') as output_file:
        for token in session_tokens:
            output_file.write(token + '\n')

if __name__ == "__main__":
    main()
