from rules import check_url

def test():
    urls = [
        "http://google.com",
        "http://suspicious-login-update.zip/verify@google.com",
        "http://192.168.1.1/login",
        "https://www.amazon.com/gp/help/customer/display.html"
    ]
    
    for url in urls:
        result = check_url(url)
        print(f"URL: {url}")
        print(f"Level: {result['level']}, Score: {result['score']}")
        print(f"Reasons: {result['reasons']}")
        print("-" * 20)

if __name__ == "__main__":
    test()
