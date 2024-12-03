Modern Search Engine - Python GUI Application

This is a simple yet functional GUI-based search engine application built using Python’s tkinter library. It allows users to perform web searches and displays the results with titles, URLs, and descriptions, similar to popular search engines. The application includes pagination to navigate between pages of results.

Features

	•	Search Functionality: Enter a query to search the web.
	•	Results Display: Shows titles, URLs, and descriptions of search results.
	•	Clickable Links: Titles and URLs are clickable and open in the default web browser.
	•	Pagination: Navigate between pages of results using Next and Previous buttons.
	•	Responsive UI: Scrollable results area with a modern and clean interface.

Prerequisites

	•	Python 3.x: Ensure you have Python 3 installed on your system.
	•	Required Python Libraries:
	•	tkinter (usually comes with Python installations)
	•	requests
	•	beautifulsoup4
	•	googlesearch-python (also known as googlesearch)

Installation

	1.	Clone the Repository (if applicable) or Download the Script:

git clone https://github.com/yourusername/modern-search-engine.git
cd modern-search-engine


	2.	Create a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate


	3.	Install Required Libraries:

pip install requests beautifulsoup4 googlesearch-python

	•	If you encounter any issues with googlesearch-python, you can install it using:

pip install git+https://github.com/MarioVilas/googlesearch.git



Usage

	1.	Run the Application:

python search_engine.py


	2.	Using the Search Engine:
	•	Enter a Query: Type your search term into the search bar at the top of the window.
	•	Perform Search: Press Enter or click the Search button.
	•	View Results:
	•	Results will display with the title, URL, and description.
	•	Titles and URLs are clickable and will open in your default web browser.
	•	Navigate Pages:
	•	Use the Next and Previous buttons at the bottom to navigate between pages.
	•	Each page displays up to 10 results.
	•	The application fetches up to 20 results in total.
	3.	Exiting the Application:
	•	Close the window or press Ctrl+C in the terminal if running from the command line.

Code Overview

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from googlesearch import search
import requests
from bs4 import BeautifulSoup

	•	Imports:
	•	tkinter: For GUI components.
	•	webbrowser: To open links in the default browser.
	•	googlesearch: To perform web searches.
	•	requests and BeautifulSoup: To fetch and parse webpage content.

Functions

	•	get_title_description(url):
	•	Fetches the title and meta description from a given URL.
	•	Returns a tuple (title, description).
	•	perform_search(*args):
	•	Triggered when a search is performed.
	•	Retrieves search results and stores them.
	•	Calls display_results(current_page) to show the first page.
	•	display_results(page_number):
	•	Displays results for the specified page.
	•	Updates pagination buttons.
	•	update_pagination_buttons():
	•	Enables or disables pagination buttons based on the current page.
	•	next_page() and prev_page():
	•	Handle navigation between pages.

GUI Components

	•	Main Window:
	•	Size: 500x500 pixels.
	•	Title: "Modern Search Engine".
	•	Header Frame:
	•	Contains the search entry and search button.
	•	Results Frame:
	•	Scrollable area where search results are displayed.
	•	Each result shows the title, URL, and description.
	•	Pagination Frame:
	•	Contains Previous and Next buttons to navigate between pages.
	•	Footer Frame:
	•	Displays a simple footer with the application name and year.

Styles

	•	Utilizes ttk.Style for modern widget styling.
	•	Hover Effects:
	•	Titles and URLs change color when hovered over to indicate interactivity.

Dependencies

Ensure all the required libraries are installed:

pip install requests beautifulsoup4 googlesearch-python

If you face issues with googlesearch-python, consider using an alternative installation method:

pip install git+https://github.com/MarioVilas/googlesearch.git

Troubleshooting

	•	No Search Results:
	•	Ensure you have an active internet connection.
	•	Check for any typos in your search query.
	•	Application Freezes:
	•	Fetching webpage titles and descriptions may take time.
	•	Be patient or consider reducing the number of results.
	•	Import Errors:
	•	Verify that all required libraries are installed.
	•	Use pip list to check installed packages.

Potential Enhancements

	•	Asynchronous Requests:
	•	Implement threading or asynchronous I/O to improve performance.
	•	Error Handling:
	•	Enhance error messages for network issues or invalid URLs.
	•	Customizable Results Per Page:
	•	Allow users to select how many results to display per page.
	•	Search History:
	•	Implement a feature to track and display previous searches.
	•	GUI Improvements:
	•	Add icons, improve styling, or include themes for a better user experience.

Legal and Ethical Considerations

	•	Respect Website Policies:
	•	Be mindful of websites’ robots.txt files and terms of service.
	•	Avoid making excessive requests to a single website.
	•	Usage Limits:
	•	The googlesearch library may have usage limits or may be subject to changes in Google’s search policies.

Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

License

This project is licensed under the MIT License.

Contact

For questions or suggestions, please contact your.email@example.com.

Acknowledgments

	•	Python Software Foundation: For providing Python.
	•	Third-party Libraries: requests, beautifulsoup4, googlesearch-python.

Disclaimer

This application is for educational purposes. The developer is not responsible for any misuse or violations of service terms resulting from the use of this application.
