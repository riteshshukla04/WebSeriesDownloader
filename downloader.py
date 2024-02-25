
import os
def downloadFile(name,seasonName,url):
    import requests

    url = f'https://archive.org{url}'
    destination = f'{seasonName}\{name}'
    if not os.path.exists(seasonName):
      # If not, create the folder
      os.makedirs(seasonName)
      print(f"Folder '{seasonName}' created successfully.")
    if os.path.exists(destination):
      print(f"The file exists in the directory---{destination}")
      return
    response = requests.get(url)
    print(f"Downloading---{destination}")
    with open(destination, 'wb') as file:
        file.write(response.content)

    print(f"File downloaded and saved as {destination}")
