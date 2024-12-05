Here’s a README.md for your project:

# Modern Search Engine

A simple yet modern search engine application built using Python and `Tkinter`. It allows users to search for web content, displays search results with titles, descriptions, and URLs, and provides a user-friendly interface for navigating search results. Users can also view web pages directly within the application.

## Features

- Perform web searches and fetch up to 20 results.
- Display results with titles, descriptions, and URLs.
- Pagination support for navigating search results.
- Clickable links to open web pages directly in the application.
- "Back to Search Results" button to return to the results page.
- Modern and responsive UI with hover effects.

## Technologies Used

- **Python**: Main programming language.
- **Tkinter**: For the GUI design.
- **BeautifulSoup**: To scrape metadata (title and description) from web pages.
- **Requests**: For making HTTP requests.
- **Googlesearch-Python**: To perform Google searches.
- **TkinterWeb**: For displaying web pages inside the app.

## Prerequisites

- Python 3.6 or higher
- The following Python packages:
  - `tkinter`
  - `requests`
  - `bs4`
  - `googlesearch-python`
  - `tkinterweb`

Install the dependencies using:
```bash
pip install requests beautifulsoup4 googlesearch-python tkinterweb

Installation

	1.	Clone the repository:

git clone https://github.com/yourusername/modern-search-engine.git


	2.	Navigate to the project directory:

cd modern-search-engine


	3.	Run the script:

python app.py



Usage

	1.	Launch the application.
	2.	Enter your search query in the search bar and press “Enter” or click the “Search” button.
	3.	View the search results with titles, URLs, and descriptions.
	4.	Click on a title or URL to open the webpage within the app.
	5.	Use the “Previous” and “Next” buttons to navigate through search result pages.

Screenshots

Search Page with results

Web Page view inside the application

Future Improvements

	•	Add more search engine options.
	•	Support for additional languages.
	•	Enhanced error handling and UI improvements.

Contributing

Contributions are welcome! Feel free to fork this repository, create a new branch, and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author: Radoslav Dimitrov Petkov
Email: radigoig@gmail.com
