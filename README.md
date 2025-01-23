# Flask Todo Application

A simple, elegant todo list application built with Flask and SQLite.

## Features

- Create, read, update, and delete todo items
- Mark tasks as complete/incomplete
- Clean and responsive user interface
- SQLite database for data persistence

## Requirements

- Python 3.7+
- Flask
- SQLite3

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/a-todo-app-using-flask.git
cd a-todo-app-using-flask
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
flask init-db
```

5. Run the application:
```bash
flask run
```

The application will be available at `http://localhost:5000`

## Project Structure

```
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
├── instance/
├── static/
├── requirements.txt
└── README.md
```

## License

MIT License

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request