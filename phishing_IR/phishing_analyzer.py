import re

# Read email file
with open("sample_phishing_email.txt", "r") as file:
    email_content = file.read()

# Extract URLs
urls = re.findall(r'(https?://\S+)', email_content)

# Extract email addresses
emails = re.findall(r'[\w\.-]+@[\w\.-]+', email_content)

# Simple phishing keywords
phishing_keywords = ["urgent", "password", "verify", "suspend", "compromised"]

# Check for keywords
keyword_matches = []
for word in phishing_keywords:
    if word.lower() in email_content.lower():
        keyword_matches.append(word)

# Output results
print("=== PHISHING EMAIL ANALYSIS RESULT ===\n")

print("Extracted Email Addresses:")
for e in set(emails):
    print("-", e)

print("\nExtracted URLs:")
for url in urls:
    print("-", url)

print("\nSuspicious Keywords Found:")
for k in keyword_matches:
    print("-", k)

# Verdict
if urls and keyword_matches:
    print("\n⚠️ Verdict: HIGH RISK PHISHING EMAIL")
else:
    print("\n✅ Verdict: Likely Safe Email")
