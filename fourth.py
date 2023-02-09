"""The solution of the fourth problem."""


from http.client import HTTPConnection


def get_public_ip() -> str:
    """Found yout pulic ip.

    Returns:
        str: your public ip address.
    """
    connection = HTTPConnection("ifconfig.me")
    connection.request("GET", "/ip")
    return str(connection.getresponse().read())[2:-1]


print(get_public_ip())
