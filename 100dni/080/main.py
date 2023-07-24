import os
import hashlib
import base64
file_path = r"D:\Programowanie\ZeroToJunior\100dni\080\url.txt"

def save_to_file(short_url, original_url):
    with open(file_path, "a") as f:
        f.write(f"{short_url},{original_url}\n")

def generate_shor_url(original_url):
        hash_obj = hashlib.sha256(original_url.encode("utf-8"))
        hash_str = hash_obj.hexdigest()
        b64_encoded = base64.b64encode(hash_str .encode("utf-8"))[:6]
        short_url = b64_encoded.decode("utf-8").replace("/", "_").replace("+", "-")
        return short_url
    
def load_url():
    if not os.path.exists(file_path):
        return {}
    
    url_dict = {}
    with open(file_path, "r") as f:
        for line in f:
            short_url, original_url = line.strip().split(",")
            url_dict[short_url] = original_url
            
        return url_dict
    
def main():
    url_dict = load_url()
    
    while True:
        user_input = input("Podaj adres URL lub skrócony adres URL (q aby zakończyć): ")
        
        if user_input == "q":
            break
        
        if user_input in url_dict:
            print(f"Oryginalny adres url: {url_dict[user_input]}")
        else:
            short_url = generate_shor_url(user_input)
            if short_url not in url_dict:
                save_to_file(short_url, user_input)
                url_dict[short_url] = user_input
                print(f"Skrócony adres URL: {short_url}")
            else:
                print("Skrót już istnieje. Spróbuj ponownie.")
        
if __name__ == "__main__":
    main()
    
    