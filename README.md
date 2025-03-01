# Work Harder

A tool that records human computer interactions and plays them back to simulate realistic user activity.

## Overview

Work Faker consists of two main components:

1. A **recorder** built with Svelte that captures mouse movements, clicks, and keyboard activity
2. A **replayer** written in Python that recreates the recorded user behavior

This tool can be useful for:

- Testing user interfaces with realistic interaction patterns
- Creating demos that show natural user workflows
- Automating repetitive tasks while maintaining human-like behavior
- Amusing your coworkers (use responsibly!)

## How It Works

### Recording User Interactions

The Svelte application records:

- Mouse movements (x, y coordinates)
- Mouse clicks
- Keyboard activity
- Timing of all interactions

Data is timestamped and stored as a JSON array, which can be copied to the clipboard with the "PRINT" button.

### Processing the Data

The Node.js script (`scripts/processData.js`) converts the raw JSON data into a more optimized format:

```javascript
// Before: [{t: 123, x: 456, y: 789, p: false}, ...]
// After: {123: {x: 456, y: 789, p: false}, ...}
```

### Replaying User Behavior

The Python script (`scripts/replayActions.py`) uses pyautogui to recreate the recorded interactions:

- Moves the mouse to recorded coordinates
- Simulates clicks
- Types text from a sample document
- Adds realistic variations like occasional typos and corrections

## Installation

### Prerequisites

- Node.js (for data processing)
- Python 3.x (for replay functionality)
- Required Python packages:
  ```
  pip install pyautogui keyboard
  ```

### Setup

1. Clone this repository
2. Install dependencies:
   ```
   npm install
   ```

## Usage

### Recording

1. Run the Svelte application
   ```
   npm run dev
   ```
2. Interact with your computer as you normally would
3. Click the "PRINT" button to copy the recorded data to your clipboard
4. Save the clipboard contents to a file named `data.json`

### Processing

Run the Node.js script to optimize the data format:

```
node scripts/processData.js
```

This creates a `formatted.json` file.

### Replaying

1. Prepare a `sampleDocument.txt` file with text content to be typed
2. Run the Python script:
   ```
   python scripts/replayActions.py
   ```
3. Switch to the application window where you want the interactions to be simulated
4. The script will begin replaying your actions after a 5-second delay

## Safety Features

- Move your mouse to the upper-left corner of the screen to abort the replay
- The replay will automatically stop after completing all actions

## Customization

You can modify the Python script to:

- Adjust timing and speed of interactions
- Change the probability of simulated typos
- Customize the text being typed

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
