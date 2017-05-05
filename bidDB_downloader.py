import requests
import json
import re
import threading
from joblib import Parallel, delayed
from util.cli_parser import CLIParser

# Create mutex
mutex = threading.Lock()


# Get vulnerability title from HTML body
def get_title(body):
    init_index = body.index('<span class="title">') + len('<span class="title">')
    return body[init_index:body.index('</span>')]


# Get vulnerable products from HTML body
def get_vulnerable_products(body):
    tmp_body = get_info_by_label(body, 'Vulnerable')
    if '<span class="related">' in tmp_body:
        regex = re.compile(r"<span class=\"related\">(\n.*){5}<\/span>", re.MULTILINE)
        tmp_body = re.sub(regex, '', tmp_body)
    splitted_body = tmp_body.split('<br/>')
    vuln_products = []
    for line in splitted_body:
        line = line.rstrip().lstrip()
        if len(line) != 0:
            vuln_products.append(line)
    return vuln_products


# Get specific BID info
def get_info_by_label(body, label):
    init_index = body.index('<span class="label">' + label + ':</span>') + \
                 len('<span class="label">' + label + ':</span>')
    tmp_body = body[init_index:]
    init_index = tmp_body.index('<td>') + len('<td>')
    tmp_body = tmp_body[init_index:]
    tmp_body = tmp_body[:tmp_body.index('</td>')]
    return tmp_body.rstrip().lstrip()


# Get CVEs
def get_linked_CVEs(body):
    regex = r"(CVE-[0-9]{4}-[0-9]{4,5})"
    cves_obj = re.search(regex, body)
    cves = []
    if cves_obj:
       for group in cves_obj.groups():
           cves.append(group)
    return cves


# Prepares output
def prepare_output(title, bugtraq_id, clazz, linked_cves, is_local, is_remote, vuln_products):
    data = {}
    data['title'] = title
    data['bugtraq_id'] = bugtraq_id
    data['class'] = clazz
    data['cve'] = linked_cves
    data['local'] = is_local.lower()
    data['remote'] = is_remote.lower()
    data['vuln_products'] = vuln_products
    return data


# Requests the bid, parses the HTML and prints the BugTraq info
def get_bid(bugtraq_id):
    r = requests.get("http://www.securityfocus.com/bid/" + str(bugtraq_id))
    if r.status_code == 200:
        try:
            body = r.content.decode("utf-8")
            body = body[body.index('<div id="vulnerability">'):body.index('<span class="label">Not Vulnerable:</span>')]
            title = get_title(body)
            clazz = get_info_by_label(body, 'Class')
            linked_cves = get_linked_CVEs(body)
            is_local = get_info_by_label(body, 'Local')
            is_remote = get_info_by_label(body, 'Remote')
            vuln_products = get_vulnerable_products(body)
        except:
            vuln_products = []
        if len(vuln_products) > 0:
            mutex.acquire()
            print(json.dumps(prepare_output(title, bugtraq_id, clazz, linked_cves, is_local, is_remote, vuln_products),
                             sort_keys=True), flush=True)
            mutex.release()


# Executes the main function called get_bid in a parallel way
def main(parser_args):
    Parallel(n_jobs=parser_args.get_workers())(delayed(get_bid)(i) for i in range(parser_args.get_first_bid(),
                                                                                  parser_args.get_last_bid() + 1))

if __name__ == '__main__':
    main(CLIParser())
