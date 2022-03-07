// Name the file `retrieve.mjs` so you can use `import` with nodejs  
// Run `npm i web3.storage` to install this package
import { Web3Storage } from 'web3.storage'

// const token = process.env.API_TOKEN

const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc'
const client = new Web3Storage({ token })

async function retrieveFiles () {
  const cid =
    'bafybeidd2gyhagleh47qeg77xqndy2qy3yzn4vkxmk775bg2t5lpuy7pcu'
  // You can fetch data using any CID, even from IPFS Nodes or Gateway URLs!
  const res = await client.get(cid)
  const files = await res.files()

  for (const file of files) {
    console.log(`${file.cid}: ${file.name} (${file.size} bytes)`)
  }
}

retrieveFiles()
// Now run it with 
// API_TOKEN=YOUR_TOKEN_HERE node ./retrieve.mjs 