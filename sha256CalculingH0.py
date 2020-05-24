import sys
import os

from Crypto.Hash import SHA256

def main():
    blockSize = 1024
    filePath = sys.argv[1]
    fileSize = os.path.getsize(filePath)
    lastBlockSize = fileSize % blockSize
    fileOpen = open(filePath, 'rb')
    lastHashCalculated = ''
    for chunk in readChunksInversed(fileOpen, fileSize, lastBlockSize, blockSize):
		sha256 = SHA256.new()
		sha256.update(chunk)
		if(lastHashCalculated):
			sha256.update(lastHashCalculated)
		lastHashCalculated = sha256.digest()
    fileOpen.close()

    print 't3 - seguranca de sistemas - paulo aranha'
    print 'h0 for file in', filePath, ' ', lastHashCalculated.encode('hex')

def readChunksInversed(file, fileSize, lastChunkSize, chunkSize):
	flag = True
	lastReadedPosition = fileSize
	while lastReadedPosition>0:
		size = chunkSize
		if(flag):
			size = lastChunkSize
			flag = False
		file.seek(lastReadedPosition - size)
		data = file.read(chunkSize)
		lastReadedPosition -= size
		yield data

main()