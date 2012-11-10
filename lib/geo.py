import webapp2

from external import geohash


class GeohashHandler(webapp2.RequestHandler):  
    def get(self):
        self.post()

    def post(self):
        hash_value = ''
        coordinates = self.request.get('coordinates', '')
        if coordinates:
            lat = coordinates.split(',')[0]
            lng = coordinates.split(',')[1]
            hash_value = geohash.encode(float(lat), float(lng))

        html = '''
        <form action="/geohash" method="post">
        <input type="text" name="coordinates" placeholder="37.7,-122.4" value="%s">
        <input type="submit" value="hash">
        </form>
        %s
        ''' %(coordinates, hash_value)
        self.response.write(html)
