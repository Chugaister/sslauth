# sslauth

## Description

This project is tiny webserver that shares a single file. It is helpful when you want to get an ssl certificate but do not have your own DNS name. There is range of services which can authenticate your server with HTTP file upload method. You should download a file provided by the service on your server and deploy this app.

## Environment

#### Install python 3.10.11 from [official site](https://www.python.org/downloads/release/python-31011/)
Another versions may also work

#### Install dependencies

`pip install -r requirements.txt`

## Usage
#### Basic configuration

`python wsgi.py --file_path FILE_PATH`

#### You can configure host, port and path
`wsgi.py [-h] --file_path FILE_PATH [--endpoint_path ENDPOINT_PATH] [--host HOST] [--port PORT]`

#### Options:

<code>
--file_path FILE_PATH, -F FILE_PATH<br>
--endpoint_path ENDPOINT_PATH, -E ENDPOINT_PATH<br>
--host HOST, -H HOST<br>
--port PORT, -P PORT<br>
</code>