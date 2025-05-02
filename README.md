<h2 align="center">
    ──「 💫 ᴀʙɪʀ ダ sᴍᴀʀᴛ✘ᴍᴜsɪᴄ 💫 」──
</h2>

<p align="center">
  <img src="https://telegra.ph/file/56d1760224589ee370186.jpg">
</p>

<p align="center">
<a href="https://github.com/abirxdhack/SmartXMusic/stargazers"><img src="https://img.shields.io/github/stars/abirxdhack/SmartXMusic?color=black&logo=github&logoColor=black&style=for-the-badge" alt="Stars" /></a>
<a href="https://github.com/abirxdhack/SmartXMusic/network/members"> <img src="https://img.shields.io/github/forks/abirxdhack/SmartXMusic?color=black&logo=github&logoColor=black&style=for-the-badge" /></a>
<a href="https://github.com/abirxdhack/SmartXMusic/blob/master/LICENSE"> <img src="https://img.shields.io/badge/License-MIT-blueviolet?style=for-the-badge" alt="License" /> </a>
<a href="https://www.python.org/"> <img src="https://img.shields.io/badge/Written%20in-Python-orange?style=for-the-badge&logo=python" alt="Python" /> </a>
<a href="https://github.com/abirxdhack/SmartXMusic/commits/main"> <img src="https://img.shields.io/github/last-commit/abirxdhack/SmartXMusic?color=blue&logo=github&logoColor=green&style=for-the-badge" /></a>
</p>

<p align="center">
  <img src="https://telegra.ph/file/36be820a8775f0bfc773e.jpg">
</p>

---

<h3 align="center">
    📼   𓆩 ˹sᴍᴀʀᴛ✘ᴍᴜsɪᴄ ✘ ғᴇᴀᴛᴜʀᴇs˼ 𓆪   📼
</h3>

⚡️ **ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ᴜʟᴛɪᴍᴀᴛᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 💌**

✨ **Lag-Free Music Streaming**: High-quality audio with minimal latency.  
✨ **Advanced Neon Welcome Messages**: Customizable, vibrant group welcomes.  
✨ **Lightweight but Powerful Performance**: Optimized for efficiency and speed.  
✨ **Real-Time Performance Optimization**: Dynamic resource management for uninterrupted streaming.  
✨ **No Promotional Content or Unwanted Shits**: Clean, ad-free experience.  
✨ **Easy-to-Use Interface for Beginners**: Intuitive commands for all users.  

---

<h3 align="center">
    ─「 📖 ɪɴᴛʀᴏᴅᴜᴄᴛɪᴏɴ 」─
</h3>

Welcome to **SmartXMusic**, a redefined Telegram Music Bot that provides advanced tools for managing group music sessions. This bot is a **Fork** of the popular [AnonXMusic](https://github.com/AnonymousX1025/AnonXMusic), enhanced with additional features and bug fixes for a seamless user experience.

With **SmartXMusic**, you can enjoy:  
💥 **Improved Stability**: Say goodbye to crashes and loop errors!  
⭐️ **Enhanced Features**: Optimized performance and real-time updates.  
🌐 **User-Friendly Interface**: Simple, intuitive, and lightweight.  

Whether you're hosting music sessions or managing a Telegram group, **SmartXMusic** is your ultimate companion for uninterrupted and advanced music streaming.

---

<h3 align="center">
    ─「 🔧 ᴠᴀʀɪᴀʙʟᴇs 」─
</h3>

#### Mandatory Variables:
To deploy and run the bot, you must set the following environment variables:
- **`API_ID`**: Telegram API ID (get it from [my.telegram.org](https://my.telegram.org)).  
- **`API_HASH`**: Telegram API Hash (get it from [my.telegram.org](https://my.telegram.org)).  
- **`BOT_TOKEN`**: Bot token from [BotFather](https://t.me/BotFather).  
- **`SESSION_STRING`**: Pyrogram session string for the bot.  
  *(Use only one session string and one user client for simplicity and reliability ❄️)*

#### Recommended Variables:
These optional variables enhance the bot's functionality:
- **`LOG_GROUP_ID`**: Group ID for logging events.  
- **`MONGO_DB_URI`**: MongoDB connection string for database support.  
- **`OWNER_ID`**: Telegram User ID of the bot owner for admin privileges.  
- **`HEROKU_APP_NAME`**: Set this if deploying on Heroku.  
- **`HEROKU_API_KEY`**: Heroku API key for managing dynos.  

For a complete list of variables and their descriptions, refer to the [sample.env](https://github.com/abirxdhack/SmartXMusic/blob/master/sample.env) file.

---

<h3 align="center">
    ─「 DEPLOYMENT OPTIONS 」─
</h3>

Below are detailed tutorials for deploying **SmartXMusic** on various platforms, including enhanced instructions for Docker, Docker Compose, Heroku, and Localhost/VPS setups.

### Deploy on Heroku
<p align="center">
<a href="https://dashboard.heroku.com/new?template=https://github.com/abirxdhack/SmartXMusic"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a>
</p>

#### Heroku Deployment Steps:
1. **Create a Heroku Account**: Sign up at [heroku.com](https://heroku.com) if you don’t have an account.
2. **Install Heroku CLI**: Download and install the Heroku CLI from [heroku.com](https://devcenter.heroku.com/articles/heroku-cli).
3. **Log in to Heroku**:
   ```bash
   heroku login
   ```
4. **Fork the Repository**: Fork [SmartXMusic](https://github.com/abirxdhack/SmartXMusic) to your GitHub account.
5. **Deploy via Heroku Dashboard**:
   - Click the "Deploy to Heroku" button above.
   - Enter your app name and fill in the mandatory variables (`API_ID`, `API_HASH`, `BOT_TOKEN`, `SESSION_STRING`).
   - Optionally, add recommended variables like `LOG_GROUP_ID`, `MONGO_DB_URI`, etc.
6. **Enable Dynos**:
   - Go to the "Resources" tab in your Heroku app dashboard.
   - Enable the `worker` dyno to start the bot.
7. **Monitor Logs**:
   ```bash
   heroku logs --tail
   ```

#### Troubleshooting Heroku:
- **Dyno Crashes**: Ensure all mandatory variables are correctly set.
- **Quota Limits**: Heroku free tier has limited hours; consider upgrading to a paid plan for continuous uptime.
- **Session String Issues**: Generate a new session string using Our Safe Bot  [@ItsSmartToolBot](https://t.me/ItsSmartToolBot) And /pyro Command And Then Follow Steps

---

### Deploy on Localhost/VPS
This method is ideal for users with access to a Linux-based server or local machine.

#### Prerequisites:
- A Linux-based system (Ubuntu recommended).
- Basic knowledge of terminal commands.
- Internet connection for downloading dependencies.

#### Step-by-Step Setup:
1. **Update and Upgrade System**:
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   ```
2. **Install FFmpeg and Python**:
   ```bash
   sudo apt-get install python3-pip ffmpeg -y
   ```
3. **Install pip**:
   ```bash
   sudo pip3 install -U pip
   ```
4. **Install Node.js**:
   ```bash
   curl -fssL https://deb.nodesource.com/setup_19.x | sudo -E bash - && sudo apt-get install nodejs -y && npm i -g npm
   ```
5. **Clone the Repository**:
   ```bash
   git clone https://github.com/abirxdhack/SmartXMusic && cd SmartXMusic
   ```
6. **Install Python Requirements**:
   ```bash
   pip3 install -U -r requirements.txt
   ```
7. **Set Up Environment Variables**:
   - Copy the sample environment file:
     ```bash
     cp sample.env .env
     ```
   - Edit the `.env` file:
     ```bash
     nano .env
     ```
     Fill in the mandatory variables (`API_ID`, `API_HASH`, `BOT_TOKEN`, `SESSION_STRING`) and any optional ones. Save and exit (`Ctrl+O`, `Enter`, `Ctrl+X`).
8. **Install tmux for Persistent Sessions**:
   ```bash
   sudo apt install tmux && tmux
   ```
9. **Run the Bot**:
   ```bash
   bash start
   ```
10. **Detach from tmux**:
    - Press `Ctrl+B`, then `D` to detach and keep the bot running.
    - To reattach later:
      ```bash
      tmux attach
      ```

#### Troubleshooting Localhost/VPS:
- **FFmpeg Errors**: Ensure FFmpeg is installed correctly (`ffmpeg -version`).
- **Python Dependency Issues**: Run `pip3 install -U -r requirements.txt` again.
- **Port Conflicts**: Ensure no other service is using the bot’s default port.
- **Session String Expired**: Generate a new session string and update `.env`.

---

### Deploy with Docker Compose
Docker Compose simplifies deployment by managing dependencies in a containerized environment. This is the most reliable method for consistent performance across systems.

#### Prerequisites:
- A system with Docker and Docker Compose installed.
- Basic knowledge of Docker commands.

#### Install Docker and Docker Compose:
1. **Install Docker on Ubuntu**:
   ```bash
   sudo apt-get update
   sudo apt-get install -y docker.io
   sudo systemctl start docker
   sudo systemctl enable docker
   ```
   Verify installation:
   ```bash
   docker --version
   ```
2. **Install Docker Compose**:
   ```bash
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```
   Verify installation:
   ```bash
   docker-compose --version
   ```
3. **Add User to Docker Group** (to run Docker without sudo):
   ```bash
   sudo usermod -aG docker $USER
   ```
   Log out and log back in for the change to take effect.

#### Docker Compose Deployment Steps:
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/abirxdhack/SmartXMusic && cd SmartXMusic
   ```
2. **Set Up Environment Variables**:
   - Copy the sample environment file:
     ```bash
     cp sample.env .env
     ```
   - Edit the `.env` file:
     ```bash
     nano .env
     ```
     Add mandatory variables (`API_ID`, `API_HASH`, `BOT_TOKEN`, `SESSION_STRING`) and optional ones. Save and exit.
3. **Build and Start the Bot**:
   ```bash
   docker compose up --build --remove-orphans
   ```
   This command builds the Docker image and starts the bot in a container.
4. **Run in Detached Mode** (optional):
   ```bash
   docker compose up -d
   ```
5. **View Logs**:
   ```bash
   docker compose logs -f
   ```
6. **Stop the Bot**:
   ```bash
   docker compose down
   ```

#### Troubleshooting Docker Compose:
- **Docker Not Running**: Ensure Docker is running (`sudo systemctl status docker`).
- **Permission Denied**: Run commands with `sudo` or add your user to the Docker group.
- **Image Build Fails**: Check for errors in `Dockerfile` or `docker-compose.yml`. Ensure all dependencies are listed in `requirements.txt`.
- **Container Exits Immediately**: Verify that all mandatory variables are set in `.env`.
- **Port Conflicts**: Modify `docker-compose.yml` to use a different port if needed.

#### Advantages of Docker Compose:
- **Isolated Environment**: Prevents dependency conflicts.
- **Easy Scaling**: Adjust resources in `docker-compose.yml`.
- **Portability**: Run the same setup on any system with Docker.

---

<h3 align="center">
    ─「 SUPPORT 」─
</h3>

<p align="center">
<a href="https://telegram.me/TheSmartDev"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
<a href="https://telegram.me/ISmartDevs"><img src="https://img.shields.io/badge/-Support%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

---

### Special Thanks
- _Special thanks to [ᴛᴇᴀᴍ ʏᴜᴋᴋɪ](https://github.com/TeamYukki) for [ʏᴜᴋᴋɪ ᴍᴜsɪᴄ ʙᴏᴛ](https://github.com/TeamYukki/YukkiMusicBot)_  
- _Special thanks to ˹ᴛʜᴇ ғᴧʟʟᴇɴ ᴧssᴏᴄɪᴀᴛɪᴏɴ˼ for [AnonXMusic](https://github.com/AnonymousX1025/AnonXMusic)_ 🌐
