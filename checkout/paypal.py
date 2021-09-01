import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "Aa0DEVAQ0LcPpfmvvjbSRp4cyJrcflp_633fvCvdcfDPRzg6VCJCebHdlWaOxnhrcvBc3CB2Kid7y7YA"
        self.client_secret = "EEskRxYsBbdBdImEWDALAqrWDaitxJxkMGp196mC1isruurLU-rOQ-SjZipjxCR9LKO6Eqc4EVzxzRd3"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
