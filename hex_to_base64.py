from binascii import a2b_hex, b2a_base64

def hex_to_base64(string):
	bin = a2b_hex(string)
	converted = b2a_base64(bin)
	return converted

if __name__ == "__main__":
	string = raw_input("Enter hex string: ")
	print hex_to_base64(string)
