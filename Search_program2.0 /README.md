# Custom Search Browser

A Python application that uses Google Custom Search API to perform web searches and display the results in a graphical interface. Built with PyQt5, it allows users to view search results, click on them, and display the corresponding web page directly within the application.

## Features

- **Google Search Integration**: Uses Google Custom Search API to fetch search results.
- **Search Results Display**: Displays search results with titles and snippets in a user-friendly list.
- **Embedded Browser**: Opens web pages in a built-in browser window using `QWebEngineView`.
- **Interactive UI**: Modern graphical interface with clickable results.

## Technologies Used

- **Python**: Core programming language.
- **Google Custom Search API**: For fetching search results.
- **PyQt5**: For creating the graphical user interface.
- **QWebEngineView**: For displaying web pages within the app.

## Prerequisites

1. **Python 3.6+**
2. **Google API Key and CSE ID**
   - Create a [Google Custom Search Engine (CSE)](https://cse.google.com/cse/) and get your CSE ID.
   - Obtain an API key from the [Google Cloud Console](https://console.cloud.google.com/).
3. Install required dependencies:
   ```bash
   pip install google-api-python-client PyQt5 PyQtWebEngine

Installation

	1.	Clone the repository:

git clone https://github.com/yourusername/custom-search-browser.git


	2.	Navigate to the project directory:

cd custom-search-browser


	3.	Replace the API_KEY and CSE_ID in the script with your credentials.

Usage

	1.	Run the script:

python app.py


	2.	Enter a search term in the search bar and click “Search”.
	3.	View the search results displayed in the left panel.
	4.	Click on a result to load the corresponding web page in the right panel.

File Structure

custom-search-browser/
├── app.py        # Main application file
└── README.md     # Project documentation

Screenshots

Main Interface

Search Results

Future Improvements

	•	Add error handling for API failures and network issues.
	•	Include pagination for search results.
	•	Provide support for multiple languages in search queries.

Contributing

Contributions are welcome! Fork the repository, create a branch, and submit a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Author: Radoslav Dimitrov Petkov
Email: radigoig@gmail.com
