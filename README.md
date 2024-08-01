# YouTube-PeakWatch
Youtube PeakWatch is a Python-based project designed to streamline the process of analyzing and tracking the most popular content from your favorite YouTube channels. Utilizing the YouTube API, the project fetches data from your top 5 favorite channels to identify their most viewed videos

The core functionality of Youtube PeakWatch includes:

Data Aggregation: Collects and aggregates the view count data of videos from the specified YouTube channels.
Report Generation: Processes the aggregated data to generate a comprehensive report, highlighting the top 5 most viewed videos across the selected channels.
Email Delivery: Automatically sends the final report, including the top 5 most viewed videos, directly to your email for easy access and review.
By leveraging Python and the YouTube API, Youtube PeakWatch simplifies the tracking of popular content, ensuring that you stay updated with the latest trends and most engaging videos from your favorite channels

## Project Structure

- `src/`: Contains the source code.
  - `main.py`: Main script to execute the project.
  - `youtube_api_corey.py`: Contains functions for YouTube API interactions and data processing.
- `data/`: Directory for storing output files.
  - `YoutubeVideoResults.csv`: The CSV file with the fetched video data.
- `.gitignore`: Specifies files and directories to ignore in version control.
- `requirements.txt`: Lists the required Python packages.
- `README.md`: Project documentation.

## Getting Started

### Prerequisites

- Python 3.x
- An active YouTube API key
- A Google email account for sending emails

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/kanishkdave/youtube_peakwatch.git
   cd youtube_peakwatch
