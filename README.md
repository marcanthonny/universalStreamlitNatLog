# Streamlit Application

This is a simple Streamlit application that demonstrates the use of multiple pages and utility functions. 

## Project Structure

```
streamlit-app
├── src
│   ├── app.py          # Main entry point of the Streamlit application
│   ├── pages
│   │   └── page2.py    # Second page of the Streamlit application
│   └── utils
│       └── helpers.py   # Utility functions for the application
├── data
│   └── sample_data.csv  # Sample data for demonstration
├── requirements.txt      # Python dependencies
├── .gitignore            # Files to ignore in Git
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd streamlit-app
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command:
```
streamlit run src/app.py
```

## Usage

- Navigate through the application using the sidebar to access different pages.
- The main page is defined in `src/app.py`, and additional functionality can be found in `src/pages/page2.py`.
- Utility functions can be found in `src/utils/helpers.py` for data processing and visualization.

## Contributing

Feel free to submit issues or pull requests for improvements or additional features. 

## License

This project is licensed under the MIT License.