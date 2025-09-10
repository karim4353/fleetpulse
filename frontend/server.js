const http = require('http');
const fs = require('fs');
const index = `<html><body><h1>FleetPulse Dashboard (Prototype)</h1><p>Open API: <a href='/api'>/api</a></p></body></html>`;
http.createServer((req,res)=>{ if(req.url=='/'){ res.end(index)} else if(req.url=='/api'){ res.end(JSON.stringify({msg:'use API gateway at http://localhost:8003'})) }else res.end('') }).listen(3000, ()=>console.log('frontend:3000'));
