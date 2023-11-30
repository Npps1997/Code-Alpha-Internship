import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def generate_short_url(self, original_url):
        # unique hash for the original URL
        hash_object = hashlib.md5(original_url.encode())
        hash_digest = hash_object.hexdigest()

        # Taking the first 8 characters as the short URL
        short_url = hash_digest[:8]

        # Storing the mapping in the dictionary
        self.url_mapping[short_url] = original_url

        return short_url

    def redirect(self, short_url):
        # Retrieving the original URL from the dictionary
        return self.url_mapping.get(short_url, None)


shortener = URLShortener()

original_url = input("Enter the URL to shorten: ")

short_url = shortener.generate_short_url(original_url)
print(f"Short URL: {short_url}")

redirected_url = shortener.redirect(short_url)
print(f"Redirected URL: {redirected_url}")
