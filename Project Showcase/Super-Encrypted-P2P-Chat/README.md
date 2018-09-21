# Super Encrypted P2P Chat System

This repository hosts 2 types of encryption, a joke that I found on r/ProgrammerHumor and proper AES Symmetric encryption. And I would like to mention that most of the code from the proper encryption was "forked" from a popular tutorial website, and since it works so well it was pointless to make my own, I just added encryption to it! You can find the original code [here](https://www.geeksforgeeks.org/simple-chat-room-using-python/)!

**Note: Proper encryption will only work in linux, I tried to trouble shoot with windows but scockets aren't very intuitive to use, so if you do have a solution then make a pull request or issue**

Video of this Project: COMMING SOON!

# Instructions for Joke Encryption:
- Launch the server with your computers IP adress this can either be Global, Lan or Localhost (127.0.0.1) then type a port I recomend using 9000
- Launch the client type the same IP and port then volia, though its only 1 way
- Enjoy!

# Instructions for Proper Encryption
- Use linux, preferabbly the inbuilt bash console for windows and install PyCrypto with pip which you probably need to download but before sudo apt-get update then sudo apt-get python-pip then pip install PyCrypto
- Launch the server with your computers IP adress this can either be Global, Lan or Localhost (127.0.0.1) then type a port I recomend using 9000
- Launch the client type the same IP and port.
- Type the key for a chatroom or type a new key for a new chatroom. Every key is a different chatroom
- Enjoy!
