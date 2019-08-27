"""
:author: Gatsby Lee
:since: 2019-08-25

"serviceAccounts": [
{
    "email": string,
    "scopes": [
    string
    ]
}
]
"""
import collections

# ref: https://cloud.google.com/sdk/gcloud/reference/alpha/compute/instances/set-scopes
DEFAULT_SCOPES = (
    'https://www.googleapis.com/auth/devstorage.read_only',
    'https://www.googleapis.com/auth/logging.write',
    'https://www.googleapis.com/auth/monitoring.write',
    'https://www.googleapis.com/auth/pubsub',
    'https://www.googleapis.com/auth/service.management.readonly',
    'https://www.googleapis.com/auth/servicecontrol',
    'https://www.googleapis.com/auth/trace.append',
)


class ServiceAccounts(object):
    __slots__ = ('_accounts',)

    def __init__(self):
        self._accounts = collections.defaultdict(set)

    @staticmethod
    def create_default():
        s = ServiceAccounts()
        s.add('default', *DEFAULT_SCOPES)
        return s

    def add(self, email, *scopes):
        if email not in self._accounts and len(self._accounts) == 1:
            raise ValueError('Only one service account per VM instance is supported')
            # Only one service account per VM instance is supported.
        for s in scopes:
            self._accounts[email].add(s)

    def get(self):
        r = []
        for k in self._accounts:
            r.append({'email': k, 'scopes': list(self._accounts[k])})
        return r

    def remove_email(self, email):
        del self._accounts[email]

    def remove_scope(self, email, scope):
        self._accounts[email].remove(scope)
