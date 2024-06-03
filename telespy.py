"""
                                                                                          
                                                                                          
                                                                                          
                                         .........                                        
                                ..::------------------::..                                
                            .:------------------------------:..                           
                        .:--------------------------------------:.                        
                      :--------------------------------------------:.                     
                   .:---------------:...---------:...-----------------.                   
                 .-----------------      .:----:      ------------------:                 
               .------------------.                    -------------------.               
              :-------------------                     :-------------------:              
             --------------------:                     .---------------------.            
           .---------------------                       ----------------------.           
          .---------------------:                       .----------------------.          
          ----------------------:                        -----------------------.         
         -------------------------::..              ..::-------------------------         
        .------------------::....::--------------------::....:-------------------:        
        ----------------:             .....::::.....            .-----------------        
       .---------------.                                          ----------------.       
       :----------------.                                       .:----------------:       
       :----------------::::.                               ..:-:.:----------------       
       :--------------:     .:---::::...............::::::--..      :--------------       
       :------------:        .--      .....----.....      :-         .-------------       
       :----------:           .-:.        .----.        .:--           :----------:       
       .-----------:.          :----:::::---------::::----:.         .:-----------:       
        ---------------:.       .---------------------:.          .:--------------        
        :-----------------::.     :-----------------.          .-----------------:        
         -----------------::.      .-------------:.          .::-----------------         
          ---------------:           .---------:.            ..:::--------------.         
          .-----------------:.         .:-----.         .::--------------------:          
           .--------------------:.        :-:       .:------------------------:           
            .-----------------------:.   .-.    .:---------------------------.            
              :-------------------------:-    :-----------------------------              
               .-------------------------  .:-----------------------------:               
                 :----------------------..:-----------------------------:                 
                   .-------------------::-----------------------------:                   
                     .:---------------------------------------------.                     
                        .:---------------------------------------.                        
                           .:--------------------------------:.                           
                               ..::--------------------::..                               
                                       .............                                      
                                                                                          
                                                                                          
                                                                                         

TeleSpy: Telegram OSINT Tool

Author: K3ySton3

Usage: python telespy.py --api-id YOUR_API_ID --api-hash YOUR_API_HASH --phone YOUR_PHONE --channel CHANNEL_NAME --output output.json

Example: python telespy.py --api-id 123456 --api-hash abcdef1234567890 --phone +1234567890 --channel my_channel --output output.json

"""

import argparse
import logging
import json
from telethon import TelegramClient, events, sync
from telethon.tl.types import PeerChannel

# Initialize the logger
logging.basicConfig(level=logging.INFO)

# Function to scrape a Telegram channel
def scrape_telegram(api_id, api_hash, phone, channel_name, output_file, verbose):
    # Initialize the Telegram client
    client = TelegramClient('session_name', api_id, api_hash)

    # Connect to Telegram
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))

    # Function to handle new messages
    @client.on(events.NewMessage(chats=channel_name))
    async def new_message_handler(event):
        message = event.message.message
        sender = await event.get_sender()
        sender_username = sender.username
        chat = await event.get_chat()
        chat_title = chat.title

        # Collect the data
        data = {
            'sender_username': sender_username,
            'message': message,
            'chat_title': chat_title,
            'chat_id': chat.id
        }

        # Save the data to the output file
        with open(output_file, 'a') as f:
            f.write(json.dumps(data) + '\n')
        
        logging.info(f"Scraped data: {data}")

    if verbose:
        print("TeleSpy is now running...")
        print(f"Scraping messages from Telegram channel: {channel_name}")
        print(f"Outputting results to file: {output_file}")
    else:
        print("TeleSpy is now running in silent mode. Use -v to see TeleSpy's processes.")

    # Start listening to the channel
    client.run_until_disconnected()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Telegram OSINT Tool")
    parser.add_argument('--api-id', type=int, required=True, help='Telegram API ID')
    parser.add_argument('--api-hash', type=str, required=True, help='Telegram API Hash')
    parser.add_argument('--phone', type=str, required=True, help='Your phone number associated with Telegram')
    parser.add_argument('--channel', type=str, required=True, help='Telegram channel name or ID to scrape')
    parser.add_argument('--output', type=str, help='Output file for scraped data')
    parser.add_argument('-v', '--verbose', action='store_true', help='Display running processes of TeleSpy')
    args = parser.parse_args()

    scrape_telegram(args.api_id, args.api_hash, args.phone, args.channel, args.output, args.verbose)

