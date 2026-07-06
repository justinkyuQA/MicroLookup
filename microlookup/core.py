import socket

def lookup(target):

    print()
    print("MicroLookup")
    print("=" * 40)

    try:

        ip = socket.gethostbyname(target)
        print("Hostname :", target)
        print("IPv4      :", ip)

        try:
            reverse = socket.gethostbyaddr(ip)
            print("Reverse   :", reverse[0])
        except:
            print("Reverse   : Not Available")

    except Exception as e:
        print("Lookup failed.")
        print(e)
