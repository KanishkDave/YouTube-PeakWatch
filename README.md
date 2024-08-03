# YouTube-PeakWatch
Youtube PeakWatch is a Python-based project designed to streamline the process of analyzing and tracking the most popular content from your favorite YouTube channels. Utilizing the YouTube API, the project fetches data from your top 5 favorite channels to identify their most viewed videos

The core functionality of Youtube PeakWatch includes:

Data Aggregation: Collects and aggregates the view count data of videos from the specified YouTube channels.
Report Generation: Processes the aggregated data to generate a comprehensive report, highlighting the top 5 most viewed videos across the selected channels.
Email Delivery: Automatically sends the final report, including the top 5 most viewed videos, directly to your email for easy access and review.
By leveraging Python and the YouTube API, Youtube PeakWatch simplifies the tracking of popular content, ensuring that you stay updated with the latest trends and most engaging videos from your favorite channels.

## Features

- Fetches video details from specified YouTube channels.
- Analyzes video statistics to identify top videos and most-watched videos from each channel.
- Sends an email with the top videos and most-watched videos.
- Results are saved in a CSV file.

## Project Structure

- `src/`: Contains the source code.
  - `main.py`: Main script to execute the project.
  - `youtube_api_call.py`: Contains functions to interact with the YouTube Data API.
- `data/`: Directory for storing output files.
  - `YoutubeVideoResults.csv`: The CSV file with the fetched video data.
- `.gitignore`: Specifies files and directories to ignore in version control.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Project documentation.

## Requirements

List of Python packages required for the project:

- `pandas`
- `smtplib` (standard library)
- `ssl` (standard library)
- `email` (standard library)
- `google-api-python-client`

## Getting Started

    Create a virtual environment and install the required packages:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Create a `.env` file in the root of the project with the following content:

    ```env
    EMAIL_ID=your-email@example.com
    EMAIL_PASS=your-email-password
    ```

4. **Configure the YouTube API:**

    Replace the placeholder API key in the `youtube_api_call.py` file with your own YouTube Data API key.

5. **Run the project:**

    Execute the main script:

    ```sh
    python src/main.py
    ```

## Acknowledgments

- [YouTube Data API v3 Documentation](https://developers.google.com/youtube/v3)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Documentation](https://docs.python.org/3/)
