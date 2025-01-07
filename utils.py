import re


def convert_to_url_format(text):
    # Replace spaces with hyphens and convert to lowercase
    text = re.sub(r'\s+', '-', text)
    # Remove non-alphanumeric characters except hyphens
    text = re.sub(r'[^a-zA-Z0-9-/]', '', text)
    # Convert to lowercase
    return text.lower()