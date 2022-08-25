# Entry point for the application.
from views import app
import views    # For application discovery by the 'flask' command.

if __name__ == "__main__":
        app.run()
