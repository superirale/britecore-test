from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb-9fWdnh0XRL5kVN162SXEISmFBo0E8euG9tjZ-M4gF1t_WxND4V_IFluj6pe8P1S62INrQIPIzOVdkbem5Xd2yQ6JQTynjnk5v8i7XU6jVLOK1o9-zgIef1WCfvGwtTM2zLwUw0KAt9fwiG87rdOEabAhoYGx54CTkUdckGTR2j1UMsjWAAw6j7hzvP9fj30diBy'

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()