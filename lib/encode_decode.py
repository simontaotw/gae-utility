import urllib

import webapp2


class EncodeDecodeHandler(webapp2.RequestHandler):
    def get(self):
        self.post()

    def post(self):
        url = self.request.get('url', '')
        action = self.request.get('action', '')
        value = ''    

        if 'encode' == action:
            value = urllib.quote(url, '') 
        else:
            value = urllib.unquote(url)

        html = '''
        <form action="/encode" method="post">
        <textarea name="url" rows="10" cols="50" placeholder="http://www.google.com">%s</textarea><br />
        <input type="submit" name="action" value="encode">
        <input type="submit" name="action" value="decode">
        </form>
        ''' %value
        self.response.write(html)
