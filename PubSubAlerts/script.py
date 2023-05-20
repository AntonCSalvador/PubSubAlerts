from twilio.rest import Client
import requests
from bs4 import BeautifulSoup

# Send an HTTP request and retrieve the HTML content
url = "https://arepublixchickentendersubsonsale.com/"
response = requests.get(url)
html_content = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the <h1> element and extract its text
h1_element = soup.find('h1')
h1_text = h1_element.text if h1_element else None

# Check the extracted text
if h1_text == "Not this week my dudes":
    text = "Not on sale. Maybe next week."
else:
    text = "TENDERS ON SALE. GET A SUB"


# Twilio API credentials
account_sid = "AC76760e3cbc2270007996792b7a083fb2"
auth_token = "5438bcb4af139d426d4a5cdb0eacf9c1"

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define the recipient's phone number and the message content
recipient_number = "+19048640615"  # Replace with the recipient's phone number
message = text

# Send the message
client.messages.create(
    body=message,
    from_="+18448892711",
    to=recipient_number
)
