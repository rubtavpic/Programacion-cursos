
var http = require('http');

var server = http.createServer(function(request, response){
    response.writeHead(200, {'Content-Type': 'text/html; charset=UTF-8'});
    response.end('<h3>Wake up, Neo...</h3>\n');
});

// Arrancar el servidor
server.listen(1337, '127.0.0.1');
console.log('Servidor arrancado en 127.0.0.1:1337');