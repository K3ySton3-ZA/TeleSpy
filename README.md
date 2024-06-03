![TeleSpy Logo](https://github.com/K3ySton3-ZA/TeleSpy/raw/main/TeleSpy.png)

# TeleSpy

**TeleSpy** is a powerful and user-friendly CLI tool designed for OSINT (Open Source Intelligence) and cybersecurity professionals. It enables efficient scraping of usernames, text messages, and channel names from Telegram. Ideal for gathering and analyzing open-source intelligence, TeleSpy helps you stay ahead in the ever-evolving landscape of cyber threats.

## Features

- Scrape Telegram for usernames, text messages, and channel names
- Save data in JSON format for easy analysis
- Simple command-line interface for ease of use
- Leverages the `telethon` library for interacting with the Telegram API

## Installation

**Clone the repository**:
  
   ```
   git clone https://github.com/K3ySton3-ZA/telespy.git
   cd telespy
   ```
**Create a virtual environment (optional but recommended)**:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Install the required dependencies**:

```
pip install -r requirements.txt
```

## Getting Started
### Telegram API Setup
1. Go to my.telegram.org.
2. Log in with your phone number.
3. Create a new application to get your api_id and api_hash.

## Running TeleSpy
Run the script with the required arguments from your terminal:

```
python telespy.py --api-id YOUR_API_ID --api-hash YOUR_API_HASH --phone YOUR_PHONE --channel CHANNEL_NAME --output output.json
```

### Arguments
- --api-id: Your Telegram API ID (required)
- --api-hash: Your Telegram API Hash (required)
- --phone: Your phone number associated with Telegram (required)
- --channel: Telegram channel name or ID to scrape (required)
- --output: Output file for scraped data (required)
- --use-session: Use an existing session file for authentication instead of requiring you to enter your phone number, API ID, and API hash. If this file does not exist, TeleSpy will create one after first successful authentication.

### Example
```
python telespy.py --api-id 123456 --api-hash abcdef1234567890 --phone +1234567890 --channel my_channel --output output.json
```

## Legal and Ethical Considerations
- API Limits: Be aware of Telegram's API rate limits to avoid being banned.
- Permissions: Ensure you have permission to scrape the data and comply with local laws and Telegram's terms of service.

## Contributing
We welcome contributions to improve TeleSpy! Please fork the repository and submit pull requests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or issues, please open an [issue](https://github.com/K3ySton3-ZA/TeleSpy/issues) on GitHub or contact us at connect@mayanstegmann.com.

---
Enjoy using TeleSpy for your OSINT and cybersecurity needs!


