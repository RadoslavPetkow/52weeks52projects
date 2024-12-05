import sys
from googleapiclient.discovery import build
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem, QLabel
)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

# Replace these with your valid API key and CSE ID
API_KEY = 'YOUR_API_KEY'
CSE_ID = 'YOUR_CSE_ID'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    result = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return result.get('items', [])


class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Search Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Main container widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Layouts
        main_layout = QVBoxLayout(main_widget)
        top_layout = QHBoxLayout()
        main_layout.addLayout(top_layout)

        # Search bar
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter search term...")
        top_layout.addWidget(self.search_bar)

        # Search button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.perform_search)
        top_layout.addWidget(self.search_button)

        # Layout to hold results and browser
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)

        # Results list
        self.results_list = QListWidget()
        self.results_list.itemClicked.connect(self.load_selected_result)
        content_layout.addWidget(self.results_list, 30)  # 30% width

        # Web view
        self.browser = QWebEngineView()
        content_layout.addWidget(self.browser, 70)  # 70% width

        # Store results
        self.search_results = []

    def perform_search(self):
        query = self.search_bar.text().strip()
        if not query:
            return  # do nothing if no query

        self.results_list.clear()
        self.search_results = google_search(query, API_KEY, CSE_ID)

        if not self.search_results:
            # Show a message when no results are found
            no_result_item = QListWidgetItem("No results found.")
            no_result_item.setFlags(no_result_item.flags() & ~Qt.ItemIsSelectable)
            self.results_list.addItem(no_result_item)
            return

        # Display the top results
        for item in self.search_results:
            title = item.get('title', 'No Title')
            snippet = item.get('snippet', '')
            display_text = f"{title}\n{snippet}"
            list_item = QListWidgetItem(display_text)
            list_item.setData(Qt.UserRole, item)  # store the entire item
            self.results_list.addItem(list_item)

    def load_selected_result(self, item):
        data = item.data(Qt.UserRole)
        if data:
            url = data.get('link', '')
            if url:
                self.browser.setUrl(QUrl(url))


def main():
    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
