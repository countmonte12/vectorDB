import chromadb
from flask import Flask, jsonify,request
    
app = Flask(__name__)
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="Prompts")
id=0
collection.add(
    documents=["doc1000101", "doc288822"],
    metadatas=[{"response": "style1"}, {"response": "style2"}],
    ids=["uri9", "uri10"],
)

@app.route('/api/addResponse', methods=['POST'])
def add_data(): 
    global id
    request_data = request.get_json()
    id=id+1
    prompt=request_data.get('prompt')
    response=request_data.get('response')
    print(prompt,response)
    results = collection.add(
    documents=[prompt],
    metadatas=[{"response": response}],
    
    ids=[f"id"])
    return "Added"
    


    



@app.route('/api/getResponses', methods=['POST'])
def get_data():
    request_data = request.get_json()
    prompt=request_data.get('prompt')
    results = collection.query(
    query_texts=[prompt],
    n_results=4)

    responses = [item["response"] for sublist in results["metadatas"] for item in sublist]
    return responses


if __name__ == '__main__':
    app.run(debug=True)

