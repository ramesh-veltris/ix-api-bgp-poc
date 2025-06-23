# IX-API BGP PoC

## 🔧 Setup Instructions

1. **Clone the IX-API Sandbox**
   
   ```bash
   git clone https://gitlab.com/ix-api/ix-api-sandbox-v2
2. **Run the Sandbox**

  Follow the instructions under "Running the Sandbox" in the IX-API Sandbox README to start the API server(https://gitlab.com/ix-api/ix-api-sandbox-v2).
  
3. **Get API Key & Secret**
   
  After running the sandbox, obtain your API Key and API Secret.

4. **Set up .env file**

Copy the example file:

```bash
cp .env.example .env
```
Open .env and add your API Key and Secret:
```bash
API_KEY=your_api_key_here
API_SECRET=your_api_secret_here
```
 5. **Create and activate a virtual environment**

```bash
python -m venv env
source env/bin/activate       # On macOS/Linux
env\Scripts\activate          # On Windows
```
 6.**Install dependencies**

```bash
pip install -r requirements.txt
```
 7.**Run the Django server**

```bash
python manage.py runserver
```

  
