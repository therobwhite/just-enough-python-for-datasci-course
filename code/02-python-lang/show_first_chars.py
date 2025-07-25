import httpx

url = input("What URL will we download? ")

if not url.startswith('http'):
    url = 'https://' + url

resp = httpx.get(url, follow_redirects=True)
resp.raise_for_status()

text = resp.text
count = 250
print(f"The first {count} letters from {url} are:")
print()
print(text[0:count])
