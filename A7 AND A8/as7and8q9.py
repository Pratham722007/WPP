import re

def tokenize(text):
    tokens = []
    patterns = [
        r"\d{1,2}/\d{1,2}/\d{2,4}",  # Dates
        r"https?://\S+|www\.\S+",    # URLs
        r"\b\w+@\w+\.\w+\b",         # Emails
        r"[\w\.-]+",                 # Words, numbers, social media handles
        r"\.\d+|\d+\.?\d*",          # Numbers
        r"[,!?;]"                    # Punctuation
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text)
        for match in matches:
            tokens.append(match)
            text = text.replace(match, '')
    return tokens

text = "Email: test@example.com, URL: https://example.com, Date: 23/05/2020"
print(tokenize(text))
