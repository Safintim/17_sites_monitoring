import argparse
import requests
import whois
from urllib.parse import urlparse
from datetime import datetime, timedelta


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    for url in load_urls4check(namespace.file):
        respond = is_server_respond_with_ok(url)
        domain_name = urlparse(url).netloc
        expiration_date = get_domain_expiration_date(domain_name)
        print_state_site(url, expiration_date, respond)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=is_file, help='path to file')
    return parser


def is_file(filepath):
    if os.path.isfile(filepath):
        return filepath
    raise argparse.ArgumentTypeError('file not found')


def load_urls4check(filepath):
    with open(filepath) as urlsfile:
        return [line.strip() for line in urlsfile if line.strip()]


def is_server_respond_with_ok(url):
    try:
        return requests.get(url).ok
    except requests.exceptions.RequestException:
        return False


def get_domain_expiration_date(domain_name):
    expiration_date = whois.whois(domain_name).expiration_date
    if isinstance(expiration_date, list):
        return expiration_date[0]
    return expiration_date


def print_state_site(url, expiration_date, respond):
    respond_text = 'OFF'
    if respond:
        respond_text = 'ON'

    if not expiration_date:
        expiration_text = 'Ошибка'
    elif expiration_date - datetime.now() > timedelta(days=30):
        expiration_text = 'Проплачено'
    else:
        expiration_text = 'Непроплачено'

    print('{:3} {} {}'.format(respond_text, expiration_text, url))


if __name__ == '__main__':
    main()
