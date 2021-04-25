import hashlib
import time
import keyfunction

possibles = keyfunction.get_possible_characters()

k = keyfunction.Key(possibles)

k.add()

pw_decrypted = input('Enter password to be encrypted: ')
pw_encrypted = hashlib.md5(pw_decrypted.encode('utf-8')).hexdigest()

print('Encoded password:' + pw_encrypted)

time.sleep(2)

print('Possible Characters:' + possibles)

time.sleep(2)

print('starting...')

time.sleep(2)
time_before = time.time()

while hashlib.md5(k.convertToString().encode('utf-8')).hexdigest() != pw_encrypted:
    k.next()
    print(str(k.key) + ' : ' + str(hashlib.md5(k.convertToString().encode('utf-8')).hexdigest()))

print('Decryption done\nthe password is:' + k.convertToString())
print('Decrypted in ' + str(time.time() - time_before) + ' seconds')