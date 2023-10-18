from gevent.pywsgi import WSGIServer
from app import CustomFlask, ArgsError
from argparse import ArgumentParser

default_host = CustomFlask.get_external_ip()
default_port = 80
default_endpoint_path = '/.well-known/pki-validation'

parser = ArgumentParser()
parser.add_argument(
    '--file_path', '-F',
    required=True,
    action='store',
    help='Authentication file path'
)
parser.add_argument(
    '--endpoint_path', '-E',
    default=default_endpoint_path,
    action='store',
    help=f'Endpoint path ({default_endpoint_path} default)'
)
parser.add_argument(
    '--host', '-H',
    action='store',
    default=default_host,
    help=f'Host ip address to run server on ({default_host} default)'
)
parser.add_argument(
    '--port', '-P',
    action='store',
    default=80,
    help=f'Port to run on ({default_port} default)'
)
args = parser.parse_args()


def main():
    try:
        app = CustomFlask(
            args.file_path,
            args.endpoint_path,
            args.host,
            args.port,
            __name__
        )
    except ArgsError as exc:
        print("Error:", exc)
        return
    print(f"You may follow {app.get_url()} and check if server works")
    http_server = WSGIServer(
        (app.host, app.port),
        app
    )
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
