# Youtube Videos Downloader
#### Video Demo:  https://youtu.be/BqO752L0kRA
#### Description:



# YouTube Video Downloader

## Description

The YouTube Video Downloader is a Python-based application designed to allow users to download YouTube videos in various resolutions and formats, including `144p`, `360p`, `720p`, `1080p`, and `mp3` audio. The downloader uses the `pytube` library for handling YouTube video streams and `Tkinter` for creating the graphical user interface (GUI).

The application is a simple, user-friendly solution for downloading videos without the need for complex setup or external dependencies like `ffmpeg`, although the app does provide instructions for users who wish to combine separate audio and video files for higher-quality downloads.

## Installation

To run this application, you'll need Python and the required libraries. Follow these steps to set up the project:

1. Clone or download this repository.
2. Ensure you have Python installed on your system.
3. Install the dependencies listed in the `requirements.txt` file using the following command:

    ```bash
    pip install -r requirements.txt
    ```

**Important Note:**

This project requires a specific version of `pytube` due to necessary modifications to the `cipher.py` file. The version available on GitHub may not work correctly with YouTube’s current setup. Follow the instructions below to ensure compatibility:


### Installation Instructions for Modified `pytube`

#### Option 1: Install Using the Included `.whl` File

1. **Uninstall any existing `pytube` version:**

    ```bash
    pip uninstall pytube
    ```

2. **Install the modified `pytube` `.whl` file included in this repository:**

    Locate the `.whl` file in the repository directory. The file is named `pytube-15.0.0-py3-none-any.whl`. Install it using the following command:

    ```bash
    pip install pytube-15.0.0-py3-none-any.whl
    ```

   This `.whl` file includes the necessary changes to `cipher.py`.

#### Option 2: Manually Modify `cipher.py` in `pytube`

1. **Uninstall any existing `pytube` version:**

    ```bash
    pip uninstall pytube
    ```

2. **Install the `pytube` package from PyPI:**

    ```bash
    pip install pytube
    ```

3. **Locate the `cipher.py` file:**

   Find the installed `pytube` package directory. This is usually located in the `site-packages` directory within your Python environment. The path is typically something like:
   ```
   <path_to_python>/lib/site-packages/pytube/cipher.py
   ```

4. **Edit the `cipher.py` file:**

   Open `cipher.py` in a text editor and locate the `get_throttling_function_name` function. Modify it as follows:

    ```python
    def get_throttling_function_name(js: str) -> str:
        """Extract the name of the function that computes the throttling parameter.

        :param str js:
            The contents of the base.js asset file.
        :rtype: str
        :returns:
            The name of the function used to compute the throttling parameter.
        """
        function_patterns = [
            # The following pattern is based on issues and commits related to YouTube's throttling functions
            r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
            r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
            r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
        ]
        logger.debug('Finding throttling function name')
    ```

5. **Save the file and exit the editor.**

---

## Project Files

This project consists of the following core files:

### 1. **main.py**:
This is the main application file containing all the logic for the YouTube downloader. It integrates the following functions and features:
- **Tkinter GUI**: The graphical interface allows users to paste a YouTube URL, select video resolution or audio format, and download the desired file.
- **Threading**: To ensure a smooth user experience, especially with larger downloads, the application uses a separate thread to perform the download operation, avoiding the UI freezing during the process.
- **Validation**: The `is_valid_youtube_url()` function ensures that the input URL is valid before attempting a download, reducing the likelihood of user error.
- **Multiple Resolutions**: The program detects available resolutions (144p, 360p, 720p, 1080p) and offers them to the user. It also provides the option to download audio as an MP3.
- **Download Management**: After the download is complete, the app provides feedback on the location of the downloaded files, with options to open the containing folder or the file itself.

### 2. **Icons**:
- `download.png`: The download button icon.
- `help.png`: The help button icon, which shows instructions on how to use the app.
- `credit.png`: The credits button icon, which shows acknowledgments.


## Design Decisions

### 1. **Minimal External Dependencies**:
One of the key decisions in this project was to avoid external dependencies like `ffmpeg` for video and audio merging. The reason behind this was to make the program easier to share and deploy. While `ffmpeg` is commonly used for merging audio and video streams, requiring users to install it separately would complicate the setup. However, for users who wish to combine the audio and video streams downloaded in 1080p resolution, the app provides clear instructions on how to do so using `ffmpeg` as an optional step.

### 2. **Threading for UI Responsiveness**:
I chose to implement threading for the download operation to prevent the UI from freezing during the download process. Since downloading a video can take time depending on the user's internet speed and file size, performing the download in a separate thread ensures that the user can still interact with the app and see progress updates in real time.

### 3. **Resolution and Format Flexibility**:
The app offers flexibility in terms of both video resolution and audio formats. Depending on the user's needs, they can choose a low resolution like 144p for quick downloads or higher resolutions like 1080p if they prefer quality. The MP3 option is ideal for users who are only interested in downloading audio.

### 4. **User Feedback**:
After each download, the user is provided with the exact path where the file is stored. This is crucial for ensuring that users can easily find the downloaded files. Additionally, when separate video and audio streams are downloaded (in 1080p resolution), the app informs the user that they will need to merge these files manually.

### 5. **GUI Design**:
Tkinter was chosen for the GUI because it is easy to set up and requires no additional installations for users running the program on most platforms. The interface is clean and simple, allowing users to input a link, choose a resolution, and begin the download process with minimal friction.

## How It Works

### Step 1: Input a YouTube Link
- Users are prompted to enter a valid YouTube video URL into the input box.

### Step 2: Choose a Format or Resolution
- Once the link is provided, the app displays buttons for available video resolutions and an option to download the audio as MP3. The available options are automatically fetched based on the YouTube video stream data.

### Step 3: Select Download Path
- Users can choose where the downloaded file will be stored by selecting a folder using the file dialog.

### Step 4: Download the File
- Clicking on a resolution button starts the download process. Users can monitor the progress, and once the download is complete, they can open the file directly from the app or navigate to the containing folder.

### Step 5: Merging Audio and Video (Optional for 1080p)
- If the user downloads a 1080p video, the app provides instructions on how to merge the separate video and audio files. An example `ffmpeg` command is also included for convenience.

## Challenges and Future Improvements

One of the challenges I faced during development was handling downloads for higher resolutions (1080p and above). YouTube streams these resolutions as separate video and audio files, which required additional logic to handle two separate downloads and notify the user about merging the files afterward.

In the future, I plan to incorporate optional built-in support for merging audio and video using `ffmpeg` (with an optional installation prompt). This will further streamline the user experience, making the app a more comprehensive solution for high-resolution downloads.

## Credits

- Developed by @medo_atif
- Special thanks to the `pytube` library for handling YouTube stream management: https://pytube.io
- This project was completed as part of CS50x, offered by Harvard University.
- A big thank you to David Malan for his exceptional teaching and guidance throughout the course.

---

