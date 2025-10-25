# MaxLikes API - Vercel Deployment

Complete deployment package for MaxLikes API on Vercel with Flask backend and IND server frontend.

## 📁 Project Structure

```
vercel/
├── index.html              # Simple IND server frontend
├── admin.html              # Full admin panel
├── api/
│   ├── app.py             # Main Flask application
│   ├── wsgi.py            # WSGI entry point
│   ├── like_pb2.py        # Protobuf definitions
│   ├── like_count_pb2.py  # Protobuf definitions
│   ├── uid_generator_pb2.py # Protobuf definitions
│   ├── token_ind.json     # India server tokens
│   ├── token_br.json      # Brazil/US/SAC/NA tokens
│   └── token_bd.json      # Bangladesh tokens
├── vercel.json            # Vercel configuration
├── requirements.txt       # Python dependencies
├── package.json           # Node.js package info
└── README.md              # This file
```

## 🚀 Quick Deploy to Vercel

### Step 1: Prepare Your Repository

1. Make sure all files from this `vercel` folder are in your Git repository
2. Push to GitHub, GitLab, or Bitbucket

### Step 2: Deploy on Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "**New Project**"
3. Import your repository
4. **Root Directory**: Select the `vercel` folder
5. Click "**Deploy**"

### Step 3: Configure Environment Variables

After deployment, you **MUST** set these environment variables:

1. Go to your project in Vercel Dashboard
2. Click "**Settings**" → "**Environment Variables**"
3. Add the following variables:

#### Required Variables:

**SECRET_KEY**
- **Value**: Generate using this command (or use provided value):
  ```bash
  python -c 'import os; print(os.urandom(24).hex())'
  ```
- **Example**: `113bc91b9709b90b13dbddb44b5797d3f1656f68f8c163c3`
- **Purpose**: Flask session management across serverless functions

**ADMIN_PASSWORD**
- **Value**: `thethestar` (or your custom password)
- **Purpose**: Admin panel login password

4. Click "**Save**" for each variable
5. **Redeploy** your app for changes to take effect

## 📱 Using Your Deployed App

After deployment, you'll get a URL like: `https://your-project.vercel.app`

### Frontend Pages:

- **IND Server Interface**: `https://your-project.vercel.app/`
  - Simple interface to send likes to IND server
  - Shows available token count
  - Enter UID and send likes instantly

- **Admin Panel**: `https://your-project.vercel.app/admin`
  - Full-featured admin panel
  - Test all servers (IND, BR, US, SAC, NA, BD)
  - Monitor API statistics
  - Requires password login

### API Endpoints:

- **Send Likes**: `GET /like?uid={UID}&server_name={SERVER}&key=gst`
  - Example: `/like?uid=123456789&server_name=IND&key=gst`

## 🔧 Configuration Files Explained

### vercel.json
Configures how Vercel builds and routes your application:
- Uses Python runtime for backend (`api/app.py`)
- Routes all API calls through Flask
- Serves static HTML pages

### requirements.txt
Python dependencies for the Flask backend:
- Flask, aiohttp, requests
- Protobuf for data serialization
- PyCryptodome for encryption

### package.json
Node.js package metadata (required by Vercel even for Python apps)

## 🎨 Frontend Features (index.html)

The IND server interface includes:

✅ **Live Token Count** - Shows how many tokens are available  
✅ **UID Input** - Enter the Free Fire user ID  
✅ **Like Preview** - Shows how many likes will be sent  
✅ **Send Button** - Instantly sends likes  
✅ **Real-time Results** - Shows success/failure with details  
✅ **Beautiful Design** - Matches the admin panel purple gradient theme  

## 📝 Token Configuration

Your tokens are stored in JSON files:

- `api/token_ind.json` - India server tokens
- `api/token_br.json` - Brazil, US, SAC, NA server tokens
- `api/token_bd.json` - Bangladesh server tokens

**Format**:
```json
[
  {"token": "your_token_here"},
  {"token": "another_token"},
  ...
]
```

## 🔐 Security Features

✅ Password-protected admin panel  
✅ Secure session management  
✅ Environment variables for sensitive data  
✅ Password hashing with werkzeug  
✅ HTTPS by default on Vercel  

## 🐛 Troubleshooting

### "Application Error" on Vercel

**Solution**: Make sure you've set the environment variables (`SECRET_KEY` and `ADMIN_PASSWORD`)

### "Token count shows ?"

**Solution**: Make sure your token JSON files are in the `api/` folder

### "Failed to connect to server"

**Solution**: 
1. Check that your API URL in index.html is correct
2. Make sure Vercel deployment was successful
3. Check Vercel function logs for errors

### Login not working

**Solution**: 
1. Ensure `ADMIN_PASSWORD` environment variable is set
2. Redeploy after adding environment variables

## 📊 Monitoring

View logs and monitor your deployment:

1. Go to Vercel Dashboard
2. Select your project
3. Click "**Deployments**" → Select latest deployment
4. Click "**Functions**" to see serverless function logs
5. Check "**Runtime Logs**" for debugging

## 🔄 Updating Your Deployment

To update your app:

1. Make changes to your code
2. Commit and push to your Git repository
3. Vercel automatically redeploys

Or manually redeploy:
1. Go to Vercel Dashboard
2. Click "**Deployments**"
3. Click "**⋮**" → "**Redeploy**"

## 💡 Tips

- Vercel serverless functions have a **10-second timeout** by default
- Keep token files small for faster cold starts
- Use Vercel's built-in analytics to monitor usage
- Set up custom domain in Vercel settings for professional URLs

## 🆘 Support

If you encounter issues:
1. Check Vercel function logs
2. Verify all environment variables are set
3. Ensure token files are properly formatted
4. Check that Flask routes are working locally first

## 📄 License

This project is provided as-is for deployment purposes.
