import webapp2

import geohash


class GeohashHandler(webapp2.RequestHandler):  
    def get(self):
        hash_value = ''
        coordinates = self.request.get('coordinates', '')
        if coordinates:
            lat = coordinates.split(',')[0]
            lng = coordinates.split(',')[1]
            hash_value = geohash.encode(float(lat), float(lng))

        html = '''
        <form action="/geohash" method="get">
        <input type="text" name="coordinates" placeholder="37.7,-122.4" value="%s">
        <input type="submit" value="hash">
        </form>
        %s
        ''' %(coordinates, hash_value)
        self.response.write(html)
