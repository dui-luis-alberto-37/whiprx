# WhisprX

This is a [Wagtail](https://wagtail.org) poject, intended to post in X using audios and transciptingthem to text to be published.

You can access to this project with https://whisprx.licc.dev for testing, or https://whisprx.licc.unam.mx for production.

## Getting Started

1. **Check that you have an appropriate version of Python 3** You want to make sure that you have a [compatible version](https://docs.wagtail.org/en/stable/releases/upgrading.html#compatible-django-python-versions) installed:

   ```sh
   python --version
   # Or:
   python3 --version
   # **On Windows** (cmd.exe, with the Python Launcher for Windows):
   py --version
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate your project dependencies. These instructions are for GNU/Linux or MacOS, but there are [other operating systems in the Wagtail docs](https://docs.wagtail.org/en/stable/getting_started/tutorial.html#create-and-activate-a-virtual-environment).

   ```bash
   mkdir whisprx
   mkdir venv
   python -m venv venv/whisprx_env
   source venv/whisprx_env/bin/activate
   ```

3. **Navigate to Project Directory**: Move into the newly created project directory.

   ```bash
   cd whisprx
   ```

4. **Install Wagtail**: Install the Wagtail CMS package using pip.

   ```bash
   pip install wagtail
   ```

5. **Initialize Project**: Use the `git clone` command to clone the project based on the Wagtail Starter Kit template.

   ```bash
   git clone git@github.com:dui-luis-alberto-37/whiprx.git
   ```
   or
   ```bash
   git clone https://github.com/dui-luis-alberto-37/whiprx.git
   ```

7. **Install Project Dependencies**: Install the project's dependencies into a virtual environment.

   ```bash
   pip install -r requirements.txt
   ```

All commands from now on should be run from inside the virtual environment.

8. **Load Dummy Data**: Load in some dummy data to populate the site with some content.

   ```bash
   make load-data
   ```

9. **Start the Server**: Start the Django development server.

   ```bash
   make start
   ```

10. **Access the Site and Admin**: Once the server is running, you can view the site at `localhost:8000` and access the Wagtail admin interface at `localhost:8000/admin`. Log in with the default credentials provided by :

    - Username: admin
    - Password: password

### Deploying

Once you have your own copy of the project, you can extend and configure it however you like.


Make sure to test any changes by reviewing them.
