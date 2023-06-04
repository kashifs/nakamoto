import hashlib

hash_table = {}

# dummy = "7a94d9a9"

def iterate_nonce(input_value, nonce_range):

    nonce = 0

    while nonce <= nonce_range:
        # Combine the input value and nonce
        data = input_value + str(nonce)

        # Calculate the hash value, truncate it
        hash_value = hashlib.md5(data.encode()).hexdigest()[:8]

        collision_found = search_hash_table(hash_value)
        if(collision_found):
            print("Collision part 1: " + collision_found + ": " + hash_value)
            print("Collision part 2: " + data + ": " + hash_value)

        # print (data)
        if data in hash_table:
            print("Input already exists in the hash table.")
        else:
            hash_table[data] = hash_value
            # print("Hash stored successfully.")

        # Increment the nonce
        nonce += 1


def search_hash_table(value):
    for key, stored_value in hash_table.items():
        if stored_value == value:
            return key  # Return the key associated with the value
    
    return None  # Value not found in the hash table


# Example usage
iterate_nonce("nakamoto", 2 ** 32)

# print()
# print("nakamoto0:" + " " + hash_table["nakamoto0"])
# print("nakamoto1:" + " " + hash_table["nakamoto1"])
# print("nakamoto2:" + " " + hash_table["nakamoto2"])
# print("nakamoto3:" + " " + hash_table["nakamoto3"])
# print("nakamoto4:" + " " + hash_table["nakamoto4"])
# print("nakamoto5:" + " " + hash_table["nakamoto5"])
# print("nakamoto6:" + " " + hash_table["nakamoto6"])
# print("nakamoto7:" + " " + hash_table["nakamoto7"])
# print("nakamoto8:" + " " + hash_table["nakamoto8"])
# print("nakamoto9:" + " " + hash_table["nakamoto9"])

# print()
# print(search_hash_table(dummy))


