# Digital Stream

**Digital Stream** is a terminal-based screensaver inspired by the visuals of the _Matrix_ movie. It creates a mesmerizing flow of binary digits (`0` and `1`) that scroll down your terminal screen, simulating a "digital rain" effect.

---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Minimalistic and artistic design.
- Fully customizable stream settings:
  - Length and density of the streams.
  - Characters displayed in the stream.
  - Frame delay for speed adjustment.
- Compatible with most terminal environments.

---

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/digital-stream.git
   cd digital-stream
   ```

2. Ensure you have Python 3.7 or newer installed on your system.

3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the screensaver using the main script:
```bash
python main.py
```

Press `Ctrl+C` to exit the screensaver.

---

## Configuration

You can customize the behavior of the digital stream by modifying the settings in the `config.py` file:

- `MIN_STREAM_LENGTH`: Minimum length of a single stream.
- `MAX_STREAM_LENGTH`: Maximum length of a single stream.
- `PAUSE`: Pause duration (in seconds) between frames.
- `STREAM_CHARS`: Characters used in the stream (default is `['0', '1']`).
- `DENSITY`: Probability of starting a new stream in each column (range `0.0` to `1.0`).

---

## Project Structure

```
digital_stream/
│
├── main.py               # Main entry point of the application
├── config.py             # Configuration settings
├── stream.py             # Core logic for rendering the digital stream
├── tests/                # Unit tests for the project
│   ├── test_config.py    # Tests for config module
│   ├── test_stream.py    # Tests for stream module
│   └── __init__.py       # Marks the directory as a package
├── requirements-dev.txt   # Project dependencies   
└── requirements.txt      
```

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. Fork this repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push them to your fork:
   ```bash
   git add .
   git commit -m "Description of your changes"
   git push origin feature-name
   ```
4. Submit a pull request to the `main` branch of this repository.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### Acknowledgments

- Inspired by "The Matrix" visuals.
- Based on a project from the book _Big Book of Small Python Projects_ by Al Sweigart.
