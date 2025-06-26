import requests
import os


def get_movie_titles():
    name = input("Enter movie, series name : ")
    return name


def save_to_csv(data_list, filename):
    with open(filename, "a", newline='') as f:
        f.write(f"{data_list}")


def fetch_movie_data(movie_name):
    base_url = "http://www.omdbapi.com/"
    params = {
    "t": movie_name,
    "apikey": "f8f01e5f"
    }
    response = requests.get(url=base_url, params=params)
    print(response)
    data = response.text
    return data





def main():
    n = int(input("Enter number how many series and movies information wants : "))
    movie_list = []
    filename = input("Enter your file name with .csv extention : ")
    for i in range(n):
        name = get_movie_titles()
        movie_list.append(name)
    for title in movie_list:
        data_list = fetch_movie_data(title)
        save_to_csv(data_list, filename)
    


if __name__ == "__main__":
    main()
