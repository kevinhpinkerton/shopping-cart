# shopping-cart

## Prerequisites

  + Anaconda 3.8+
  + Python 3.8+
  + Pip

## Installation

Fork this [remote repository](https://github.com/kevinhpinkerton/shopping-cart) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd shopping-cart
```

Use Anaconda to create and activate a new virtual environment, perhaps called "shopping-env":

```sh
conda create -n shopping-env python=3.8
conda activate shopping-env
```

From inside your virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

Go [here](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/gspread.md) to get started with the Google Sheets API. 

> NOTE: The Google credentials .json file will need to be named "google-credentials.json" and placed in the root directory to access the spreadsheet.

Go [here](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md) to get started with the SendGrid API. 

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file with the following:

    TAX_RATE = .0875
    GOOGLE_SHEET_ID = "1ItN7Cc2Yn4K90cMIsxi2P045Gzw0y2JHB_EkV4mXXpI"
    SHEET_NAME = "products"
    SENDGRID_API_KEY = "[Your key here]"
    MY_EMAIL_ADDRESS = "[Your email here]"
 
 ## Usage

Run the script:

```py
python shopping_cart.py
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment