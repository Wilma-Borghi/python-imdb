
# API IMDb

Api para consulta de Filmes e Séries

### Comando para iniciar
python -m uvicorn main:app --reload

### ENDPOINTS 
#### GET http://127.0.0.1:8000/auto-complete/{nome-do-filme}
#### GET http://127.0.0.1:8000/movie/get-coming-soon
#### GET http://127.0.0.1:8000/movie/get-images/{id}
#### GET http://127.0.0.1:8000/movie/detail/{id}
#### GET http://127.0.0.1:8000/movie/get-genres/{id}