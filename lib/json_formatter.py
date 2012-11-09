import json
import urllib

import webapp2


class JSONFormatterHandler(webapp2.RequestHandler):
    def get(self):
        text = self.request.get('text', '')
        url = self.request.get('url', '')
        
        if url:
            text = urllib.urlopen(url).read() 
             
        html= '''
        <form action="/json_formatter" method="get">
        <textarea name="text" rows="20" cols="100" placeholder="{&quot;hello&quot;: &quot;world&quot;}">%s</textarea><br />
        <input type="text" name="url" size="140" placeholder="url"><br />
        <input type="submit">
        </form>
        %s
        ''' %(text, json.dumps(text, indent=4))
        self.response.write(html)
