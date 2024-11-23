from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

IMDB_API_URL = "https://imdb-com.p.rapidapi.com"
headers = {
    "x-rapidapi-key": "00880af35emsha9c34201bce0fccp1eeb25jsn3a2405fd63bc",
    "x-rapidapi-host": "imdb-com.p.rapidapi.com"
}

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API do IMDb"}

@app.get("/auto-complete/{title}")
def search_movie(title: str):
    try:
        querystring = {"query":title}
        response = requests.get(IMDB_API_URL+"/auto-complete", headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if data.get("errorMessage"):
            raise HTTPException(status_code=400, detail=data["errorMessage"])

        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/movie/get-coming-soon")
def search_movie():
    try:
        querystring = {"comingSoonType":"MOVIE"}
        response = requests.get(IMDB_API_URL+"/title/get-coming-soon", headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if data.get("errorMessage"):
            raise HTTPException(status_code=400, detail=data["errorMessage"])

        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/movie/get-images/{id}")
def search_movie(id: str):
    try:
        querystring = {"tconst":id}
        response = requests.get(IMDB_API_URL+"/title/get-images", headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if data.get("errorMessage"):
            raise HTTPException(status_code=400, detail=data["errorMessage"])

        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/movie/detail/{id}")
def search_movie(id: str):
    try:
        querystring = {"tconst":id}
        response = requests.get(IMDB_API_URL+"/title/get-extend-details", headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if data.get("errorMessage"):
            raise HTTPException(status_code=400, detail=data["errorMessage"])

        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/movie/get-genres/{id}")
def search_movie(id: str):
    try:
        querystring = {"tconst":id}
        response = requests.get(IMDB_API_URL+"/title/get-genres", headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        if data.get("errorMessage"):
            raise HTTPException(status_code=400, detail=data["errorMessage"])

        return data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

