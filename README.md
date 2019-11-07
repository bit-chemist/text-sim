Compare 2 texts for similarity  
  
Run locally  
`python3 ./app/app.py`  

OR  

Build and run the docker container  
`docker build -t text-sim:latest .`  
`docker run -d -p 5000:5000 text-sim`  
  
Test with payloads  
`cd test`  
  
`curl -d "@1v2.json" -H "Content-Type: application/json" -X POST 0.0.0.0:5000/text-sim/api/v1.0/compare`  
Answer: 65  
  
`curl -d "@1v3.json" -H "Content-Type: application/json" -X POST 0.0.0.0:5000/text-sim/api/v1.0/compare`  
Answer: 0.17857142857142858  
