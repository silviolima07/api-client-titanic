import streamlit as st
import requests
import simplejson as json
import time
from PIL import Image

def checar_retorno(send_request):
  data = send_request.json()
  temp = str(data).split()[2]
  status = temp.replace('}}', '')
  return status


def main():
    """ RandonForestClassifier - Titanic """
    
    # Titulo
    #st.title("Streamlit - Titanic")
 
    html_page = """
    <div style="background-color:tomato;padding=50px">
        <p style='text-align:center;font-size:50px;font-weight:bold'>Streamlit - Titanic</p>
    </div>
              """
    st.markdown(html_page, unsafe_allow_html=True)    

    image = Image.open("titanic.png")
    st.sidebar.image(image,caption="",use_column_width=True)
     
    st.sidebar.markdown("#### * RandomForestClassifier")
    st.sidebar.markdown("#### * Modelo alocado no Heroku")     

    st.markdown("Selecione as caracteristicas do passageiro")
    classe = st.radio('Classe',('Primeira Classe ', 'Segunda Classe', 'Terceira Classe'))
    sexo = st.radio('Sexo',('Homem', 'Mulher'))
    embarque = st.radio('Cidade de Embarque',('Cherboug', 'Queenstown', 'Southampton'))
    idade = st.slider('Idade',min_value=1, max_value=80, value=20, step=5)
    passagem = st.slider('Valor da Passagem',min_value=0, max_value=512, value=100, step=10)
    st.markdown("## Caracteristicas selecionadas do passageiro")
    st.write(classe,'---', sexo, '---',embarque,'---',idade,"anos",'---','$$',passagem)
    
    data = [{'Classe': classe, 'Sexo': sexo, 'Embarque':embarque, 'Idade': idade, 'Passagem': passagem}]
        
    # Choosen data
    data = {'Classe': classe, 'Sexo': sexo, 'Embarque':embarque, 'Idade': idade, 'Passagem': passagem}
    
    # Formato json 
    data = json.dumps(data)
      
    # url da api no heroku 
    url = 'https://app-api-001.herokuapp.com/'
       
    bar = st.progress(0)

    if st.button('Submit'):
        for i in range(11):
            bar.progress(i * 10)
            # wait
            time.sleep(0.1)

        send_request = requests.post(url, data)
        #st.text("Acessando a api no heroku...")
        if not send_request.ok:
            st.warning("Houston we have a problem.")
       
        elif send_request.ok:
            st.markdown('#### De acordo com o modelo:')
            status = checar_retorno(send_request)
            
            if status == '1':
                st.title("Sobreviveu")
                st.balloons()
            else:
                st.title("Morreu")
           



if __name__ == '__main__':
    main()

     
