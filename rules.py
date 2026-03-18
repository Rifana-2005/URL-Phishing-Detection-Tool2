import re
from urllib.parse import urlparse

def check_url(url):
    """
    Analyzes a URL for phishing characteristics.
    Returns a dictionary with score, level, and reasons.
    """
    score = 0
    reasons = []
    
    # 1. Length of URL
    if len(url) > 75:
        score += 20
        reasons.append("URL is unusually long (potential masking)")
    
    # 2. Presence of '@' symbol
    if '@' in url:
        score += 30
        reasons.append("Contains '@' symbol (often used to redirect to a different site)")
        
    # 3. Suspicious Characters/Patterns
    suspicious_patterns = [r'//', r'-', r'\.zip', r'\.exe', r'\.scr']
    for pattern in suspicious_patterns:
        if re.search(pattern, url.replace('http://', '').replace('https://', '')):
            score += 10
            reasons.append(f"Contains suspicious pattern or character: {pattern}")

    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    # 4. Number of subdomains
    if domain.count('.') > 3:
        score += 20
        reasons.append("High number of subdomains (common in phishing)")
        
    # 5. IP Address instead of Domain
    ip_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(ip_pattern, domain):
        score += 40
        reasons.append("Uses an IP address instead of a domain name")
        
    # 6. Common Phishing Keywords
    keywords = ['login', 'verify', 'update', 'account', 'banking', 'secure', 'signin', 'paypal', 'ebay', 'amazon', 'netflix']
    for keyword in keywords:
        if keyword in url.lower():
            score += 15
            reasons.append(f"Contains phishing keyword: '{keyword}'")

    # Determine risk level
    if score >= 60:
        level = "High"
    elif score >= 30:
        level = "Medium"
    else:
        level = "Low"
        if not reasons:
            reasons.append("No common phishing patterns detected.")
            
    return {
        "url": url,
        "score": min(score, 100),
        "level": level,
        "reasons": reasons
    }
