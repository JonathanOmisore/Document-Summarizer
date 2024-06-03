from flask import Flask, request, render_template, jsonify
from langchain import LanguageChain, SummarizeDocumentChain

app = Flask(__name__)

# Initialize the language model and summarization chain
langchain = LanguageChain()
summarizer = SummarizeDocumentChain(language_chain=langchain)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    document = request.form.get('document')
    if not document:
        return jsonify({'error': 'No document provided'}), 400

    # Summarize the document
    summary = summarizer.summarize(document)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)
