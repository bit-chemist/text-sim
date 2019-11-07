Compare 2 texts for similarity  
  
`docker build -t text-sim:latest .`  
`docker run -d -p 5000:5000 text-sim`  
`curl -d "@1v2.json" -H "Content-Type: application/json" -X POST 0.0.0.0:5000/text-sim/api/v1.0/compare`