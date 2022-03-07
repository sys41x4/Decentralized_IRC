from web3 import Web3, EthereumTesterProvider
from web3 import Web3
#from web3.auto import w3

w3 = Web3(EthereumTesterProvider())
w3.isConnected()
print(w3.eth.get_block('latest'))

# Retrive file from https://dweb.link/ipfs/bafybeidd2gyhagleh47qeg77xqndy2qy3yzn4vkxmk775bg2t5lpuy7pcu
#                   https://bafybeidd2gyhagleh47qeg77xqndy2qy3yzn4vkxmk775bg2t5lpuy7pcu.ipfs.dweb.link
# https://dweb.link/ipfs/ + CID
# or https://<CID>+.ipfs.dweb.link/<FileName>
# Example
#       https://bafybeidd2gyhagleh47qeg77xqndy2qy3yzn4vkxmk775bg2t5lpuy7pcu.ipfs.dweb.link/dr-is-tired.jpg


# PS G:\Programming\My_projects\python\decentralized_irc_Project> node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjn1vP0JvKnR61sq7rMaTc C:\Users\Arijit\Pictures\wallpapers\wp2747939.jpg
# Uploading 1 files
# Content added with CID: bafybeib752offm5y7dh63gmnwh57xdx4qrmnf5ij7ow4gsjcpzkz5blu3q
# PS G:\Programming\My_projects\python\decentralized_irc_Project> node put-files.js --token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjn1vP0JvKnR61sq7rMaTc C:\Users\Arijit\Pictures\wallpapers\test.jpg     
# Uploading 1 files
# Content added with CID: bafybeib752offm5y7dh63gmnwh57xdx4qrmnf5ij7ow4gsjcpzkz5blu3q

# Where wp2747939.jpg & test.jpeg are same image having same hash values


# We can do is before uploading the file calculate the hash of the file, if hash history is avilable in "hash : file link" log, then the file will not be uploaded and the previous stored link weill be pushed in the chat