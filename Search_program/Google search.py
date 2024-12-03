import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from googlesearch import search
import requests
from bs4 import BeautifulSoup

# Global variables to store search results and current page
search_results = []
current_page = 1
results_per_page = 10

# Function to fetch title and description from a URL
def get_title_description(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get the title
        title = soup.title.string.strip() if soup.title else 'No Title'

        # Get the meta description
        description_tag = soup.find('meta', attrs={'name': 'description'})
        if not description_tag:
            description_tag = soup.find('meta', attrs={'name': 'Description'})
        description = description_tag['content'].strip() if description_tag else 'No Description'

        return title, description
    except Exception:
        return 'No Title', 'No Description'

# Function to perform the search and store results
def perform_search(*args):
    global search_results
    global current_page
    query = search_entry.get()
    if not query.strip():
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return

    try:
        # Clear previous results
        for widget in results_frame.winfo_children():
            widget.destroy()

        # Reset current page and search results
        current_page = 1
        search_results = []

        # Perform search and get up to 20 results
        for idx, url in enumerate(search(query, num_results=20)):
            title, description = get_title_description(url)
            search_results.append({'title': title, 'url': url, 'description': description})

        # Display the first page
        display_results(current_page)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display results for the given page
def display_results(page_number):
    # Clear previous results
    for widget in results_frame.winfo_children():
        widget.destroy()

    start_idx = (page_number - 1) * results_per_page
    end_idx = start_idx + results_per_page
    page_results = search_results[start_idx:end_idx]

    for result in page_results:
        title = result['title']
        url = result['url']
        description = result['description']

        # Result Frame
        result_item = ttk.Frame(results_frame, padding=(5, 5))
        result_item.pack(fill=tk.X, pady=3)

        # Title Label
        title_label = ttk.Label(
            result_item,
            text=title,
            style="Title.TLabel",
            cursor="hand2",
            wraplength=400,
            anchor="w"
        )
        title_label.pack(fill=tk.X)
        title_label.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
        title_label.bind("<Enter>", lambda e: e.widget.configure(style="HoverTitle.TLabel"))
        title_label.bind("<Leave>", lambda e: e.widget.configure(style="Title.TLabel"))

        # URL Label
        url_label = ttk.Label(
            result_item,
            text=url,
            style="Url.TLabel",
            cursor="hand2",
            wraplength=400,
            anchor="w"
        )
        url_label.pack(fill=tk.X)
        url_label.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
        url_label.bind("<Enter>", lambda e: e.widget.configure(style="HoverUrl.TLabel"))
        url_label.bind("<Leave>", lambda e: e.widget.configure(style="Url.TLabel"))

        # Description Label
        desc_label = ttk.Label(
            result_item,
            text=description,
            style="Description.TLabel",
            wraplength=400,
            anchor="w"
        )
        desc_label.pack(fill=tk.X, pady=(3, 0))

    # Update pagination controls
    update_pagination_buttons()

# Function to update the state of pagination buttons
def update_pagination_buttons():
    total_pages = (len(search_results) + results_per_page - 1) // results_per_page

    if current_page <= 1:
        prev_button.config(state=tk.DISABLED)
    else:
        prev_button.config(state=tk.NORMAL)

    if current_page >= total_pages:
        next_button.config(state=tk.DISABLED)
    else:
        next_button.config(state=tk.NORMAL)

# Functions for pagination buttons
def next_page():
    global current_page
    current_page += 1
    display_results(current_page)

def prev_page():
    global current_page
    current_page -= 1
    display_results(current_page)

# Create the main application window
app = tk.Tk()
app.title("Modern Search Engine")
app.geometry("500x500")
app.configure(bg="#f0f0f0")

# Styles
style = ttk.Style()
style.theme_use("default")
style.configure("TButton", font=("Arial", 10))
style.configure("TEntry", font=("Arial", 10))
style.configure("Title.TLabel", foreground="#1a0dab", font=("Arial", 11, "bold"), background="#ffffff")
style.configure("HoverTitle.TLabel", foreground="#d14836", font=("Arial", 11, "bold"), background="#ffffff")
style.configure("Url.TLabel", foreground="#006621", font=("Arial", 9), background="#ffffff")
style.configure("HoverUrl.TLabel", foreground="#0b0080", font=("Arial", 9), background="#ffffff")
style.configure("Description.TLabel", foreground="#4d5156", font=("Arial", 10), background="#ffffff")
style.configure("TLabel", background="#f0f0f0")

# Header Frame
header_frame = ttk.Frame(app, padding=(5, 5))
header_frame.pack(fill=tk.X)

# Search Entry
search_entry = ttk.Entry(header_frame, font=("Arial", 10), width=35)
search_entry.pack(side=tk.LEFT, padx=(0, 5))
search_entry.bind("<Return>", perform_search)

# Search Button
search_button = ttk.Button(header_frame, text="Search", command=perform_search)
search_button.pack(side=tk.LEFT)

# Results Frame with Scrollbar
results_container = ttk.Frame(app)
results_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

canvas = tk.Canvas(results_container, bg="#ffffff")
scrollbar = ttk.Scrollbar(results_container, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

results_frame = scrollable_frame

# Pagination Controls
pagination_frame = ttk.Frame(app, padding=(5, 5))
pagination_frame.pack(fill=tk.X)

prev_button = ttk.Button(pagination_frame, text="Previous", command=prev_page)
prev_button.pack(side=tk.LEFT, padx=5)
prev_button.config(state=tk.DISABLED)

next_button = ttk.Button(pagination_frame, text="Next", command=next_page)
next_button.pack(side=tk.RIGHT, padx=5)
next_button.config(state=tk.DISABLED)

# Footer Frame
footer_frame = ttk.Frame(app, padding=(5, 5))
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
footer_label = ttk.Label(footer_frame, text="Modern Search Engine © 2023", font=("Arial", 8))
footer_label.pack()

# Run the application
app.mainloop()