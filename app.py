from flask import Flask, request, jsonify, Response,render_template,json
import nmt as pz

app = Flask(__name__)


#model
# model = torch.load("D:\Nerd\Desktop\webapp\model.pt")

#clean input dzongkha text
# def cleanInput(s):
#     s=str(s)
#     s = re.sub(r'་\s*[& ]', ' ',s)
#     s=re.sub(r'།','',s)
#     s=re.sub(r'\s#\s',' ',s)
#     return s


@app.route('/')
def home():
     return render_template('index.html')
 
 
@app.route('/api',methods=['POST'])
def entry():
    data = request.get_json()
    print(data)
    text=data['text']
    js = json.dumps({'text':pz.ppredict(text)})    
    resp = Response(js, status=200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
    # data = request.get_json(force=True)
    # print(data)
    # text=data['text']
    # import nmt as pz
    # js = json.dumps({'text':pz.ppredict(text)})    
    # resp = Response(js, status=200, mimetype='application/json')
    # resp.headers['Access-Control-Allow-Origin'] = '*'
    #     result = request.form
    #     # Get the sentence from the Input site
    #     Sentence = str(result['input_text'])
    #     # Converting the text into the required format for prediction
    #     # Step 1 : Converting to an array
    #     dzo = [Sentence]
    #     # Clean the input sentence
    #     cleanText = cleanInput(dzo)
    #     # Step 2 : Converting to sequences and padding them
    #     # Encode the inputsentence as sequence of integers
    #     dzo=pybo.BoString(cleanText)
        
    #     # Convert the input text to PyTorch tensors
    #     input_tensor = torch.tensor(dzo)
        
    #     # Step 3 : Get the translation tensor
    #     output_tensor =model(input_tensor)
        
    #     #convert the tensor to english words 
    #     output_words = []
    #     for index in output_tensor:
    #         word = dz.Lang.addWord[index.item()]
    #         if word == "<EOS>":
    #             break
    #         output_words.append(word)
            
    #         return " ".join(output_words)
        

if __name__ == '__main__':
      app.run(debug=True)