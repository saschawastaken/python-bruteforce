import hashlib
import time
import keyfunction

possibles = keyfunction.get_possible_characters()

ENpassword = input('Enter the encrypted password: ')

k = keyfunction.Key(possibles)
k.add()

time_before = time.time()

print("decrpyting...")

while hashlib.md5(k.convertToString().encode('utf-8')).hexdigest() != ENpassword:
    k.next()

print('Done\nThe decrypted password is: ' + k.convertToString())
print('Done in ' + str(time.time() - time_before) + 'seconds')