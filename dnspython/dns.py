import dns.resolver

def resolve_dns(domain):
    dns_name = dns.resolver.query(domain, 'A')
    for i in dns_name.response.answer:
        for j in i.items:
            if isinstance(j, dns.rdtypes.IN.A.A):
                print 'IP: \t %s' % (j.address)

if __name__ == "__main__":

    for i in range(100):
        domain = "hzcet01.qa.webex.com"
        resolve_dns(domain)
