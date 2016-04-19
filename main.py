import web

urls = (
    '/(.*)', 'hello'
)

class hello:        
    def GET(self, name):
        if not name: 
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
	class MyApplication(web.application):
		def run(self, port=8080, *middleware):
			func = self.wsgifunc(*middleware)
			return web.httpserver.runsimple(func, ('0.0.0.0', port))

	app = MyApplication(urls, globals())
	app.run(port=8080)
