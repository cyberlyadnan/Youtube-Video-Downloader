<h1>YouTube Downloader</h1>

    <h2>Description</h2>
    <p>The YouTube Downloader is a Python script that allows users to download videos and audios from YouTube by providing the URL. It uses the <code>pytube</code> library to fetch and download the content. The GUI (Graphical User Interface) is built using the <code>tkinter</code> library and customized with the <code>customtkinter</code> module for appearance and UI scaling adjustments.</p>

    <h2>Features</h2>
    <ul>
        <li>Download YouTube videos in various resolutions.</li>
        <li>Download YouTube videos as audio files.</li>
        <li>Download YouTube video thumbnails.</li>
        <li>Customize appearance mode (Light, Dark, System).</li>
        <li>Adjust UI scaling for better accessibility.</li>
    </ul>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>pytube</code> library</li>
        <li><code>Pillow</code> library (for image handling)</li>
        <li><code>webbrowser</code> module (built-in)</li>
        <li><code>tkinter</code> library (built-in)</li>
        <li><code>customtkinter</code> module (customized tkinter appearance)</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:</li>
        <pre><code>git clone https://github.com/username/YouTube-Downloader.git</code></pre>
        <li>Install the required dependencies:</li>
        <pre><code>pip install pytube Pillow</code></pre>
        <li>Run the script:</li>
        <pre><code>python main.py</code></pre>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Launch the application.</li>
        <li>Enter the YouTube video URL in the provided input field.</li>
        <li>Choose the desired download option (Thumbnail, Video, Audio) using the segmented button.</li>
        <li>Click the "Go" button to fetch video details and available resolutions.</li>
        <li>Select the desired resolution or format from the dropdown menu.</li>
        <li>Click the "Download" button to start downloading the content.</li>
        <li>Choose the destination folder to save the downloaded file.</li>
    </ol>

    <h2>Customization</h2>
    <ul>
        <li>Appearance Mode: Choose between Light, Dark, or System appearance modes to match your preference.</li>
        <li>UI Scaling: Adjust the UI scaling for better readability and accessibility.</li>
    </ul>
