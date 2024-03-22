# vcard/middlewares.py

class SubdomainMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract subdomain from the request host
        host = request.get_host()
        print("Request Host:", host)
        subdomain = host.split('.')[0] if '.' in host else None
        print("Extracted Subdomain:", subdomain)

        # Set the subdomain attribute on the request object
        request.subdomain = subdomain

        # Call the next middleware in the chain or the view function
        response = self.get_response(request)

        return response
