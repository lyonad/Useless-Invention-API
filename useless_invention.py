import requests

def get_useless_fact():
    """
    Fetches a random useless fact from the Useless Facts API.
    """
    url = 'https://uselessfacts.jsph.pl/random.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['text']
    else:
        return "Failed to fetch a useless fact. Maybe that's the point?"

def main():
    print("Welcome to the Useless Fact Generator!")
    print("This invention fetches completely useless facts from the internet.")
    print("Why? Because why not?\n")
    
    fact = get_useless_fact()
    print(f"Your useless fact: {fact}")
    
    # To make it even more useless, let's add a silly commentary
    print("\nCommentary: This fact is so useless, it might just change your life... or not.")

if __name__ == "__main__":
    main()