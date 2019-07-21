import argparse
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime, timedelta


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    for url in load_urls4check(namespace.file):
        print_state_site(url)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType(), help='path to file')
    return parser


def load_urls4check(file_obj):
    urls = [line.strip() for line in file_obj if line.strip()]
    file_obj.close()
    return urls


def is_server_respond_with_200(url):
    return requests.get(url).ok


def get_domain_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name).expiration_date
    if isinstance(expiration_date, list):
        return expiration_date[0]
    return expiration_date


def print_state_site(url):
    respond = 'ON'
    try:
        if not is_server_respond_with_200(url):
            respond = 'OFF'
    except requests.exceptions.RequestException as e:
        print('{:3} {}'.format('ОШИБКА', url))
        print(e)
        return

    domain_name = urlparse(url).netloc
    expiration_date = get_domain_expiration_date(domain_name)

    expiration_text = 'Непроплачено'
    if expiration_date - datetime.now() > timedelta(days=30):
        expiration_text = 'Проплачено'
    print('{:3} {} {}'.format(respond, expiration_text, url))


if __name__ == '__main__':
    main()
