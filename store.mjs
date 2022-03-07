// Name the file `store.mjs` so you can use `import` with nodejs 
// Run `npm i web3.storage` to install this package
import { Web3Storage, getFilesFromPath } from 'web3.storage'

// const token = process.env.API_TOKEN

const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweGExMjU1MURGNUMxNzZmNDU0Y2EwRjQ1NUE0NUFjMjg4ODgzRjIwYzMiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2NDYwNzU4NjY2NzQsIm5hbWUiOiJpcmMtdG9rZW4xIn0.sF0bUr8lwfr1e9-Yuv6-wJun1vP0JvKnR61sq7rMaTc'
const client = new Web3Storage({ token })

async function storeFiles () {
//  const files = await getFilesFromPath('/path/to/file')
  const files = await getFilesFromPath('C:\Users\Arijit\Pictures\wallpapers\wp2747939.jpg')
  const cid = await client.put(files)
  console.log(cid)
}

storeFiles()
// Now run it with 
// API_TOKEN=YOUR_TOKEN_HERE node ./store.mjs