# analyzer_model
### To use the package currently you need to install with below command 

### `pip install git+https://github.com/VISHU1999/analyzer_model.git`

## Analyze your documents and answer your ask question.
`From analyzer_model import doc_analyzer`.
and Use this doc_analyzer function to anaylze your documents.

doc_analyzer required two arguments . 
- File Path. 
- Question which you want to ask.

# Importent Note 
- Open a text editor or any suitable code editor on your computer.
- Create a new file and save it with the name .env. Make sure to include the dot at the beginning of the file name.
- Open the .env file in your text editor.
- Inside the .env file, add the following lines.

   -  `HUGGING_FACE_TOKEN=<YOUR_TOKEN_HERE>`
   -  `HUGGINGFACE_MODEL=<YOUR_MODEL_NAME_HERE>` its optional default model is `google/flan-t5-base`

Replace YOUR_TOKEN_HERE with your Hugging Face token and YOUR_MODEL_NAME_HERE with the name of the model you want to use.
Save the .env file.
Congratulations! You have created the .env file and added your Hugging Face token and model name to it. Make sure to keep this file secure and avoid sharing it with others, as it contains sensitive information.
### Example of analyze the resume and ask 5 question to ask based on resume

https://github.com/VISHU1999/analyzer_model/assets/70027559/17e8ff73-0bb3-4d24-9912-42b4094a8975


