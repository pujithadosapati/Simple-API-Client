import requests
# Public REST API URL
API_URL = "https://jsonplaceholder.typicode.com/posts/1"
def get_post():
    try:
        # Send GET request
        response = requests.get(API_URL, timeout=10)

        # Check HTTP status code
        response.raise_for_status()

        # Convert JSON response into Python data
        data = response.json()

        # Display selected information
        print("\n===== API RESPONSE =====")
        print("Post ID:", data["id"])
        print("User ID:", data["userId"])
        print("Title:", data["title"])
        print("Body:", data["body"])

        print("\nAPI data retrieved successfully!")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server.")

    except requests.exceptions.HTTPError as error:
        print("HTTP Error:", error)

    except ValueError:
        print("Error: Invalid JSON response.")

    except requests.exceptions.RequestException as error:
        print("Request Error:", error)

# Main program
if __name__ == "__main__":
    get_post()
