# Spotify Search
<p>
    <a href="https://choosealicense.com/licenses/mit/" target="_blank">
        <img src="https://img.shields.io/github/license/matcsantos/SpotifySearch" alt="LICENSE">
    </a>
    <a href="https://pypi.org/project/spotifysearch/" target="_blank">
        <img src="https://img.shields.io/pypi/v/spotifysearch?color=33BBFF&label=PIP" alt="PIP">
    </a>
</p>

SpotifySearch is a complete wrapper for the Search API provided by Spotify written in Python.

It has built-in classes that helps you access the data returned by Spotify, alongside with useful methods for exporting data.

Check the [documentation](https://readthedocs.org/) for more information on classes and methods.

## What you can do
- Get Spotify catalog information about albums, artists or tracks that match a keyword string.
- Easily access the information provided by Spotify using specific class attributes and methods, such as **name**, **id**, **url** and many more.
- Access and export audio and image files, such as album covers for example.

## Installation
SpotifySearch depends on **[requests](https://pypi.org/project/requests/)**. You can easily install it by using **PIP**
```bash
python -m pip install requests
```

Then, you can safely install SpotifySearch using the following command:
```bash
python -m pip install spotifysearch
```

## Testing your installation
You can test your installation using python interactive shell
```python
>>> import spotifysearch
```

## Getting access to the API
To get access to Spotify Search API, you need to have a Spotify account to get an access token, which is required by the API itself. <br>
You can [register an account](https://www.spotify.com/signup/) if you don't have one.

Then, you need to login into your account in [Spotify for Developers](https://developer.spotify.com/dashboard/login).
Once you have successfully logged in, go to your **Dashboard**, and create a new application.

You should see something like this: <br>
<p align="center"><img src="https://i.imgur.com/fWLbWUH.png"></p>

Once you've created your application, you'll receive a **client ID** and a **client secret**. These are your credentials, you should store them in a **safe environment**.

**IMPORTANT: You should not store your credentials inside of your code if you're planning to publish it. You should use Environment Variables instead. Check [this section](https://github.com/matcsantos/SpotifySearch#keeping-your-credentials-safe) to learn how to keep your credentials safe.**

## Making your first call
So now that you have your **credentials**, you can start making your calls to the API. 

Open your editor and run the following code:

```python
# First, we import our Client class from spotifysearch.client
from spotifysearch.client import Client

# Then, we create an instance of that class passing our credentials as arguments.
# IMPORTANT: Don't put your credentials inside your code if your planning to publish it.
myclient = Client("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")

# Now we can call the method search() from our client and store the results in a new object.
results = myclient.search("Never gonna give you up")

# Then we call the method get_tracks() from our results object, which returns a list of tracks.
tracks = results.get_tracks()

# Now, let's access the first track in our list by using index 0.
track = tracks[0]

# Finally, we can access some information contained in our track.
print(track.name, "-", track.artists[0].name)
print(track.url)

```

**This should be your result:**
```bash
Never Gonna Give You Up - Rick Astley
https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT
```
<br>

That seems to be a lot of code, but you can simplify it a lot, like so:
```python
from spotifysearch.client import Client

myclient = Client("YOUR_CLIENT_ID", "YOUR_CLIENT_SECRET")
track = myclient.search("Never gonna give you up").get_tracks()[0]

print(track.name, "-", track.artists[0].name)

```
In a few lines of code, we got access to the API, retrieved some useful information of the first track in our results and displayed it.

There are a lot of class attributes and methods that you can use to retrieve the information you need, you can check them out in the [documentation](https://readthedocs.org/).

## Keeping your credentials safe
As mentioned before, you should not store your credentials inside of your code. Specially if you are planning to publish it.

A safer way to store them is by using Environment Variables.
Here's a complete [tutorial](https://www.twilio.com/blog/environment-variables-python) on how to define and access environment variables using Python.

## License
This project is under the terms of the [MIT license](https://opensource.org/licenses/MIT).
