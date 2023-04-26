import requests
import pprint

url = "https://openai80.p.rapidapi.com/chat/completions"


question = input ('¿Qué quieres saber hoy?: ')
#question = 'Resume el Quijote en 4 líneas como si se lo contaras a un guiri'
#question =  '¿Es el Quijote una burla a las novelas caballerescas?'

while question != 'nada':
	payload = {
		"model": "gpt-3.5-turbo",
		"messages": [
			{
				"role": "user",
				"content": question
			}
		]
	}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "44cbf57424msh681e1ea55e11f93p17ebaajsn5504512b94d3",
		"X-RapidAPI-Host": "openai80.p.rapidapi.com"
	}		

	response = requests.post(url, json=payload, headers=headers)

	#pprint.pprint(response.json())
	print ('\n', response.json()['choices'][0]['message']['content'] , '\n') #Aquí elijo el elemento 'content' dentro de 'message', dentro del elemento 0 de la lista 'choices'
	question = input ('\n¿Qué más quieres saber? (escribe "nada" para salir): ')
print ('Fin de la restransmisión')