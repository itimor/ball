import random
import base64
from .settings import PROXIES


class RandomUserAgent(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        cur_agent = random.choice(self.agents)
        print("**************User-Agent: %s************" % cur_agent)
        request.headers.setdefault('User-Agent', cur_agent)


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_pass']:
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
            encoded_user_pass = base64.b64encode(proxy['user_pass'].encode('utf-8'))
            request.headers['Proxy-Authorization'] = 'Basic ' + str(encoded_user_pass, encoding="utf-8")
            print("************** %s: ProxyMiddleware have pass************" % proxy['ip_port'])
        else:
            print("************** %s: ProxyMiddleware no pass************" % proxy['ip_port'])
            request.meta['proxy'] = "http://%s" % proxy['ip_port']
